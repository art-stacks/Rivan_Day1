import netmiko
from netmiko import ConnectHandler

# prompt user for info
user_m = input('What is your monitor number? ')
cam6_mac = input('''
What is the MAC address of the device on fa0/6?
Enter in period separated format ( xxxx.xxxx.xxxx )
''')
cam8_mac = input('''
What is the MAC address of the device on fa0/8?
Enter in period separated format ( xxxx.xxxx.xxxx )
''')


# 3 Steps (WRITE, CONNECT, PUSH)

# WRITE - device info and commands
# ConnectHandler arguments to establish SSH connection to device
device_info = {
    'device_type': 'cisco_ios',
    'ip': f'10.{user_m}.1.4',
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
    'int vlan 10',
    'no shut',
    f'ip add 10.{user_m}.10.4 255.255.255.0',
    'desc mgmtWifi-configured-via-python',
    'exit',
    'int vlan 50',
    'no shut',
    f'ip add 10.{user_m}.50.4 255.255.255.0',
    'desc mgmtCCTV--configured-via-python',
    'exit'
]

dhcp_commands = [
    # exclude ips
    f'ip dhcp excluded-add 10.{user_m}.1.1 10.{user_m}.1.100',
    f'ip dhcp excluded-add 10.{user_m}.10.1 10.{user_m}.10.100',
    f'ip dhcp excluded-add 10.{user_m}.50.1 10.{user_m}.50.100',
    f'ip dhcp excluded-add 10.{user_m}.100.1 10.{user_m}.100.100',
    
    # dhcp pool
    'ip dhcp pool POOLDATA',
    f'network 10.{user_m}.1.0 255.255.255.0',
    f'default-router 10.{user_m}.1.4',
    'domain-name MGMTDATA.COM',
    f'dns-server 10.{user_m}.1.10',
    'exit',

    'ip dhcp pool POOLWIFI',
    f'network 10.{user_m}.10.0 255.255.255.0',
    f'default-router 10.{user_m}.10.4',
    'domain-name WIFIDATA.COM',
    f'dns-server 10.{user_m}.1.10',
    'exit',

    'ip dhcp pool POOLCCTV',
    f'network 10.{user_m}.50.0 255.255.255.0',
    f'default-router 10.{user_m}.50.4',
    'domain-name CCTVDATA.COM',
    f'dns-server 10.{user_m}.1.10',
    'exit',

    'ip dhcp pool POOLVOICE',
    f'network 10.{user_m}.100.0 255.255.255.0',
    f'default-router 10.{user_m}.100.4',
    'domain-name VOICEDATA.COM',
    f'dns-server 10.{user_m}.1.10',
    f'option 150 ip 10.{user_m}.100.8',
    'exit'
]

switchport_commands = [
    # create vlans
    'vlan 1',
    'name MGMTVLAN',
    'exit',
    'vlan 10',
    'name WIFIVLAN',
    'exit',
    'vlan 50',
    'name CCTVVLAN',
    'exit',
    
    # access/voice port
    'int fa 0/2',
    'switchport mode access',
    'switchport access vlan 10',
    'exit',
    'int fa 0/4',
    'switchport mode access',
    'switchport access vlan 10',
    'exit',
    'int fa 0/6',
    'switchport mode access',
    'switchport access vlan 50',
    'exit',
    'int fa 0/8',
    'switchport mode access',
    'switchport access vlan 50',
    'exit',
    'int fa 0/5',
    'switchport mode access',
    'switchport voice vlan 100',
    'switchport access vlan 1',
    'mls qos trust device cisco-phone',
    'exit',
    'int fa 0/7',
    'switchport mode access',
    'switchport voice vlan 100',
    'switchport access vlan 1',
    'mls qos trust device cisco-phone',
    'exit'   
]

reserve_commands = [
    # reserve ips
    'ip dhcp pool CAMERA6',
    f'host 10.{user_m}.50.6 255.255.255.0',
    f'client-identifier {cam6_mac}',
    'exit',
    'ip dhcp pool CAMERA8',
    f'host 10.{user_m}.50.8 255.255.255.0',
    f'client-identifier {cam8_mac}',
    'exit'
]

ospf_commands = [
    # dynamic routing
    'router ospf 1',
    f'router-id 10.{user_m}.{user_m}.4',
    f'network 10.{user_m}.0.0 0.0.255.255 area 0',
    'exit',
    'int gi 0/1',
    'ip ospf network point-to-point',
    'exit'
]


# CONNECT - to the device
# Establish connection and access cli
accessCLI = ConnectHandler(**device_info)

# PUSH - commands to the device
order_of_config = ['IP addresses', 'DHCP', 'Switchport', 'Reserved IPs', 'OSPF Routing']

for config in order_of_config:
    # inform user what is currently being configured
    print('~'*15 + f'\nConfiguring {config}...')
    
    if config == 'IP addresses':
        output = accessCLI.send_config_set(ip_commands)
    elif config == 'DHCP':
        output = accessCLI.send_config_set(dhcp_commands)
    elif config == 'Switchport':
        output = accessCLI.send_config_set(switchport_commands)
    elif config == 'Reserved IPs':
        output = accessCLI.send_config_set(reserve_commands)
    else:
        output = accessCLI.send_config_set(ospf_commands)
    
    # print cli output on the terminal
    print(output)
    
    print('Configuration Successful!!!\n')