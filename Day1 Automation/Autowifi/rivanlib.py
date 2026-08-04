
# Configurations for Cisco Commands
class Cisco:
	def __init__(self, data):
		self.data = data


	def gen_config(self):
		full_command = []

		if 'vlan' in self.data:
			command = self.vlan()
			full_command = [*full_command, *command]
			
		if 'interface' in self.data:
			command = self.ipv4_int()
			full_command = [*full_command, *command]

		if 'dhcpv4' in self.data:
			command = self.ipv4_dhcp()
			full_command = [*full_command, *command]
		
		return full_command


	def vlan(self):
		'''
		This method is used to configure VLANs NOT SVIs

		Scheme (JSON):
		{
			"vlan":
			[
				{
					"id": "20",
					"name": "MANAGEMENT VLAN"
				}
			]
		}
		'''
		
		full_command = []

		# Iterate through all given vlan values
		for vlan in self.data['vlan']:

			# Configure VLAN with Name assignment
			command = [
				f'vlan {vlan["id"]}',
				f'name {vlan["name"]}'
			]

			full_command = [*full_command, *command]
		
		return full_command


	def ipv4_int(self):
		'''
        This method is used to configure IPv4 addresses on L3 interfaces 
        such as Routing Ports, SVIs, and Loopback Interfaces.
        
        Scheme (JSON):
        
		{
			"interface": 
			[
				{
					"name": "GigabitEthernet1",
					"enabled": true,
					"description": "Configured via Python",
					"type": {
						"swport": {
							"data-vlan": "20",
							"voice-vlan": "100"
						},

						"rtport": {
							"ietf-ip:ipv4": {
								"address": 
								[
									{
										"ip": "208.8.8.11",
										"netmask": "255.255.255.0"
									},

									{
										"ip": "208.8.8.12",
										"netmask": "255.255.255.0"
									}
								]
							}
						}
					}
				}
			]
		}
		'''
        
		full_command = []

		# Iterate through all given interface values
		for interface in self.data['interface']:
            
			try:
				# Configure Interface Name & Description
				command = [
					f'interface {interface["name"]}',
					f'description {interface["description"]}'
				]

				# Determine if interface is shutdown
				if interface['enabled'] == True:
					command = [*command, 'no shut']
				else:
					command = [*command, 'shut']

				# Determine if the interface is a switchport or routingport
				if 'swport' in interface['type'] and 'rtport' in interface['type']:
					print('[!] Error: An interface cannot both be a switchport and routing port. Specify only a single Type: \'swport\' or \'rtport\' ')
				

				elif 'swport' in interface['type']:
					swport = interface['type']['swport']
					command = [
						*command,
						f'switchport mode access',
						f'switchport access vlan {swport["data-vlan"]}'
					]

					if 'voice-vlan' in swport:
						command = [
							*command,
							f'switchport voice vlan {swport["voice-vlan"]}'
						]
				

				elif 'rtport' in interface['type']:
					rtport = interface['type']['rtport']

					# Turn a switchport to a routing port
					command = [
						*command,
						'no switchport' 
					]

					# Evaluate if there are more than one IP address specified
					ipv4_address = rtport['ietf-ip:ipv4']['address']
					for ipadd in ipv4_address:
						index = ipv4_address.index(ipadd)
						if index > 0:
							line = [
								f'ip address {ipadd["ip"]} {ipadd["netmask"]} secondary'
							]
						else:
							line = [
								f'ip address {ipadd["ip"]} {ipadd["netmask"]}'
							]

						command = [*command, *line]

				full_command = [*full_command, *command]
			
			except Exception as err:
				print(err)
				continue
		
		return full_command


	def ipv4_dhcp(self):
		'''
		This method is used to configure a DHCPv4 Pool.
        
        Scheme (JSON):

		{
			"dhcpv4": [
				{
					"name": "MGMTPOOL",
					"network": {
						"ip": "192.168.103.0",
						"netmask": "255.255.255.0"
					},
					"gateway": "192.168.103.11",
					"dns": "192.168.103.11",
					"domain": "MGMT.COM"
				}
			]
		}
		'''

		full_command = []

		# Iterate through all given dhcp values
		for dhcp in self.data['dhcpv4']:
			command = [
				f'ip dhcp pool {dhcp["name"]}',
				f'network {dhcp["network"]["ip"]} {dhcp["network"]["netmask"]}',
				f'default-router {dhcp["gateway"]}',
				f'dns-server {dhcp["dns"]}',
				f'domain-name {dhcp["domain"]}'
			]

			full_command = [*full_command, *command]
		
		return full_command


	def ap_wifi(self):
		'''
		This method is used to configure cisco access point.

		Scheme (JSON):

		{
			"aironet": {
				"hostname": "aironet-m",
				"ssid": "m-welcomeToRivan",
				"auth-type": "open",
				"key-man": "wpa",
				"wifi-pass": "C1sc0123",
				"channel": "9",
				"encr-mod": "tkip",
				"vlan": "m"
			}
		} 
		'''

		aironet = self.data['aironet']

		full_command = [
			f'hostname {aironet["hostname"]}',
			f'dot11 ssid {aironet["ssid"]}',
			f'vlan {aironet["vlan"]}',
			f'authentication {aironet["auth-type"]}',
			f'authentication key-management {aironet["key-man"]}',
			f'wpa-psk ascii {aironet["wifi-pass"]}',
			'guest-mode',
			'default Int Dot11Radio 0',
			'default interface gigabitEthernet 0',
			'int dot11radio 0',
			'no shut',
			f'channel {aironet["channel"]}',
			f'encryption mode ciphers {aironet["encr-mod"]}',
			f'encryption vlan {aironet["vlan"]} mode ciphers {aironet["encr-mod"]}',
			f'ssid {aironet["ssid"]}',
			'exit',
			f'interface dot11radio 0.{aironet["vlan"]}',
			f'encapsulation dot1q {aironet["vlan"]} native',
			'bridge-group 1',
			'exit'
		]

		return full_command
