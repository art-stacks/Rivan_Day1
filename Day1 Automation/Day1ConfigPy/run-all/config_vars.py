def getUserInfo():
    user_m = input('What is your monitor number? ')

    cam6_mac = input('''
    What is the MAC address of the device on fa0/6?
    Enter in period separated format ( xxxx.xxxx.xxxx ):
        ''')

    cam8_mac = input('''
    What is the MAC address of the device on fa0/8?
    Enter in period separated format ( xxxx.xxxx.xxxx ):
        ''')

    ephone_1_mac = input('''
    What is the MAC address of the device on fa0/5?
    Enter in period separated format ( xxxx.xxxx.xxxx ):
        ''')

    ephone_2_mac = input('''
    What is the MAC address of the device on fa0/7?
    Enter in period separated format ( xxxx.xxxx.xxxx ):
        ''')
    
    user_info = {
        'monitor_num': user_m, 
        'cam6_mac_address': cam6_mac, 
        'cam8_mac_address': cam8_mac, 
        'ephone1_mac_address': ephone_1_mac, 
        'ephone2_mac_address': ephone_2_mac
    }
    
    return user_info

# prompt user for their monitor number and mac addresses
user_info = getUserInfo()

# parse info to their respective variable
user_m = user_info['monitor_num']
cam6_mac = user_info['cam6_mac_address']
cam8_mac = user_info['cam8_mac_address']
ephone_1_mac = user_info['ephone1_mac_address']
ephone_2_mac = user_info['ephone2_mac_address']

# commands to be pushed to devices
coretaas_config = [
    # console access
    f'hostname coreTAAS-{user_m}',
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
    'exit',
]

corebaba_config = [
    # console access
    f'hostname coreBABA-{user_m}',
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
    'exit',
    
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
    f'option 43 ip 10.{user_m}.10.{user_m}',
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
    'exit',

    # create vlans
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
    'exit',
    
    # reserve ips
    'ip dhcp pool CAMERA6',
    f'host 10.{user_m}.50.6 255.255.255.0',
    f'client-identifier {cam6_mac}',
    'exit',
    'ip dhcp pool CAMERA8',
    f'host 10.{user_m}.50.8 255.255.255.0',
    f'client-identifier {cam8_mac}',
    'exit',
    
    # static routing
    'ip routing',
    f'ip route 0.0.0.0 0.0.0.0 10.{user_m}.{user_m}.1 254',

    # dynamic routing
    'router ospf 1',
    f'router-id 10.{user_m}.{user_m}.4',
    f'network 10.{user_m}.0.0 0.0.255.255 area 0',
    'exit',
    'int gi 0/1',
    'ip ospf network point-to-point',
    'exit'
]

cucm_config = [
    # console access
    f'hostname CUCM-{user_m}',
    'line cons 0',
    'password pass',
    'login',
    'exec-timeout 0 0',
    'exit',
    
    # configure analog phones
    'dial-peer voice 1 pots',
    f'destination-pattern {user_m}00',
    'port 0/0/0',
    'exit',
    'dial-peer voice 2 pots',
    f'destination-pattern {user_m}01',
    'port 0/0/1',
    'exit',
    'dial-peer voice 3 pots',
    f'destination-pattern {user_m}02',
    'port 0/0/2',
    'exit',
    'dial-peer voice 4 pots',
    f'destination-pattern {user_m}03',
    'port 0/0/3',
    'exit',
    
    # configure telephony
    'no telephony-service',
    'telephony-service',
    'no auto assign',
    'no auto-reg-ephone',
    'max-ephones 5',
    'max-dn 20',
    f'ip source-address 10.{user_m}.100.8 port 2000',
    'create cnf-files',
    'ephone-dn 1',
    f'number {user_m}11',
    'ephone-dn 2',
    f'number {user_m}22',
    'ephone-dn 3',
    f'number {user_m}33',
    'ephone-dn 4',
    f'number {user_m}44',
    'ephone-dn 5',
    f'number {user_m}55',
    'ephone-dn 6',
    f'number {user_m}66',
    'ephone-dn 7',
    f'number {user_m}77',
    'ephone-dn 8',
    f'number {user_m}88',
    'ephone 1',
    f'mac-address {ephone_1_mac}',
    'type 8945',
    'button 1:1 2:2 3:3 4:4',
    'restart',
    'ephone 2',
    f'mac-address {ephone_2_mac}',
    'type 8945',
    'button 1:5 2:6 3:7 4:8',
    'restart',
    'exit',
    
    # enable video calls
    'ephone 1',
    'video',
    'voice service voip',
    'h323',
    'call start slow',
    'ephone 2',
    'video',
    'voice service voip',
    'h323',
    'call start slow',
    'exit',

    # allow incoming calls
    'voice service voip',
    'ip address trusted list',
    'ipv4 0.0.0.0 0.0.0.0',
    'exit',

    # allow outgoing calls
    'dial-peer voice 11 Voip',
    'destination-pattern 11..',
    'session target ipv4:10.11.100.8',
    'codec g711ULAW',
    'dial-peer voice 12 Voip',
    'destination-pattern 12..',
    'session target ipv4:10.12.100.8',
    'codec g711ULAW',
    'dial-peer voice 21 Voip',
    'destination-pattern 21..',
    'session target ipv4:10.21.100.8',
    'codec g711ULAW',
    'dial-peer voice 22 Voip',
    'destination-pattern 22..',
    'session target ipv4:10.22.100.8',
    'codec g711ULAW',
    'dial-peer voice 31 Voip',
    'destination-pattern 31..',
    'session target ipv4:10.31.100.8',
    'codec g711ULAW',
    'dial-peer voice 32 Voip',
    'destination-pattern 32..',
    'session target ipv4:10.32.100.8',
    'codec g711ULAW',
    'dial-peer voice 41 Voip',
    'destination-pattern 41..',
    'session target ipv4:10.41.100.8',
    'codec g711ULAW',
    'dial-peer voice 42 Voip',
    'destination-pattern 42..',
    'session target ipv4:10.42.100.8',
    'codec g711ULAW',
    'dial-peer voice 51 Voip',
    'destination-pattern 51..',
    'session target ipv4:10.51.100.8',
    'codec g711ULAW',
    'dial-peer voice 52 Voip',
    'destination-pattern 52..',
    'session target ipv4:10.52.100.8',
    'codec g711ULAW',
    'dial-peer voice 61 Voip',
    'destination-pattern 61..',
    'session target ipv4:10.61.100.8',
    'codec g711ULAW',
    'dial-peer voice 62 Voip',
    'destination-pattern 62..',
    'session target ipv4:10.62.100.8',
    'codec g711ULAW',
    'dial-peer voice 71 Voip',
    'destination-pattern 71..',
    'session target ipv4:10.71.100.8',
    'codec g711ULAW',
    'dial-peer voice 72 Voip',
    'destination-pattern 72..',
    'session target ipv4:10.72.100.8',
    'codec g711ULAW',
    'dial-peer voice 81 Voip',
    'destination-pattern 81..',
    'session target ipv4:10.81.100.8',
    'codec g711ULAW',
    'dial-peer voice 82 Voip',
    'destination-pattern 82..',
    'session target ipv4:10.82.100.8',
    'codec g711ULAW',
    'dial-peer voice 91 Voip',
    'destination-pattern 91..',
    'session target ipv4:10.91.100.8',
    'codec g711ULAW',
    'dial-peer voice 91 Voip',
    'destination-pattern 92..',
    'session target ipv4:10.92.100.8',
    'codec g711ULAW',
    'exit',
    
    # -configure ivrs
    f'dial-peer voice {user_m} voip',
    'service rivanaa out-bound',
    f'destination-pattern {user_m}69',
    f'session target ipv4:10.{user_m}.100.8',
    f'incoming called-number {user_m}69',
    'dtmf-relay h245-alphanumeric',
    'codec g711ulaw',
    'no vad',

    'telephony-service',
    r'moh "flash:/en_bacd_music_on_hold.au"',

    'application',
    'service rivanaa flash:app-b-acd-aa-3.0.0.2.tcl',
    'paramspace english index 1',
    'param number-of-hunt-grps 2',
    'param dial-by-extension-option 8',
    'param handoff-string rivanaa',
    'param welcome-prompt flash:en_bacd_welcome.au',
    'paramspace english language en',
    'param call-retry-timer 15',
    'param service-name rivanqueue',
    r'paramspace english location flash:',
    'param second-greeting-time 60',
    'param max-time-vm-retry 2',
    'param voice-mail 1234',
    'param max-time-call-retry 700',
    'param aa-pilot _69',
    'service rivanqueue flash:app-b-acd-3.0.0.2.tcl',
    'param queue-len 15',
    f'param aa-hunt1 {user_m}00',
    f'param aa-hunt2 {user_m}01',
    f'param aa-hunt3 {user_m}77',
    f'param aa-hunt4 {user_m}33',
    'param queue-manager-debugs 1',
    'param number-of-hunt-grps 4',
    'exit',

    # static routing
    'ip routing',
    f'ip route 0.0.0.0 0.0.0.0 10.{user_m}.100.4 254',

    # dynamic routing
    'router ospf 1',
    f'router-id 10.{user_m}.100.8',
    f'network 10.{user_m}.100.0 0.0.0.255 area 0',
    'exit'
]

# force telephony numbers
register_ephones = [
    'telephony-service',
    'create cnf-files'
]

edge_config = [
    # console access
    f'hostname EDGE-{user_m}',
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
    'exit',
    
    # floating static route to other pcs
    'ip routing',
    'ip route 10.11.0.0 255.255.0.0 200.0.0.11 254',
    'ip route 10.12.0.0 255.255.0.0 200.0.0.12 254',
    'ip route 10.21.0.0 255.255.0.0 200.0.0.21 254',
    'ip route 10.22.0.0 255.255.0.0 200.0.0.22 254',
    'ip route 10.31.0.0 255.255.0.0 200.0.0.31 254',
    'ip route 10.32.0.0 255.255.0.0 200.0.0.32 254',
    'ip route 10.41.0.0 255.255.0.0 200.0.0.41 254',
    'ip route 10.42.0.0 255.255.0.0 200.0.0.42 254',
    'ip route 10.51.0.0 255.255.0.0 200.0.0.51 254',
    'ip route 10.52.0.0 255.255.0.0 200.0.0.52 254',
    'ip route 10.61.0.0 255.255.0.0 200.0.0.61 254',
    'ip route 10.62.0.0 255.255.0.0 200.0.0.62 254',
    'ip route 10.71.0.0 255.255.0.0 200.0.0.71 254',
    'ip route 10.72.0.0 255.255.0.0 200.0.0.72 254',
    'ip route 10.81.0.0 255.255.0.0 200.0.0.81 254',
    'ip route 10.82.0.0 255.255.0.0 200.0.0.82 254',
    f'ip route 10.{user_m}.0.0 255.255.0.0 10.{user_m}.{user_m}.4 253',
    
    # dynamic routing
    'router ospf 1',
    f'router-id {user_m}.0.0.1',
    'network 200.0.0.0 0.0.0.255 area 0',
    f'network 10.{user_m}.{user_m}.0 0.0.0.255 area 0',
    f'network {user_m}.0.0.1 0.0.0.0 area 0',
    'int gi 0/0/0',
    'ip ospf network point-to-point',
    'exit'
]

