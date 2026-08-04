import time
import multiprocessing
from netmiko import ConnectHandler

def configureDeviceTelnet(device, 
                          device_info, 
                          commands, 
                          sh_cli_output=False):
    '''
    This function will handle TELNET connection and configuration
    to a specified device.
    '''
    
    # Provide device information to python to authenticate
    # then connect to the specified device
    accessCli = ConnectHandler(**device_info)
    
    # Push enable command to the cli to enter privilege exec mode: Router> -> Router#
    accessCli.enable()
    
    # Enter global configuration mode: Router# -> Router(config)
    # then send specified commands
    output = accessCli.send_config_set(commands)
    
    accessCli.disconnect()
    
    # Print cli output on the terminal
    if sh_cli_output:
        print('`'*32)
        print(f'Configuring {device}...')
        print(f'\n{output}\n')

def configureDeviceSSH(device, 
                       device_info,
                       commands, 
                       sh_cli_output=False):
    '''
    This function will handle SSH connection and configuration
    to a specified device.
    '''
    
    # Change connection for SSH
    device_info['device_type'] = 'cisco_ios'
    
    # Provide device information to python to authenticate
    # then connect to the specified device
    accessCli = ConnectHandler(**device_info)
    
    # Enter global configuration mode: Router# -> Router(config)
    # then send specified commands
    output = accessCli.send_config_set(commands)
    
    accessCli.disconnect()
    
    # Print cli output on the terminal
    if sh_cli_output:
        print('`'*32)
        print(f'Configuring {device}...')
        print(f'\n{output}\n')
    
def main(device, 
         device_info, 
         commands, 
         connection= 'telnet', 
         sh_cli=False):
    
    if connection == 'telnet':
        configureDeviceTelnet(device, device_info, commands, sh_cli)
    elif connection == 'ssh':
        configureDeviceSSH(device, device_info, commands, sh_cli)

if __name__ == '__main__':
    # Import device configurations
    import config_vars
    
    telnet = 'telnet'
    ssh = 'ssh'
    
    coretaas_info = {
        'device_type': 'cisco_ios_telnet',
        'ip': f'10.{config_vars.user_m}.1.2',
        'username': 'admin',
        'password': 'pass',
        'secret': 'pass'
    }

    corebaba_info = {
        'device_type': 'cisco_ios_telnet',
        'ip': f'10.{config_vars.user_m}.1.4',
        'username': 'admin',
        'password': 'pass',
        'secret': 'pass'
    }

    cucm_info = {
        'device_type': 'cisco_ios_telnet',
        'ip': f'10.{config_vars.user_m}.100.8',
        'username': 'admin',
        'password': 'pass',
        'secret': 'pass'
    }

    edge_info = {
        'device_type': 'cisco_ios_telnet',
        'ip': f'10.{config_vars.user_m}.{config_vars.user_m}.1',
        'username': 'admin',
        'password': 'pass',
        'secret': 'pass'
    }

    order_of_config = ['coretaas', 'corebaba', 'cucm', 'edge']
    process_list = []

    # Record the time it takes to run the script
    start = time.perf_counter()
    
    # Use multiprocessing to configure multiple devices at the same time
    for device in order_of_config:
        if device == 'coretaas':
            # Assign a cpu core to a function. This will NOT run the function.
            proc = multiprocessing.Process(target=main, args=[device, 
                                                              coretaas_info, 
                                                              config_vars.coretaas_config, 
                                                              telnet, 
                                                              True])
        elif device == 'corebaba':
            proc = multiprocessing.Process(target=main, args=[device, 
                                                              corebaba_info, 
                                                              config_vars.corebaba_config, 
                                                              telnet, 
                                                              True])
        elif device == 'cucm':
            proc = multiprocessing.Process(target=main, args=[device, 
                                                              cucm_info, 
                                                              config_vars.cucm_config, 
                                                              telnet, 
                                                              True])
        elif device == 'edge':
            proc = multiprocessing.Process(target=main, args=[device, 
                                                              edge_info, 
                                                              config_vars.edge_config, 
                                                              telnet, 
                                                              True])
        
        # list each process to easily run them using a for loop
        process_list.append(proc)
    
    # run the function for each process
    for i in process_list:
        i.start()
    
    # wait for all the process to finish before moving on to the next line 
    for i in process_list:
        i.join()
    
    # provide a 5 second delay for cucm to finish initializing telephony
    wait_for_telephony_init = time.sleep(5)
    main('cucm', 
         cucm_info, 
         config_vars.register_ephones, 
         'telnet', 
         True)
    
    finish = time.perf_counter()
    print(f'\nFinished in {round(finish - start, 2)} second(s)!')
    input('(Press ENTER to END)')