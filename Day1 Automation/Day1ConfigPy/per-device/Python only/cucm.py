import netmiko
from netmiko import ConnectHandler

# prompt user for info
user_m = input('What is your monitor number? ')
ephone_1_mac = input('''
What is the MAC address of the device on fa0/5?
Enter in period separated format ( xxxx.xxxx.xxxx )
''')
ephone_2_mac = input('''
What is the MAC address of the device on fa0/7?
Enter in period separated format ( xxxx.xxxx.xxxx )
''')


# 3 Steps (WRITE, CONNECT, PUSH)

# WRITE - device info and commands
# ConnectHandler arguments to establish SSH connection to device
device_info = {
    'device_type': 'cisco_ios',
    'ip': f'10.{user_m}.100.8',
    'port': 22,
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass'
}


# Commands are separated per variable for more user readability
cons_commands = [
    # console access
    'line cons 0',
    'password pass',
    'login',
    'exec-timeout 0 0',
    'exit'
]

analog_commands = [
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
    'exit'
]

ephone_commands = [
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
    'exit'
]

vidcall_commands = [
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
    'exit'
]

incoming_commands = [
    # allow incoming calls
    'voice service voip',
    'ip address trusted list',
    'ipv4 0.0.0.0 0.0.0.0',
    'exit'
]

# allow outgoing calls
callers = '11,12,21,22,31,32,41,42,51,52,61,62,71,72,81,82'
list_of_callers = callers.split(',')
outgoing_commands = []
for monitor in list_of_callers:
    command_per_user = [
        f'dial-peer voice {monitor} Voip',
        f'destination-pattern {monitor}..',
        f'session target ipv4:10.{monitor}.100.8',
        f'codec g711ULAW',
        'exit'
    ]
    outgoing_commands.append(command_per_user)

ivrs_commands = [
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
    'exit'
]

ospf_commands = [
    # dynamic routing
    'router ospf 1',
    f'router-id 10.{user_m}.100.8',
    f'network 10.{user_m}.100.0 0.0.0.255 area 0',
    'exit'
]


# CONNECT - to the device
# Establish connection and access cli
accessCLI = ConnectHandler(**device_info)

# PUSH - commands to the device
order_of_config = [
    'Console Access',
    'Analog Phones',
    'Telephony',
    'Video Calls',
    'Incoming Calls',
    'Outgoing Calls',
    'IVRS',
    'OSPF Routing'
]

# counter for how many times telephony has been configured
push_telephony = 0

for config in order_of_config:
    # inform user what is currently being configured
    print('~'*15 + f'\nConfiguring {config}...')
    
    if config == 'Console Access':
        output = accessCLI.send_config_set(cons_commands)
    elif config == 'Analog Phones':
        output = accessCLI.send_config_set(analog_commands)
    elif config == 'Telephony':
        
        # push telephony config 2 times
        while push_telephony < 2:
            output = accessCLI.send_config_set(ephone_commands)
            push_telephony += 1
            print(' '*4 + f'{config} configuration {push_telephony}/2')
            
    elif config == 'Video Calls':
        output = accessCLI.send_config_set(vidcall_commands)
    elif config == 'Incoming Calls':
        output = accessCLI.send_config_set(incoming_commands)
    elif config == 'Outgoing Calls':
        
        # push commands per command block
        for command in outgoing_commands:
            output = accessCLI.send_config_set(command)
            
    elif config == 'IVRS':
        output = accessCLI.send_config_set(ivrs_commands)
    else:
        output = accessCLI.send_config_set(ospf_commands)
    
    # print cli output on the terminal
    print(output)
        
    print('Configuration Successful!!!\n')