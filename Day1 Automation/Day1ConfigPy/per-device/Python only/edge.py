import netmiko
from netmiko import ConnectHandler

# prompt user for info
user_m = input('What is your monitor number? ')

# 3 Steps (WRITE, CONNECT, PUSH)

# WRITE - device info and commands
# ConnectHandler arguments to establish SSH connection to device
device_info = {
    'device_type': 'cisco_ios',
    'ip': f'10.{user_m}.{user_m}.1',
    'port': 22,
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass'
}

# Commands are separated per variable for more user readability
ip_commands = [
    # console access
    'line cons 0',
    'password pass',
    'login',
    'exec-timeout 0 0',
    'exit',
    
    # interface IPs
    'int gi 0/0/1',
    'no shut',
    f'ip add 200.0.0.{user_m} 255.255.255.0',
    'desc OUTSIDE-configured-via-python',
    'exit',
    'int loopback 0',
    'no shut',
    f'ip add {user_m}.0.0.1 255.255.255.255',
    'desc VIRTUALIP-configured-via-python',
    'exit'
]

static_inside_commands = [
    # floating default route
    'ip routing',
    f'ip route 10.{user_m}.0.0 255.255.0.0 10.{user_m}.{user_m}.4 120'
]

# floating static route to other pcs
all_monitors = '11,12,21,22,31,32,41,42,51,52,61,62,71,72,81,82'
list_of_monitors = all_monitors.split(',')
static_outside_commands = []
for monitor in list_of_monitors:
    per_static_route = [
        f'ip route 10.{monitor}.0.0 255.255.0.0 200.0.0.{monitor} 120'
    ]
    static_outside_commands.append(per_static_route[0])

ospf_commands = [
    'router ospf 1',
    f'router-id {user_m}.0.0.1',
    'network 200.0.0.0 0.0.0.255 area 0',
    f'network 10.{user_m}.{user_m}.0 0.0.0.255 area 0',
    f'network {user_m}.0.0.1 0.0.0.0 area 0',
    'int gi 0/0/0',
    'ip ospf network point-to-point',
    'exit'
]


# CONNECT - to the device
# Establish connection and access cli
accessCLI = ConnectHandler(**device_info)

# PUSH - commands to the device
order_of_config = ['IP addresses', 'Inside floating static routes', 'Outside floating static routes', 'OSPF Routing']

for config in order_of_config:
    # inform user what is currently being configured
    print('~'*15 + f'\nConfiguring {config}...')
    
    if config == 'IP addresses':
        output = accessCLI.send_config_set(ip_commands)
    elif config == 'Inside floating static routes':
        output = accessCLI.send_config_set(static_inside_commands)
    elif config == 'Outside floating static routes':
        output = accessCLI.send_config_set(static_outside_commands)
    else:
        output = accessCLI.send_config_set(ospf_commands)
    
    # print cli output on the terminal
    print(output)
    
    print('Configuration Successful!!!\n')