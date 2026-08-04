import netmiko
from netmiko import ConnectHandler

# prompt user for info
user_m = input('What is your monitor number? ')

# 3 Steps (WRITE, CONNECT, PUSH)

# WRITE - device info and commands
# ConnectHandler arguments to establish SSH connection to device
device_info = {
    'device_type': 'cisco_ios',
    'ip': f'10.{user_m}.1.2',
    'port': 22,
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass'
}

# Commands to be sent to the device
ip_commands = [
    # console access
    'line cons 0',
    'password pass',
    'login',
    'exec-timeout 0 0',
    'exit',
    
    # interface IPs
    'int vlan 10',
    'no shut',
    f'ip add 10.{user_m}.10.2 255.255.255.0',
    'desc mgmtWifi-configured-via-python',
    'exit',
    'int vlan 50',
    'no shut',
    f'ip add 10.{user_m}.50.2 255.255.255.0',
    'desc mgmtCCTV--configured-via-python',
    'exit',
    'int vlan 100',
    'no shut',
    f'ip add 10.{user_m}.100.2 255.255.255.0',
    'desc mgmtCCTV--configured-via-python',
    'exit'
]

# CONNECT - to the device
# Establish connection and access cli
accessCLI = ConnectHandler(**device_info)


# PUSH - commands to the device
# inform user what is currently being configured
print('Configuring device...')
output = accessCLI.send_config_set(ip_commands)

# print cli output on the terminal
print(output)

print('Configuration Successful!!!\n')

#pprint.pp(reserve_commands, indent=4)