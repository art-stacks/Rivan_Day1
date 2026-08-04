
<!-- Your monitor number = #$34T# -->

## SETUP
Setup:  
  - RSTHayup: NetAuto Lab
  - NetOps-PH
  - CSR1000v

<br>

### RSTHayup: NetAuto
1. Turn on all devices, then run the python script from "Ex 03 - NetAuto"

<br>

2. Access NetAuto devices via SecureCRT

<br>

3. Set Static route on the real PC into the Lab Environment
~~~
!@cmd
route add 10.255.12.0 mask 255.255.252.0 [C1's e0/0 IP]
~~~

<br>
<br>

### Run Servers and Edge Routers
NetOps:
  Name: NetOps-PH
  
  | NetAdapter   |                    |
  | ---          | ---                |
  | NetAdapter   | VMNet1             |
  | NetAdapter 2 | VMNet2             |
  | NetAdapter 3 | VMNet3             |
  | NetAdapter 4 | Bridge (Replicate) |

<br>

CSR1000v:
  Name: UTM-PH
  
  | NetAdapter   |        |
  | ---          | ---    |
  | NetAdapter   | NAT    |
  | NetAdapter 2 | VMNet2 |
  | NetAdapter 3 | VMNet3 |

&nbsp;
---
&nbsp;

### Set IP address and Routing
~~~
!@UTM-PH
conf t
 hostname UTM-PH
 enable secret pass
 service password-encryption
 no logging cons
 no ip domain lookup
 line vty 0 14
  transport input all
  password pass
  login local
  exec-timeout 0 0
 int g1
  ip add 208.8.8.11 255.255.255.0
  no shut
 int g2
  ip add 192.168.102.11 255.255.255.0
  no shut
 int g3
  ip add 11.11.11.113 255.255.255.224
  no shut
 !
 username admin privilege 15 secret pass
 ip http server
 ip http secure-server
 ip http authentication local
 ip route 0.0.0.0 0.0.0.0 208.8.8.2
 end
wr
!
~~~


<br>

__NetOps-PH Setup__
> Login: root
> Pass: C1sc0123

<br>

1. Get the MAC Address for the Bridge connection
VMWare > NetOps-PH Settings > NetAdapter (2, 3, & 4) > Advance > MAC Address

| NetAdapter   | MAC Address      | VM Interface | ENS     |
| ---          | ---              | ---          | ---     |
| NetAdapter 2 | ___.___.___.___  | ens___       |  ens192 |
| NetAdapter 3 | ___.___.___.___  | ens___       |  ens224 |
| NetAdapter 4 | ___.___.___.___  | ens___       |  ens256 |

<br>

2. Get Network-VM Mapping
~~~
!@NetOps-PH
ip -br link
~~~

<br>

3. Modify Interface IP
VMNet2:  192.168.102.6/24
VMNet3:  11.11.11.100/27
Bridged: 10.#$34T#.1.6/24

<br>

~~~
!@NetOps-PH
ifconfig ens192 192.168.102.6 netmask 255.255.255.0 up
ifconfig ens224 11.11.11.100 netmask 255.255.255.224 up
ifconfig ens256 10.#$34T#.1.6 netmask 255.255.255.0 up
~~~

<br>

Verify:
~~~
!@NetOps-PH
ip -4 addr

nmcli connection show
netstat -rn
~~~

<br>

or  

<br>

__Using Network Management CLI for persistent IP.__

<br>

VMNet2:
~~~
!@NetOps-PH
nmcli connection add \
type ethernet \
con-name VMNET2 \
ifname ens192 \
ipv4.method manual \
ipv4.addresses 192.168.102.6/24 \
autoconnect yes

nmcli connection up VMNET2

nmcli connection add \
type ethernet \
con-name VMNET3 \
ifname ens224 \
ipv4.method manual \
ipv4.addresses 11.11.11.100/27 \
autoconnect yes

nmcli connection up VMNET3

nmcli connection add \
type ethernet \
con-name BRIDGED \
ifname ens256 \
ipv4.method manual \
ipv4.addresses 10.#$34T#.1.6/24 \
autoconnect yes

nmcli connection up BRIDGED

ip route add 10.0.0.0/8 via 10.#$34T#.1.4 dev ens256
ip route add 200.0.0.0/24 via 10.#$34T#.1.4 dev ens256
ip route add 0.0.0.0/0 via 11.11.11.113 dev ens224
~~~

&nbsp;
---
&nbsp;

### Remote Access
Connect to Management Interfaces of Devices
NetOps-PH: 192.168.102.6
UTM-PH: 192.168.102.11

&nbsp;
---
&nbsp;

### Step 7 - Exchange SSH Keys
Delete existing SSH Keys
~~~
!@NetOps
rm -rf /root/.ssh/known_hosts
~~~

<br>

SSH to the ff devices:
~~~
!@NetOps
ssh admin@10.#$34T#.1.2
~~~

<br>

| IP                 | Device   |
| ---                | ---      |
| 10.#$34T#.1.2      | CoreTaas |
| 10.#$34T#.1.4      | CoreBaba |
| 10.#$34T#.100.8    | CUCM     |
| 10.#$34T#.#$34T#.1 | EDGE     |

<br>

- Accept the keys
- End the SSH session


<br>
<br>

---
&nbsp;


## Bash
### Shell Scripts
1. Output a basic Hello
~~~
!@UTM-PH - bash shell
nano hello.sh

///Edit hello.sh
echo "hello world"
///

chmod 500 hello.sh
./hello.sh
~~~

<br>

2. Create Multi users
~~~
!@UTM-PH - bash shell
nano add_user.sh

///add_user.sh
adduser m_user1
echo "m_user1:C1sc0123" | chpasswd

adduser m_user2
echo "m_user2:C1sc0123" | chpasswd

adduser m_user3
echo "m_user3:C1sc0123" | chpasswd
///

chmod 500 add_user.sh
./add_user.sh
~~~

<br>

### Create a shell script to ping multiple sites and get their IP.
~~~
!@UTM-PH - bash shell
cd /home/guestshell; nano icmp.sh
~~~

<br>

icmp.sh Script
~~~
#!/bin/bash

# Prompt User
read -p "What hosts to ping? (Space-separated) " -a hosts

for ip in "${hosts[@]}"
do
  (
    if [[ "$1" == "-4" || -z "$1" ]]; then
        result=$(ping -4 -c 1 "$ip" 2>/dev/null)
    elif [[ "$1" == "-6" ]]; then
        result=$(ping -6 -c 1 "$ip" 2>/dev/null)
    fi

    # Extract full IPv4 or IPv6 address
    host_ip=$(echo "$result" | sed -n 's/^PING[^(]*(\([^)]*\)).*/\1/p')


    if echo "$result" | grep -q "time="; then
        echo "$ip ($host_ip) replied"
    else
        echo "$ip ($host_ip) failed"
    fi
  ) &
done

wait

echo "All pings complete!"
~~~

<br>

Make icmp.sh executable
~~~
!@UTM-PH - bash shell
chmod +x icmp.sh
~~~

<br>

Run the Bash Script
~~~
!@UTM-PH - bash shell
./icmp.sh
~~~


<br>
<br>

---
&nbsp;


## Python & JSON
~~~
!@powershell
py -m pip install --upgrade pip
py -m pip install netmiko
py -m pip install paramiko
~~~


<br>


### Manual Method
~~~
!@UTM-PH
conf t
 int loopback 1
  ip add 1.1.1.1 255.255.255.255
  description configured-manually
 int loopback 2
  ip add 2.2.2.2 255.255.255.255
  description configured-manually
  end
~~~


<br>


### Data Types (JSON)
cbaba.json
~~~
{
    "monitor_number": "#$34T#",
    
    "device_config": {
        "hostname": "CoreBaba-#$34T#",
        "address": {
            "vlan_70": {
                "ipv4": "10.#$34T#.70.4",
                "desc": "BLUETEAM"
            },
            "vlan_71": {
                "ipv4": "10.#$34T#.71.4",
                "desc": "REDTEAM"
            },
            "vlan_72": {
                "ipv4": "10.#$34T#.72.4",
                "desc": "AUDIT"
            }
        },
        "logging_console": false
    }
}
~~~


<br>
<br>


cbaba.py
~~~
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
~~~


<br>
<br>


## NETCONF (-P 830)
*Format XML via "XML Tools" by Josh Johnson*

<br>

__RPC (Remote Procedural Calls) over SSH__

<br>

### STEP 1 - Enable NETCONF
~~~
!@Cisco
conf t
 netconf-yang
 end
~~~


&nbsp;
---
&nbsp;


### STEP 2 -  Establish the session (HELLO)
~~~
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <capabilities>
    <capability>urn:ietf:params:netconf:base:1.0</capability>
    <capability>http://cisco.com/ns/yang/Cisco-IOS-XE-native</capability>
  </capabilities>
</hello>
]]>]]>
~~~


<br>

__NETCONF Operations__
  <get>           > retrieve configuration/state  
  <get-config>    > retrieve a datastore  
  <edit-config>   > push configuration  
  <delete-config> > delete configuration  
  <copy-config>   > copy datastore  


<br>


### GET : Get the Running-Config
~~~
<rpc message-id="1" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"/>
    </filter>
  </get>
</rpc>
]]>]]>
~~~


<br>


### GET : Get Interface Config
~~~
<rpc message-id="1" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <filter type="subtree">
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface/>
      </native>
    </filter>
  </get>
</rpc>
]]>]]>
~~~


<br>


### GET-CONFIG : Get Configurations from Datastore
~~~
<rpc message-id="1" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get-config>
    <source>
      <running/>
    </source>
    <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface/>
      </native>
    </filter>
  </get-config>
</rpc>
]]>]]>
~~~


<br>


### EDIT-CONFIG : Create Loopbacks
~~~
<rpc message-id="1" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <edit-config>
    <target>
      <running/>
    </target>
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <Loopback>
            <name>5</name>
            <description>Configured via raw NETCONF SSH</description>
            <ip>
              <address>
                <primary>
                  <address>5.5.5.5</address>
                  <mask>255.255.255.255</mask>
                </primary>
              </address>
            </ip>
          </Loopback>
        </interface>
      </native>
    </config>
  </edit-config>
</rpc>
]]>]]>
~~~


<br>


### DELETE-CONFIG : Delete Loopback 
~~~
<rpc message-id="200" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <edit-config>
    <target>
      <running/>
    </target>
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <Loopback operation="delete">
            <name>5</name>
          </Loopback>
        </interface>
      </native>
    </config>
  </edit-config>
</rpc>
]]>]]>
~~~


<br>


### COPY-CONFIG (Only for supported IOS) : Copy Running Configurations
~~~
<rpc message-id="105" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <copy-config>
    <target>
      <startup/>
    </target>
    <source>
      <running/>
    </source>
  </copy-config>
</rpc>
]]>]]>
~~~


&nbsp;
---
&nbsp;


## YANG DATA MODELING LANGUAGE
### Map YANG to XML
IETF RFC 8530: https://datatracker.ietf.org/doc/html/rfc8530  
Cisco YANG Data: https://developer.cisco.com/docs/nso-guides-6.3/the-yang-data-modeling-language/#yang-introduction  

<br>

~~~
container interface {
    list Loopback {
        key "name";
        leaf name { type string; }
        leaf description { type string; }
        container ip {
            container address {
                leaf primary { type inet:ipv4-address; }
            }
        }
    }
}
~~~


<br>


~~~
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
    <Loopback>
      <name>1</name>
      <description>Configured via raw NETCONF SSH</description>
      <ip>
        <address>
          <primary>
            <address>5.5.5.5</address>
            <mask>255.255.255.255</mask>
          </primary>
        </address>
      </ip>
    </Loopback>
  </interface>
</native>
~~~


<br>


~~~
container system {
    container login {
        leaf message {
            type string;
            description
                "Message given at start of login session";
        }
    }
}
~~~


<br>


~~~
<system>
  <login>
    <message>Good morning, Dave</message>
  </login>
</system>
~~~


&nbsp;
---
&nbsp;


### XML YANG Data via Python
~~~
!@powershell
py -m pip install ncclient
py -m pip install lxml
~~~


<br>


~~~
from ncclient import manager
from ncclient import xml_

import xml.dom.minidom
from lxml import etree

# Device info
ios_xe_host = "192.168.102.11"
ios_xe_port = 830
ios_xe_username = "admin"
ios_xe_password = "pass"

# Connect to device
m = manager.connect(
    host=ios_xe_host,
    port=ios_xe_port,
    username=ios_xe_username,
    password=ios_xe_password,
    hostkey_verify=False,
    look_for_keys=False,
    device_params={"name": "iosxe"}
)

# Build the NETCONF payload as XML ElementTree
netconf_interface_template = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>1</name>
        <description>Configured via NETCONF</description>
        <ip>
          <address>
            <primary>
              <address>7.7.7.7</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

# Convert string to ElementTree element
netconf_element = xml_.to_ele(netconf_interface_template)

# Push configuration
netconf_reply = m.edit_config(target="running", config=netconf_element)

# Pretty print reply
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Close session
m.close_session()
~~~


<br>
<br>

---
&nbsp;


## RESTCONF
*Net Config over HTTPS*

~~~
!@Cisco
conf t
 username admin priv 15 secret pass
 ip http server
 ip http secure-server
 restconf
 end
~~~


<br>


### From Cisco Configuration File (CLI) to JSON
~~~
!@Telnet -p 80
GET /index.html

GET / HTTP/1.1
Host: 192.168.102.11
~~~


<br>


~~~
!@cmd
curl.exe -k -u admin:pass -H "Accept: application/yang-data+xml" https://192.168.102.11/restconf/data/ietf-interfaces:interfaces
curl.exe -k -u admin:pass -H "Accept: application/yang-data+json" https://192.168.102.11/restconf/data/ietf-interfaces:interfaces


curl.exe -k -u admin:pass -H "Accept: application/yang-data+json" https://192.168.102.11/restconf/data/ietf-yang-library:modules-state -o modules.json
~~~


<br>

__ietf-interfaces__
~~~
!@cmd
curl.exe -k -u admin:pass -H "Accept: application/yang-data+json" https://192.168.102.11:443/restconf/tailf/modules/ietf-interfaces/2014-05-08 -o int.yang
~~~


<br>
<br>


### CRUD     What to do with data
- Create     Add new data
- Read       Retrieve existing data
- Update     Modify existing data
- Delete     Remove data


<br>


### HTTP Protocol Operations / Methods
- Get        Retrieve a resource
- Post       Submit new data / create
- Put        Replace an existing resource
- Patch      Partially modify a resource
- Delete     Delete a resource


<br>


### POST
__loopback.json__
~~~
{
  "ietf-interfaces:interface": {
    "name": "Loopback9",
    "description": "Configured via RESTCONF",
    "type": "iana-if-type:softwareLoopback",
    "enabled": true,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "9.9.9.9",
          "netmask": "255.255.255.255"
        }
      ]
    }
  }
}
~~~


<br>


~~~
!@cmd
curl.exe -k -u admin:pass -X POST `
  -H "Content-Type: application/yang-data+json" `
  -d "@loopback.json" `
  https://192.168.102.11/restconf/data/ietf-interfaces:interfaces
~~~


<br>


### HTTP POST DATA
~~~
POST /restconf/data/ietf-interfaces:interfaces HTTP/1.1
Host: 192.168.102.11
Authorization: Basic YWRtaW46cGFzcw==
Content-Type: application/yang-data+json
Accept: application/yang-data+json
Content-Length: 187

{
  "ietf-interfaces:interface": {
    "name": "Loopback9",
    "description": "Configured via RESTCONF",
    "type": "iana-if-type:softwareLoopback",
    "enabled": true,
    "ipv4": {
      "address": [
        {"ip": "9.9.9.9", "netmask": "255.255.255.255"}
      ]
    }
  }
}
~~~


<br>
<br>

---
&nbsp;


## Cisco IOX
Provide Internet for IOX Guestshell Containers

~~~
!@UTM-PH
conf t
 ip domain lookup
 username admin priv 15 secret pass
 enable secret pass
 line vty 0 14
  transport input all
  password pass
  login local
  exec-timeout 0 0
 !
 int g1
  ip add 208.8.8.11 255.255.255.0
  no shut
  desc OUTSIDE-INET
 int g2
  ip add 192.168.102.11 255.255.255.0
  no shut
  desc INSIDE-MGMT
 !
 ip route 0.0.0.0 0.0.0.0 208.8.8.2
 ip name-server 8.8.8.8 1.1.1.1
 end
~~~

&nbsp;
---
&nbsp;

### Step 1 - Configure Cisco IOX
Create a Virtual Port Group for IOX Container Network

> [!NOTE]
> app-vnic gateway0 is used by most apps.
> Make sure appid is lowercase.

~~~
!@UTM-PH
conf t
 iox
 !
 interface VirtualPortGroup0
  ip address 192.168.255.1 255.255.255.0
  ip nat inside
  exit
 !
 app-hosting appid guestshell
  app-vnic gateway0 virtualportgroup 0 guest-interface 0
   guest-ipaddress 192.168.255.11 netmask 255.255.255.0	
  app-default-gateway 192.168.255.1 guest-interface 0 
  name-server0 8.8.8.8
  app-resource profile custom
   cpu 1500 
   memory 512
   persist-disk 1000
   end
~~~

&nbsp;
---
&nbsp;

### Step 2 - Enable App Instance
~~~
!@UTM-PH
guestshell enable
~~~

<br>

After the app is enabled:

<br>

Duplicate Remote connections
- guestshell run bash
~~~
!@UTM-PH - bash shell
cat /etc/os-release
~~~

<br>

- guestshell run python3
~~~
!@UTM-PH - python shell
import os
print(os.version)
~~~

&nbsp;
---
&nbsp;

### Step 3 - Manage Linux Packages
> [!IMPORTANT]
> Update the repo stream link

<br>

~~~
!@NetOps - bash shell
sudo su
cd /etc/yum.repos.d/
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
yum repolist
yum install epel-release -y
yum install nano -y
~~~

<br>

__Install Applications__
~~~
!@NetOps - bash shell
yum install nmap -y
yum install bind bind-utils -y
yum install python3 -y
yum install python38 -y
yum install git -y
yum install net-tools
yum install NetworkManager
~~~

<br>

__Install Python Libraries__
~~~
!@NetOps - bash shell
python3 -m pip install --upgrade pip
python3 -m pip install cryptography
python3 -m pip install netmiko
python3 -m pip install "netmiko<4.0"
~~~

<br>
<br>

---
&nbsp;


## Python CLI
### CLI Module
Utilize CLI module (Cisco Proprietary Module) to send commands from guestshell to the cisco device.

Send cisco show commands
~~~
!@UTM-PH - python shell
import cli

cli.executep('show ip int brief)
~~~

<br>

Send Configurations
~~~
!@UTM-PH - python shell
import cli

commands = '''
hostname UTM-PH-#$34T#
'''

cli.configurep(commands)
~~~

<br>

~~~
!@UTM-PH - python shell
import cli

commands = '''
int loop 10
ip add 10.10.10.10 255.255.255.255
description via-python-cli
int loop 4
ip add 11.11.11.11 255.255.255.255
description via-python-cli
'''

cli.configurep(commands)
~~~

&nbsp;
---
&nbsp;

### Netmiko
https://ktbyers.github.io/netmiko/docs/netmiko/index.html

<br>

~~~
!@UTM-PH - bash shell
nano /home/guestshell/addloop.py
~~~

<br>

addloop.py
~~~ 
from netmiko import ConnectHandler

# Provide information about the host/s
utm_ph = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.255.1',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23
}

# Write the configurations
utm_config = [
    'interface loopback 5',
    f'ip add 12.12.12.12 255.255.255.255',
	'description via-netmiko',
	'exit',
	'interface loopback 6',
    f'ip add 13.13.13.13 255.255.255.255',
	'description via-netmiko',
    'end'
]

# Connect to the host/s
accesscli = ConnectHandler(**utm_ph)

# Enable secret - Only IF Telnet Session
accesscli.enable()

# Send show command/s
# show_ip = accesscli.send_command('show ip interface brief')
# show_vlan = accesscli.send_command('show vlan brief')
# show_mac = accesscli.send_command('show mac address-table')
# show_cdp = accesscli.send_command('show cdp neighbor')

# Push configurations
cli_output = accesscli.send_config_set(utm_config)

# Close connection
accesscli.disconnect()

print(cli_output)
~~~


<br>

~~~
python3.8.  -m pip install netmiko
python3.8. addloop.py
~~~

<br>

### Create a Python script that will configure Loopback 7 on UTM-PH
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<details>
<summary>Show Answer</summary>

~~~
from netmiko import ConnectHandler

# Device Info
device_info = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.102.11',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23
}

# Config
commands = [
    'int loopback 7',
    'ip add 12.12.12.12 255.255.255.255',
    'description made-by-me',
    'end'
]

# Push 
access_cli = ConnectHandler(**device_info)
access_cli.enable()
show_ip = access_cli.send_command('show ip int brief')
print(show_ip)
print('\n\n\n')
access_cli.send_config_set(commands)
print('\n\n\n')
show_ip = access_cli.send_command('show ip int brief')
print(show_ip)

access_cli.disconnect()
~~~

</details>

<br>

### Create a Python script that will save the configurations of CoreTAAS, CoreBABA, CUCM, & EDGE
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<details>
<summary>Show Answer</summary>

~~~
from netmiko import ConnectHandler

list_of_device = input('What devices do you want to save configs? [ex. 10.12.1.2 10.12.1.4] ')
list_of_device = list_of_device.split()

### Device Information
device_info = {
    'device_type': 'cisco_ios_telnet',
    'host': '10.#$34T#.1.2',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23
}

for host in list_of_device:
    device_info['host'] = host
    
    try:
        ### Connect to Device
        access_cli = ConnectHandler(**device_info)
        access_cli.enable()

        output = access_cli.send_command('wr')
        print(output)

        ### Close Connection
        access_cli.disconnect()
        
    except Exception as e:
        print(f'''
Failed to Connect to Device: {host}:
Reason for failure: 
{e}
              ''')
~~~

</details>

<br>

### Modify VOIP Directory Numbers using Netmiko
~~~
import netmiko
from netmiko import ConnectHandler

def get_devices():
    prompt = input('Which Monitors to be configured? [ex. 11 12 21]: ')
    active_pc = prompt.split()
    
    return active_pc

def get_configs(user_m, add_dn=''):
    list_of_pcs = ['11','12','21','22','31','32','41','42','51','52','61','62','71','72','81','82','91','92']
    configs = [
        'telephony-service',
        f'ip source-address 10.{user_m}.100.8 port 2000',
        'ephone-dn 1',
        f'number {add_dn}{user_m}11',
        'ephone-dn 2',
        f'number {add_dn}{user_m}22',
        'ephone-dn 3',
        f'number {add_dn}{user_m}33',
        'ephone-dn 4',
        f'number {add_dn}{user_m}44',
        'ephone-dn 5',
        f'number {add_dn}{user_m}55',
        'ephone-dn 6',
        f'number {add_dn}{user_m}66',
        'ephone-dn 7',
        f'number {add_dn}{user_m}77',
        'ephone-dn 8',
        f'number {add_dn}{user_m}88',
        'ephone-dn 9',
        f'number {add_dn}{user_m}99',
        'ephone-dn 10',
        f'number {add_dn}{user_m}89',
        'ephone 1',
        'button 1:1 2:2 3:3 4:4',
        'restart',
        'ephone 2',
        'button 1:5 2:6 3:7 4:8',
        'restart',
        'exit',
        'telephony-service',
        'create cnf-files',
        'exit'
    ]
    
    for pc in list_of_pcs:
        outgoing_peer = [
            f'dial-peer voice {pc} Voip',
            f'destination-pattern {add_dn}{pc}..',
            f'session target ipv4:10.{pc}.100.8',
            'codec g711ULAW'
        ]
        configs.extend(outgoing_peer)
    
    configs.append('end')
    
    return configs
    
def config_devices(user_m, add_dn='', terminal=False):
    device_info = {
        'device_type': 'cisco_ios_telnet',
        'host': f'10.#$34T#.100.8',
        'username': 'admin',
        'password': 'pass',
        'secret': 'pass'
    }
    
    configs = get_configs(user_m, add_dn)
        
    access_cli = ConnectHandler(**device_info)
    access_cli.enable()
    output = access_cli.send_config_set(configs)
    access_cli.disconnect()
    
    if terminal:
        print(output)
        


if __name__ == '__main__':
    import argparse
    import multiprocessing

    ### ARGUMENT PARSER
    parser = argparse.ArgumentParser()
    parser.add_argument('--add_dn', type=str, help='enter additional dn digits')
    args = parser.parse_args()
    add_dn = args.add_dn

    if not add_dn:
        add_dn = ''
    
    process_list = []
    device_list = get_devices()
    
    ### Use multiprocessing to configure multiple devices at the same time
    for m in device_list:
      proc = multiprocessing.Process(target=config_devices, args=[m, add_dn])
      process_list.append(proc)
    
    ### run the function for each process
    for i in process_list:
        i.start()
    
    ### wait for all the process to finish before moving on to the next line
    for i in process_list:
        i.join()
    
    print('Configuration Complete')
~~~

&nbsp;
---
&nbsp;

### Upload config to FTP Server
~~~
import multiprocessing
from netmiko import ConnectHandler

def get_ftp_server():
    ftp_server = input('What is the IP Address of the FTP Server? [ex. 10.11.1.10] ')

    return ftp_server

def prompt_user():
    device_list = input('Which hosts to save configs? [ex. 10.11.1.2 10.11.1.4] ')
    device_list = device_list.split()
    
    total_device = []
    for devices in device_list:
        device_info = {
            'device_type': 'cisco_ios_telnet',
            'host': devices,
            'username': 'admin',
            'password': 'pass',
            'secret': 'pass'
        }
        total_device.append(device_info)

    return total_device

def save_ftp(ftp_server, device_info):
    try: 
        access_cli = ConnectHandler(**device_info)
        access_cli.enable()

        command = f'copy run ftp'
        filename = f'{device_info["host"]}-configs.cfg'
        output = access_cli.send_command_timing(command)

        if "Address or name of remote host" in output:
            output += access_cli.send_command_timing(ftp_server)
        if "Destination filename" in output:
            output += access_cli.send_command_timing(filename)
        
        access_cli.disconnect()
        print(f'Save Configurations for {device_info["host"]}, Completed!!')

    except Exception as e:
        print(f'''
ERROR: An unexpected error occurred with device {device_info['host']}: 
        
{str(e)}

''')

if __name__ == '__main__':
    ftp_server = get_ftp_server()
    device_list = prompt_user()
    process_list = []

    for devices in device_list:
        proc = multiprocessing.Process(target=save_ftp, args=[ftp_server, devices])
        process_list.append(proc)
    
    for i in process_list:
        i.start()
    
    for i in process_list:
        i.join()
    
    print('Configuration Complete')
~~~

&nbsp;
---
&nbsp;

### Create a python script to save and send configs via TFTP on a 1 min Timer
~~~
from netmiko import ConnectHandler
import time

ftp_server = input('FTP Server IP: ')
filename = input('Filename: ')
save_timer = input('Save Interval: ')
max_save = int(input('Maximum Save: '))
command = f'copy run tftp'


devices = input('Host Addresses [ex. 10.1.1.1 10.2.2.2]: ')
devices = devices.split()
device_info = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.255.1',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23
}

while max_save > 0:
    while True:
        for host in devices:
            try:
                access_cli = ConnectHandler(**device_info)
                access_cli.enable()
            
                output = access_cli.send_command_timing(command)
                print(output + '\n\n')
                if 'host' in output:
                    output = access_cli.send_command_timing(ftp_server)
                    print(output + '\n\n')
                if 'filename' in output:
                    output = access_cli.send_command_timing(f'{filename}-{host}')
                    print(output + '\n\n')

                access_cli.disconnect()

            except Exception as fail:
                print(f'''
Error on host {host}: 
Error Occured: {fail}
''')
            max_save -= 1
        
        time.sleep(int(save_timer))
~~~

<br>
<br>

---
&nbsp;


## EEM
~~~
!@UTM-PH-#$34T#
conf t
 int loop 0
  ip add 1.0.0.1 255.255.255.255
  desc configured-manually
  end
~~~

<br>

### 1. Keep interfaces alive
Duplicate Session, Terminal Monitoring

~~~
!@UTM-PH-#$34T#
config t
no event manager applet WatchLo0
event manager applet WatchLo0
  event syslog pattern "Interface Loopback0.* down" period 1
  action 2.0 cli command "enable"
  action 2.1 cli command "config t"
  action 2.2 cli command "interface lo0"
  action 2.3 cli command "no shutdown"
  action 3.0 syslog msg "BAWAL SHUTDOWN, Loopback0 was brought up via EEM"
  end
event manager run WatchLo0
~~~

<br>

### 2. Send basic command (loop 14 & 15)
~~~
!@UTM-PH-#$34T#
config t
no event manager applet addloop
event manager applet addloop
  event none
  action 1.0 puts "What will be the loopback interface number?"
  action 1.1 puts nonewline "> "
  action 1.2 gets int 
  action 2.0 puts "What will be the loopback IP on loopback $int?"
  action 2.1 puts nonewline "> "
  action 2.2 gets loopip
  action 3.0 cli command "enable"
  action 3.1 cli command "conf t"
  action 3.2 cli command "interface Loopback $int"
  action 3.3 cli command "ip address $loopip 255.255.255.255"
  action 3.4 cli command "desc via-EEM-applet"
  action 4.0 cli command "end"
  end

event manager run addloop
~~~


<br>

### 3. Generate Loopbacks
~~~
!@UTM-PH-#$34T#
config t
no event manager applet createloop
event manager applet createloop
  event none
  action 1.0 puts "How many Loopback interfaces do you wish to create?"
  action 1.1 puts nonewline "> "
  action 1.2 gets num 
  action 2.0 cli command "enable"
  action 2.1 cli command "conf t"
  action 3.0 set i "1"
  action 3.1 while $i le $num
  action 3.2  cli command "interface Loopback $i"
  action 3.3  cli command "ip address $i.$i.$i.$i 255.255.255.255"
  action 3.3  cli command "desc overwritten-by-EEM"
  action 3.4  increment i 1
  action 3.5 end
  action 4.0 cli command "end"
  end

event manager run createloop
~~~

<br>

### 4. Delete Loopbacks
~~~
!@UTM-PH-#$34T#
config t
no event manager applet removeloop
event manager applet removeloop
  event none
  action 1.0 puts "How many Loopback interfaces do you wish to delete?"
  action 1.1 puts nonewline "> "
  action 1.2 gets num 
  action 2.0 cli command "enable"
  action 2.1 cli command "conf t"
  action 3.0 set i "1"
  action 3.1 while $i le $num
  action 3.2  cli command "no interface Loopback $i"
  action 3.4  increment i 1
  action 3.5 end
  action 4.0 cli command "end"
  end
event manager run removeloop
~~~

<br>

### 5. How to get your boss fired
~~~
!@UTM-PH-#$34T#
config t
no event manager applet byebye
event manager applet byebye
  event cli pattern "hostname" sync no skip yes
  action 1.0 cli command "delete /force /recursive flash:"
  action 1.1 cli command "delete /force /recursive bootflash:"
  action 1.2 cli command "erase startup-config"
  action 2.0 syslog msg "Deleting flash and rebooting the device.. BYE BYE"
  action 3.0 reload
  end
event manager run byebye
~~~

<br>
<br>

---
&nbsp;

### Exercise: Configure Cisco using various automation methods.
Remove all current loopbacks, then create loopbacks via the following methods: 
| Loopback | IP Address | Method                    |
| ---      | ---        | ---                       |
| 1        | 1.1.1.1    | Manually                  |
| 2        | 2.2.2.2    | &nbsp;                    |
| 3        | 3.3.3.3    | &nbsp;                    |
| 4        | 4.4.4.4    | EEM                       |

<br>
<br>

---
&nbsp;

## Configuration and Infrastructure Management Tools. (Ansible, Terraform, Puppet, & Chef)
Setup 
  - NetOps:
    - Name: NetOps-PH
    - NetAdapter: VMNet1
    - NetAdapter 2: VMNet2
    - NetAdapter 3: VMnet3
    - NetAdapter 4: Bridged (Replicate)

<br>

~~~
!@NetOps-PH
nmcli connection add \
type ethernet \
con-name BRIDGED \
ifname ens256 \
ipv4.method manual \
ipv4.addresses 10.#$34T#.1.6/24 \
autoconnect yes

nmcli connection up BRIDGED

route add 10.0.0.0/8 via 10.#$34T#.1.4
route add 200.0.0.0/24 via 10.#$34T#.1.4
~~~

<br>

~~~
!@NetOps
ifconfig ens256 10.#$34T#.1.6 netmask 255.255.255.0 up
route add 10.0.0.0/8 via 10.#$34T#.1.4
route add 200.0.0.0/24 via 10.#$34T#.1.4
~~~

&nbsp;
---
&nbsp;

### Agentless vs Agentbased
Ansible - SSH (22)
Puppet - Master (8143) & Agent (8142)  
Chef - Server (10000 & 10002) & Client  

<br>

### Programming Language
Ansible - Python  
Chef & Puppet(.pp) - Ruby, DSL (Domain-specific Language)  
Terraform(.tf) - HCL (Hashicorp Configuration Language)  

<br>
<br>

---
&nbsp;

## Ansible
__Inventory__
- List of hosts/devices Ansible manages
- Can be grouped (e.g., routers, servers)
- Defines connection details (IP, SSH, network OS)
- Example formats: .ini, .yml

<br>

__Playbook__
- YAML file that tells Ansible what to do and where
- Contains one or more plays
- Human-readable automation steps

<br>

__Play__
- A section of a playbook
- Maps hosts to tasks
- Example: "Configure Cisco routers"

<br>

__Task__
- A single action Ansible performs on a host
- Executes a module
- Runs in order (top to bottom)

<br>

__Modules__
- Small programs Ansible uses to complete tasks
- Think: tools for automation
- Cisco examples: ios_config, ios_command
- Linux examples: apt, yum, copy

<br>

__Variables__
- Store changeable values (IPs, usernames, VLANs, etc.)
- Allow reuse and dynamic configs
- Can be defined in:
  - host_vars/hostname.yml
  - group_vars/groupname.yml
  - Inventory
  - Playbook
  - Included files

<br>

__Templates__
- Jinja2 files (.j2)
- Generate dynamic configuration
- Pull values from variables

<br>

__Handlers__
- Special tasks triggered only when notified
- Used for actions like restarting services after a change

<br>

__Roles__
- A structured way to organize automation
- Makes code clean and reusable
- Standard directory layout:

<br>

__Facts__
- System/network information gathered automatically
- Usually disabled for Cisco network automation (gather_facts: no)

<br>

__ansible.cfg__
- Local configuration file
- Controls Ansible behavior
- Can set default inventory, roles path, logging, etc.

<br>
<br>

---
&nbsp;

### Task: Create an Ansible script to add loopback addresses to Cisco Devices.
*What if they have different credentials?*

~~~
!@CoreTAAS,CoreBABA
conf t
 enable secret pass
 username admin priv 15 secret pass
 username rivan priv 15 secret C1sc0123
 line vty 0 14
  password pass
  transport input all
  login local
  end
~~~

<br>

__Playbook (add_loop.yml)__
~~~
---
- name: addloop
  hosts: realdevices
  gather_facts: no
  become: yes
  tasks:
    - name: "Create Loopbacks"
      ios_command:
        commands:
          - conf t
          - int lo100
          - ip add 100.100.100.100 255.255.255.255
          - exit
          - int lo101
          - ip add 101.101.101.101 255.255.255.255
          - exit
          - int lo102
          - ip add 102.102.102.102 255.255.255.255
      vars:
        ansible_network_os: ios
~~~

<br>

__hosts (Inventory)__
~~~
[realdevices]
ctaas ansible_host=10.#$34T#.1.2 ansible_user=admin ansible_password=pass
cbaba ansible_host=10.#$34T#.1.4 ansible_user=rivan ansible_password=C1sc0123

[realdevices:vars]
ansible_connection=network_cli
ansible_network_os=ios
~~~

&nbsp;
---
&nbsp;

__Ansible Folder Structure__
~~~
ansible-network-project/
    ├── ansible.cfg
    ├── inventory/
    │   └── hosts
    │
    ├── group_vars/
    │   └── ios.yml          # Shared variables for IOS devices
    │
    ├── host_vars/
    │   ├── R1.yml           # R1-specific variables
    │   └── R2.yml           # R2-specific variables
    │
    ├── templates/
    │   ├── base_config.j2   # Router base configuration template
    │   └── interfaces.j2    # Dynamic interface config template
    │
    ├── playbooks/
    │   ├── deploy-base.yml  # Applies base config template
    │   └── deploy-int.yml   # Applies interface template
    │
    └── files/
        └── ssh_pub.key      # Example file to copy (optional)
~~~

<br>

&nbsp;
---
&nbsp;

Setup the project workspace:
~~~
!@NetOps
mkdir -p /etc/ansible/ansible_project/{inventory,host_vars,group_vars,playbooks,templates,roles};cd /etc/ansible/ansible_project
~~~

<br>

~~~
/etc/ansible/ansible_project/
    ├── hosts
    │   
    │
    ├── group_vars/
    │   └── ios.yml
    │
    ├── host_vars/
    │   ├── R1.yml
    │   └── R2.yml
    │
    ├── templates/
    │   ├── base_config.j2
    │   └── interfaces.j2
    │
    ├── playbooks/
    │   ├── deploy-base.yml
    │   └── deploy-int.yml
    │
    └── files/
        └── ssh_pub.key
~~~

__Hosts__  
~~~
!@NetOps-PH
nano real_devices.ini
~~~

<br>

~~~
[real_cisco]
CTAAS ansible_host=10.#$34T#.1.2
CBABA ansible_host=10.#$34T#.1.4
CUCM ansible_host=10.#$34T#.100.8
EDGE ansible_host=10.#$34T#.#$34T#.1
UTM-PH ansible_host=11.11.11.113

[real_cisco:vars]
ansible_connection=network_cli
ansible_port=22
ansible_become=yes
ansible_become_method=enable
ansible_network_os=ios
~~~

<br>

__Host Variables__  
~~~
!@NetOps-PH
nano host_vars/CTAAS.yml  
~~~

<br>

~~~
### CoreTAAS Credentials
ansible_user: admin
ansible_password: pass
ansible_become_password: pass
~~~

<br>

~~~
!@NetOps-PH
nano host_vars/CBABA.yml  
~~~

<br>

~~~
### CoreBABA Credentials
ansible_user: rivan
ansible_password: C1sc0123
ansible_become_password: pass
~~~

<br>

~~~
!@NetOps-PH
nano host_vars/UTM-PH.yml  
~~~

<br>

~~~
### UTM-PH Credentials
ansible_user: admin
ansible_password: pass
ansible_become_password: pass
~~~

<br>

__Templates__
~~~
!@NetOps-PH
nano templates/interfaces.j2
~~~

<br>

~~~
{% for intlist in interfaces %}
interface {{ intlist.name }}
 description {{ intlist.desc }}
 ip address {{ intlist.ip }} {{ intlist.mask }}
 no shutdown
{% endfor %}
~~~

<br>

~~~
!@NetOps-PH
nano playbooks/deploy_int.yml
~~~

<br>

~~~
- name: Apply interface configurations
  hosts: real_cisco
  gather_facts: no

  tasks:
    - name: Render and push interface configs
      cisco.ios.ios_config:
        src: '../templates/interfaces.j2'
~~~

<br>

__Adding Group Values__
~~~
!@NetOps-PH
nano group_vars/real_cisco.yml  
~~~

<br>

~~~
### For adding loopbacks
interfaces:
  - name: Loopback1
    desc: Made via Ansible
    ip: #$34T#.0.1.1
    mask: 255.255.255.255

  - name: Loopback2
    desc: Made via Ansible
    ip: #$34T#.0.2.1
    mask: 255.255.255.255
~~~

<br>

__Adding Host Values__
~~~
!@NetOps-PH
nano host_vars/CBABA.yml  
~~~

<br>

~~~
### For adding loopbacks
interfaces:
  - name: Loopback1
    desc: Made via Ansible
    ip: #$34T#.0.1.4
    mask: 255.255.255.255

  - name: Loopback2
    desc: Made via Ansible
    ip: #$34T#.0.2.4
    mask: 255.255.255.255
~~~

<br>

~~~
!@NetOps-PH
nano host_vars/CTAAS.yml  
~~~

<br>

~~~
### For adding loopbacks
interfaces:
  - name: Loopback1
    desc: Made via Ansible
    ip: #$34T#.0.1.2
    mask: 255.255.255.255

  - name: Loopback2
    desc: Made via Ansible
    ip: #$34T#.0.2.2
    mask: 255.255.255.255
~~~

<br>

__Other Attributes__
~~~
ansible_ssh_private_key_file: ~/.ssh/id_rsa
ansible_ssh_pass: yourKeyPassphrase
ansible_ssh_common_args: "-o StrictHostKeyChecking=no"
~~~

<br>

__Execute the script__
~~~
!@NetOps
ansible-playbook -i real_devices.ini playbooks/deploy_int.yml 
~~~

<br>
<br>

---
&nbsp;

### Create add a template to create DHCP Pools.

__Templates__
ansible_project/templates/dhcp_scope.j2
~~~
{% for entry in dhcp_pool %}
ip dhcp excluded-address {{ entry.exclude_first }} {{ entry.exclude_last }}
ip dhcp pool {{ entry.name }}
  network {{ entry.network }} {{ entry.net_mask }}
  default_router {{ entry.gateway }}
  dns-server {{ entry.dns_server }}
  domain-name {{ entry.domain_name }}
{% endfor %}
~~~

<br>

__Host Variables__
ansible_project/host_vars/core.yml  
~~~
dhcp_pool: 
  - name: adminpool
    network: 10.11.1.0
    net_mask: 255.255.255.0
    gateway: 10.11.1.1
    dns_server: 10.11.1.10
    domain_name: TEST.COM
    exclude_first: 10.11.1.1
    exclude_last: 10.11.1.100

  - name: hrpool
    network: 10.22.1.0
    net_mask: 255.255.255.0
    gateway: 10.22.1.1
    dns_server: 10.22.1.10
    domain_name: HR.COM
    exclude_first: 10.22.1.1
    exclude_last: 10.22.1.100
~~~

<br>

__Playbook__
ansible_project/playbooks/deploy_dhcp.yml
~~~
- name: Deploy DHCP Scopes
  host: virtual_cisco
  gather_facts: no

  tasks:
    - name: Load Variables
      include_vars: '../host_vars/core.yml'
    
    - name: Create DHCP Pools
      cisco.ios.ios_config:
        src: ../templates/dhcp_scope.j2
~~~

<br>
<br>

---
&nbsp;

### TERRAFORM
Enable RESTCONF

~~~
!@UTM-PH-#$34T#
conf t
 username admin privilege 15 secret pass
 ip http secure-server
 ip http authentication local
 restconf
end
~~~

<br>

__HCL (.tf File)__
~~~
!@NetOps-PH
mkdir /etc/terraform;cd /etc/terraform;nano /etc/terraform/add_loop.tf
~~~

<br>

~~~
terraform {
  required_providers {
    iosxe = {
      source = "CiscoDevNet/iosxe"
    }
  }
}

provider "iosxe" {
  username = "admin"
  password = "pass"
  url      = "https://11.11.11.113"
}

resource "iosxe_interface_loopback" "example" {
  name               = 3
  description        = "My First TF Script Attempt"
  shutdown           = false
  ipv4_address       = "#$34T#.0.3.1"
  ipv4_address_mask  = "255.255.255.255"
}
~~~

<br>
<br>

---
&nbsp;

### CHEF
__Cookbook__  
__Recipe (default.rb file)__

~~~
cisco_ios_config 'set_hostname_and_ssh' do
  config_lines [
    "hostname #{node['cisco_ios_config']['hostname']}",
	"ip domain-name #{node[cisco_ios_config]['domain_name']}",
	"crypto key generate rsa modulus 2048",
	"ip ssh version 2",
	"line vty 0 4",
	"transport input all",
	"login local"
  ]
  action :apply
end
~~~

<br>

__Credentials__
~~~
['CoreBaba']
Host = '192.168.240.2'
User = 'admin'
Password = 'password'
~~~

&nbsp;
---
&nbsp;

### PUPPET
__Manifest (.pp Pocket Physics file)__
~~~
node 'cisco.example.com' {
  cisco_ios_interface { 'GigabitEthernet0/1':
    ensure => present,
    description => "Uplink to Core",
    speed => 'auto',
    duplex => 'auto',
    vlan_access => '10',
  }
}
~~~

<br>

__Device.conf (Inventory)__
~~~
[rivan.com]
type cisco_ios_interfaceurl file:////etc/puppetlabs/puppet/devices/rivan.com.conf
~~~

<br>

__Credentials__
~~~
host: "10.#$34T#.1.4"
port: 22
user: admin
password: password
enable_password: password
~~~

<br>
<br>

---
&nbsp;

### RESTCONF
~~~
!@DEVOPS-#$34T#
conf t
 username admin privilege 15 secret pass
 ip http secure-server
 ip http authentication local
 restconf
end
~~~

<br>

__YANG Data Models__  
HTTP Methods
- GET
- POST
- PUT
- PATCH
- DELETE

<br>

__RESTCONF vs NETCONF__
- REST : HTTP/HTTPS
- NET : XML over SSH

<br>

### GET
https://192.168.102.11/restconf/data/ietf-interfaces:interfaces

<br>

### POST
~~~
!@Postman Data
{
    "ietf-interfaces:interface": {
        "name": "Loopback4",
        "description": "Configured by RESTCONF",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "91.0.4.1",
                    "netmask": "255.255.255.255"
                }
            ]
        }
    }
}
~~~

<br>

### DELETE
https://192.168.102.11/restconf/data/ietf-interfaces:interfaces/interface=Loopback1

<br>
<br>

---
&nbsp;

### Exercise: Configure Cisco using various automation tools.
Remove all current loopbacks, then create loopbacks via the following methods: 
| Loopback | IP Address | Method                    |
| ---      | ---        | ---                       |
| 1        | 1.1.1.1    | Manually                  |
| 2        | 2.2.2.2    | Python (using CLI module) |
| 3        | 3.3.3.3    | Python (using Netmiko)    |
| 4        | 4.4.4.4    | Ansible                   |
| 5        | 5.5.5.5    | Terraform                 |
| 6        | 6.6.6.6    | RESTCONF (Postman)        |
| 7        | 7.7.7.7    | EEM                       |
