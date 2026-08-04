# 
# Your Monitor Number
m = '#$34T#'
#
# How to configure devices via python
# Using various SSH Libraries (Paramiko, Netmiko, Nornir, etc)
#
# Verify Path - Environment Variables
#
# Install/Update libraries
# 
# @cmd
# py -m pip install --upgrade pip
# py -m pip install netmiko
# py -m pip install paramiko
#
#
#
# ---------------------------------------------------------- #
# DATA TYPES - (Line 20 - 68)
#
# Dictionary
py_dictionary = {
    'key_string': 'value_string',
    'key_int': 1,
    'key_float': 1.0,
    'key_boolean': True,
    'key_list': [True, 2, 3.0, '5'],
    'key_dictionary': {
        'nested' : [
            'I\'m',
            'nested',
            'data'
        ]
    }
}

# String
# py_dictionary['key_string']

# Integer
# py_dictionary['key_int']

# Float
# py_dictionary['key_float']

# Boolean
# py_dictionary['key_boolean']

# List
# py_dictionary['key_list']

# Nested Data
# py_dictionary['key_dictionary']['nested'][1]


## EXERCISE 01 - ex01.py
# 1. From py_dictionary, print the float value 1.0 from key_float.
# print(py_dictionary[__])

# 2. From py_dictionary, store the string value '5', from key_list, in a variable called, sample. Then, print the value of sample.
# sample = py_dictionary[__][__]
# print(__)

# 3. From py_dictionary, print the string 'data' from key_dictionary.
# 


# ---------------------------------------------------------- #
# NETMIKO (TELNET) - (Line 70 - 116)
# import netmiko
from netmiko import ConnectHandler

# Provide information about the host/s
cbaba = {
    'device_type': 'cisco_ios_telnet',
    'host': f'10.{m}.1.4',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23
}


# Write the configurations
cb_config = [
    'interface loopback 1',
    f'ip add 10.{m}.1.1 255.255.255.255',
    'end'
]


# Connect to the host/s
accesscli = ConnectHandler(**cbaba)


# Enable secret - Only IF Telnet Session
# accesscli.enable()


# Send show command/s
# show_ip = accesscli.send_command('show ip interface brief')
# show_vlan = accesscli.send_command('show vlan brief')
# show_mac = accesscli.send_command('show mac address-table')
# show_cdp = accesscli.send_command('show cdp neighbor')


# Push configurations
cli_output = accesscli.send_config_set(cb_config)

# Close connection
accesscli.disconnect()

print(cli_output)


# ---------------------------------------------------------- #
# PARAMIKO - (Line 118 - 174)
import paramiko
import time

# Prompt user
monitor = input('What is your monitor number? ')

# Device credentials and IP
ip = f'10.{monitor}.1.2'
username = 'admin'
password = 'pass'
secret = 'pass'

def configureCisco(ip, username, password, secret=None):
    try:
        print(f"Connecting to {ip}...")
        
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)

        remote_conn = client.invoke_shell()
        time.sleep(1)
        remote_conn.recv(1000)  # Clear banner

        def send_command(command, wait=1):
            remote_conn.send(command + '\n')
            time.sleep(wait)
            output = remote_conn.recv(5000).decode('utf-8')
            return output

        # Enter enable mode
        output = send_command('enable')
        if secret:
            output = send_command(secret)

        # Enter configuration mode
        send_command('configure terminal')

        # Configure Loopback0
        send_command('interface Loopback0')
        send_command('ip address 1.1.1.1 255.255.255.0')
        send_command('no shutdown')

        # Exit
        send_command('end')

        print("Configuration complete.")
        client.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    configureCisco(ip, username, password, secret)

