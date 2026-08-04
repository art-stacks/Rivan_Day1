from netmiko import ConnectHandler
import json

# monitor number
m = '#$34T#'

# Read JSON File to obtain device info
with open('ctaas.json', 'r') as file:
    data = json.load(file)


# Parse Data
hostname = data['device_config']['hostname']
vl_70 = data['device_config']['address']['vlan_70']
vl_71 = data['device_config']['address']['vlan_71']
vl_72 = data['device_config']['address']['vlan_72']
mask_24 = data['device_config']['mask_24']


# Provide information about the host/s
ctaas = {
    'device_type': 'cisco_ios_telnet',
    'host': f'10.{m}.1.4',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23
}


# Write the configurations
ct_config = [
    f'hostname {hostname}',
    'int vlan 70',
    'no shut',
    f'ip add {vl_70['ipv4']} {mask_24}',
    f'desc {vl_70['desc']}',
    'int vlan 71',
    'no shut',
    f'ip add {vl_71['ipv4']} {mask_24}',
    f'desc {vl_71['desc']}',
    'int vlan 72',
    'no shut',
    f'ip add {vl_72['ipv4']} {mask_24}',
    f'desc {vl_72['desc']}',
    'end'
]

print(ct_config)


# Connect to the host/s
accesscli = ConnectHandler(**ctaas)


# Enable secret - Only IF Telnet Session
# accesscli.enable()


# Send show command/s
show_ip = accesscli.send_command('show ip interface brief')


# Push configurations
cli_output = accesscli.send_config_set(ct_config)


# Close connection
accesscli.disconnect()


print(cli_output)