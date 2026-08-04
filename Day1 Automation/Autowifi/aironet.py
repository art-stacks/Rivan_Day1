from netmiko import ConnectHandler
import rivanlib
import json

device_info = {
    'device_type': 'cisco_ios_telnet',
    'host': '10.69.10.3',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass'
}

with open('ap.json', 'r') as file:
    command = json.load(file)


if __name__ == '__main__':
    command = rivanlib.Cisco(command).ap_wifi()

    access_cli = ConnectHandler(**device_info)
    access_cli.enable()
    output = access_cli.send_config_set(command)

    access_cli.disconnect()
    print(output)
