import json
import netmiko
from netmiko import ConnectHandler

# Prompt user for info
user_m = input('What is your monitor number? ')

# 3 basic steps (WRITE, CONNECT, PUSH)

# WRITE - device info and commands.
# Read the json file.
with open('edge-configs.json') as file:
    # Convert json data to usable python data.
    json_configs = json.load(file)

# Update the key[ip] from the json file with the user's coretaas ip address
json_configs['device_info']['ip'] = f'10.{user_m}.{user_m}.1'

# Parse data:
# ConnectHandler arguments to establish SSH connection to device.
device_info = json_configs['device_info']

# Values for commands.
ips = json_configs['ips']
all_monitors = json_configs['active_monitors']
ospf = json_configs['ospf']

# Commands are separated per variable for more user readability.
ip_commands = [
    # Console access
    'line cons 0',
    f'password {ips["password"]}',
    'login',
    f'exec-timeout {ips["no_timeout"]}',
    'exit',
    
    # Interface IPs
    'int gi 0/0/1',
    'no shut',
    f'ip add {ips["gi0/0/1"]}.{user_m} {ips["mask_24"]}',
    f'desc OUTSIDE{ips["via_py"]}',
    'exit',
    'int loopback 0',
    'no shut',
    f'ip add {user_m}.{ips["lo0"]} {ips["mask_32"]}',
    f'desc VIRTUALIP{ips["via_py"]}',
    'exit'
]

static_inside_commands = [
    # Floating default route
    'ip routing',
    f'ip route 10.{user_m}.0.0 {ips["mask_16"]} 10.{user_m}.{user_m}.4 120'
]

# Floating static route to other pcs.
list_of_monitors = all_monitors.split(',')
static_outside_commands = []
for monitor in list_of_monitors:
    per_static_route = [
        f'ip route 10.{monitor}.0.0 {ips["mask_16"]} {ips["gi0/0/1"]}.{monitor} 120'
    ]
    static_outside_commands.append(per_static_route[0])

ospf_commands = [
    # Dynamic routing
    f'router ospf {ospf["process"]}',
    f'router-id {user_m}.0.0.1',
    f'network {ips["gi0/0/1"]}.0 {ips["wild_24"]} {ospf["area"]}',
    f'network 10.{user_m}.{user_m}.0 {ips["wild_24"]} {ospf["area"]}',
    f'network {user_m}.0.0.1 {ips["wild_32"]} {ospf["area"]}',
    'int gi 0/0/0',
    'ip ospf network point-to-point',
    'exit'
]


# CONNECT - to the device.
# Establish connection by accessing the cli.
accessCLI = ConnectHandler(**device_info)

# PUSH - commands to the device.
order_of_config = ['IP addresses', 'Inside floating static routes', 'Outside floating static routes', 'OSPF Routing']

# Inform user what is currently being configured
for config in order_of_config:
    print('~'*15 + f'\nConfiguring {config}...')
    
    if config == 'IP addresses':
        output = accessCLI.send_config_set(ip_commands)
    elif config == 'Inside floating static routes':
        output = accessCLI.send_config_set(static_inside_commands)
    elif config == 'Outside floating static routes':
        output = accessCLI.send_config_set(static_outside_commands)
    else:
        output = accessCLI.send_config_set(ospf_commands)
    
    # Print the cli to the terminal.
    print(output)
    
    print('Configuration Successful!!!\n\n')