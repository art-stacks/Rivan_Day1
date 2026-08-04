import yaml
import netmiko
from netmiko import ConnectHandler

# Prompt user for info
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
# Read the json file
with open('cucm-configs.json') as file:
    # convert json data to usable python data
    json_configs = yaml.safe_load(file)

# Update the key[ip] for connection
json_configs['device_info']['ip'] = f'10.{user_m}.100.8'

# Parse data
# ConnectHandler arguments to establish SSH connection to device
device_info = json_configs['device_info']

# Values for commands
ips = json_configs['ips']
peer_1 = json_configs['analog']['peer_1']
peer_2 = json_configs['analog']['peer_2']
peer_3 = json_configs['analog']['peer_3']
peer_4 = json_configs['analog']['peer_4']
tele = json_configs['telephony']
dn_1 = tele['dn_1']
dn_2 = tele['dn_2']
dn_3 = tele['dn_3']
dn_4 = tele['dn_4']
dn_5 = tele['dn_5']
dn_6 = tele['dn_6']
dn_7 = tele['dn_7']
dn_8 = tele['dn_8']
ivrs = json_configs['ivrs']
ospf = json_configs['ospf']
all_callers = json_configs['active_monitors']

# Commands to be sent to the device.
cons_commands = [
    # Console access
    'line cons 0',
    f'password {ips["password"]}',
    'login',
    f'exec-timeout {ips["no_timeout"]}',
    'exit'
]

analog_commands = [
    # Configure analog phones
    f'dial-peer voice {peer_1["voice"]} pots',
    f'destination-pattern {user_m}{peer_1["des_pat"]}',
    f'port {peer_1["port"]}',
    'exit',
    f'dial-peer voice {peer_2["voice"]} pots',
    f'destination-pattern {user_m}{peer_2["des_pat"]}',
    f'port {peer_2["port"]}',
    'exit',
    f'dial-peer voice {peer_3["voice"]} pots',
    f'destination-pattern {user_m}{peer_3["des_pat"]}',
    f'port {peer_3["port"]}',
    'exit',
    f'dial-peer voice {peer_4["voice"]} pots',
    f'destination-pattern {user_m}{peer_4["des_pat"]}',
    f'port {peer_4["port"]}',
    'exit'
]

ephone_commands = [
    # Configure telephony
    'no telephony-service',
    'telephony-service',
    'no auto assign',
    'no auto-reg-ephone',
    'max-ephones 5',
    'max-dn 20',
    f'ip source-address 10.{user_m}.{tele["tftp_ip"]} port {tele["voice_port"]}',
    'create cnf-files',
    f'ephone-dn {dn_1["temp"]}',
    f'number {user_m}{dn_1["dn"]}',
    f'ephone-dn {dn_2["temp"]}',
    f'number {user_m}{dn_2["dn"]}',
    f'ephone-dn {dn_3["temp"]}',
    f'number {user_m}{dn_3["dn"]}',
    f'ephone-dn {dn_4["temp"]}',
    f'number {user_m}{dn_4["dn"]}',
    f'ephone-dn {dn_5["temp"]}',
    f'number {user_m}{dn_5["dn"]}',
    f'ephone-dn {dn_6["temp"]}',
    f'number {user_m}{dn_6["dn"]}',
    f'ephone-dn {dn_7["temp"]}',
    f'number {user_m}{dn_7["dn"]}',
    f'ephone-dn {dn_8["temp"]}',
    f'number {user_m}{dn_8["dn"]}',
    'ephone 1',
    f'mac-address {ephone_1_mac}',
    f'type {tele["ephone_type"]}',
    f'button {tele["btn_layout"]["ephone_1"]}',
    'restart',
    'ephone 2',
    f'mac-address {ephone_2_mac}',
    f'type {tele["ephone_type"]}',
    f'button {tele["btn_layout"]["ephone_2"]}',
    'restart',
    'exit'
]

vidcall_commands = [
    # Enable video calls
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
    # Allow incoming calls
    'voice service voip',
    'ip address trusted list',
    'ipv4 0.0.0.0 0.0.0.0',
    'exit'
]

# Allow outgoing calls
list_of_callers = all_callers.split(',')
outgoing_commands = []
for monitor in list_of_callers:
    command_per_user = [
        f'dial-peer voice {monitor} Voip',
        f'destination-pattern {monitor}..',
        f'session target ipv4:10.{monitor}.{tele["tftp_ip"]}',
        f'codec g711ULAW',
        'exit'
    ]
    outgoing_commands.append(command_per_user)

ivrs_commands = [
    # Configure ivrs
    f'dial-peer voice {ivrs["des_pat"]} voip',
    'service rivanaa out-bound',
    f'destination-pattern {user_m}{ivrs["des_pat"]}',
    f'session target ipv4:10.{user_m}.{tele["tftp_ip"]}',
    f'incoming called-number {user_m}{ivrs["des_pat"]}',
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
    f'param aa-hunt1 {user_m}{ivrs["hunt_1"]}',
    f'param aa-hunt2 {user_m}{ivrs["hunt_2"]}',
    f'param aa-hunt3 {user_m}{ivrs["hunt_3"]}',
    f'param aa-hunt4 {user_m}{ivrs["hunt_4"]}',
    'param queue-manager-debugs 1',
    'param number-of-hunt-grps 4',
    'exit'
]

ospf_commands = [
    # Dynamic routing
    f'router ospf {ospf["process"]}',
    f'router-id 10.{user_m}.{tele["tftp_ip"]}',
    f'network 10.{user_m}.100.0 {ips["wild_24"]} {ospf["area"]}',
    'exit'
]


# CONNECT - to the device.
# Establish connection and access cli.
accessCLI = ConnectHandler(**device_info)


# PUSH - commands to the device.
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

# Counter for how many times telephony has been configured
push_telephony = 0

for config in order_of_config:
    # Inform user what is currently being configured
    print('~'*15 + f'\nConfiguring {config}...')
    
    if config == 'Console Access':
        output = accessCLI.send_config_set(cons_commands)
    elif config == 'Analog Phones':
        output = accessCLI.send_config_set(analog_commands)
    elif config == 'Telephony':
        
        # Push telephony config 2 times
        while push_telephony < 2:
            output = accessCLI.send_config_set(ephone_commands)
            push_telephony += 1
            print(' '*4 + f'{config} configuration {push_telephony}/2')
            
    elif config == 'Video Calls':
        output =accessCLI.send_config_set(vidcall_commands)
    elif config == 'Incoming Calls':
        output =accessCLI.send_config_set(incoming_commands)
    elif config == 'Outgoing Calls':
        
        # Push commands per command block
        for command in outgoing_commands:
            output = accessCLI.send_config_set(command)
            
    elif config == 'IVRS':
        output = accessCLI.send_config_set(ivrs_commands)
    else:
        output = accessCLI.send_config_set(ospf_commands)
    
    # Print the cli to the terminal.
    print(output)
    
    print('Configuration Successful!!!\n')