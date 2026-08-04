import json
import netmiko
from netmiko import ConnectHandler

# Prompt user for info
user_m = input('What is your monitor number? ')

# 3 basic steps (WRITE, CONNECT, PUSH)

# WRITE - device info and commands.
# Read the json file.
with open('taas-configs.json') as file:
    # Convert json data types to python data types.
    json_configs = json.load(file)

# Update the key[ip] from the json file with the user's coretaas ip address.
json_configs['device_info']['ip'] = f'10.{user_m}.1.2'

# Parse data:
# ConnectHandler arguments to establish SSH connection to device.
device_info = json_configs['device_info']

# Values for commands.
ips = json_configs['ips']
svi = ips['svi']

# Commands to be sent to the device.
ip_commands = [
    # Console access
    'line cons 0',
    f'password {ips["password"]}',
    'login',
    f'exec-timeout {ips['no_timeout']}',
    'exit',
    
    # Interface IPs
    'int vlan 10',
    'no shut',
    f'ip add 10.{user_m}.{svi['v10']} {ips['mask_24']}',
    f'desc mgmtWifi{ips['via_py']}',
    'exit',
    'int vlan 50',
    'no shut',
    f'ip add 10.{user_m}.{svi['v50']} {ips['mask_24']}',
    f'desc mgmtCCTV{ips['via_py']}',
    'exit',
    'int vlan 100',
    'no shut',
    f'ip add 10.{user_m}.{svi['v100']} {ips['mask_24']}',
    f'desc mgmtVOICE-{ips['via_py']}',
    'exit'
]

# CONNECT - to the device.
# Establish connection by accessing the cli.
accessCLI = ConnectHandler(**device_info)


# PUSH - commands to the device.
# Print statements to inform the user the current state of the script.
print('Configuring device...')
output = accessCLI.send_config_set(ip_commands)

# Print the cli to the terminal.
print(output)

print('Configuration Successful!!!\n\n')