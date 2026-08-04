from netmiko import ConnectHandler

user_m = input('What is your monitor number? ')

taas_info = {
    'device_type': 'cisco_ios_telnet',
    'host': f'10.{user_m}.1.2',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass'
}

baba_info = {
    'device_type': 'cisco_ios_telnet',
    'host': f'10.{user_m}.1.4',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass'
}

cucm_info = {
    'device_type': 'cisco_ios_telnet',
    'host': f'10.{user_m}.100.8',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass'
}

edge_info = {
    'device_type': 'cisco_ios_telnet',
    'host': f'10.{user_m}.{user_m}.1',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass'
}

# connect to the specified device    
#   **kwargs - intelligently maps each key in a dictionary(Python's key-value pair object) as its own argument.
#   if **kwargs is not applied it will treat the entire dictionary as the first argument only.
accessCLI = ConnectHandler(**baba_info)

# send_command will send a single line of command to the current state of the cli. 
# Mostly used for show commands
showIP = accessCLI.send_command('sh ip int br')
print(showIP)

# disconnect from device
accessCLI.disconnect()