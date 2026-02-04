
<!-- Your monitor number = #$34T# -->


# 👋 Welcome to Rivan
*"There's no better teacher than experience"*

<br>
<br>

## 📂 Create your own folder in the desktop
~~~
@cmd
cd Desktop
mkdir _name-#$34T#
cd _name-#$34T#
dir
~~~

<br>
<br>

---
&nbsp;

# 🏦 Secure Enterprise Network Architecture

<br>
<br>

## 📤 IT Service Management
### Lab Setup
__1. Run the *SOC-IR* virtual machine.__  

<br>

__2. VM Login information:__
> Username: root  
> Password: C1sc0123

<br>

__3. Get the IP address of the VM.__  
Enter the command inside the VM
~~~bash
@SOC-IR
ip addr
~~~

<br>

__4. Add a hostname mapping.__  
Access the __hosts__ file located on `c:\Windows\System32\drivers\etc`  
Then, enter add the following mapping to the hosts file:
~~~
208.8.8.144  rivan.cloudsoc.com
~~~

> [!Note]
> __208.8.8.144__ must be your virtual machine IP address.

<br>

__5. Ping to verify setup for the virtual machine.__
~~~
@cmd
ping rivan.cloudsoc.com
~~~

&nbsp;
---
&nbsp;

## 🔄 ITSM Process | Implementing Cybersecurity best practices
### 👤 Upper Management
http://rivan.cloudsoc.com:8069  
> Username: itil@rivanschool.com  
> Password: C1sc0123

<br>

![otrs_odoo](img/oss_odoo.JPG)


&nbsp;
---
&nbsp;

### 🏃 Service Delivery Team
http://rivan.cloudsoc.com/otrs/index.pl  
> Username: root@localhost  
> Password: C1sc0123

<br>

![otrs_index](img/oss_index.JPG)


&nbsp;
---
&nbsp;

### 🙇 Service Desk
http://rivan.cloudsoc.com/otrs/customer.pl  
> Username: user1  
> Password: C1sc0123

<br>

![otrs_customer](img/oss_customer.JPG)

&nbsp;
---
&nbsp;

## 📦 Operational Support System
*How easy is it to bring home items from your company?*

- AMS (Asset Management System)
- IMS (Inventory Management System)
- CMDB (Configuration Management Databases)

<br>

### 🎯 Exercise 01: Register Windows Server 2025 to your company's database.

__1. Access CMDB__  
<br>

![cmdb](img/oss_01.JPG)

<br>
<br>

__2. Select the appropriate Item Class__  
<br>

![item_class](img/oss_02.JPG)

<br>
<br>

__3. Register Windows Server 2025.__  
  
View System specs using __DirectX Diagnostic Tool__  
~~~
@WinServer [Win + R]
dxdiag
~~~

<br>

Or view __System Information__  
~~~
@WinServer [Win + R]
msinfo32
~~~

<br>

Identify Serial number
~~~powershell
@powershell
Get-WmiObject win32_bios | select Serialnumber
~~~

<br>
<br>

---
&nbsp;

## 🚀 Deploy CoreTAAS
### ⭐ 1. Register CoreTAAS to your company's database, including a *Workorder* to configure the devices.

~~~
!@CoreTaas
conf t
 hostname CoreTAAS-#$34T#
 enable secret pass
 service password-encryption
 no logging console
 no ip domain-lookup
 line cons 0
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 vlan 10
  name WIFIVLAN
 vlan 50
  name CCTVVLAN
 vlan 100
  name VOICEVLAN
 int vlan 1
  no shut
  ip add 10.#$34T#.1.2 255.255.255.0
  desc DEFAULT-VLAN
 int vlan 10
  no shut
  ip add 10.#$34T#.10.2 255.255.255.0
  desc WIFI-VLAN
 int vlan 50
  no shut
  ip add 10.#$34T#.50.2 255.255.255.0
  desc CCTV-VLAN
 int vlan 100
  no shut
  ip add 10.#$34T#.100.2 255.255.255.0
  desc VOICE-VLAN
 end
~~~

<br>
<br>

__Create a Custom User Agent__  
`Admin` > `Agents` > `Add Agents`

<br>

__Add an Agent to the Work Order__  
`Workorder` > `History` > `Show Workorder` > `Add Agent`

<br>
<br>

---
&nbsp;

## 🚀 Deploy CoreBABA
### 🎯 Exercies 01: Register CoreBABA to your company's database.

<br>
<br>
<br>
<br>
<br>
<br>

## Know the jobs of a Switch
### ⚙️ 1. __POE__
> [!NOTE]
> If you need PoE functionality on a non-PoE switch, use a PoE injector.

<br>

| IEEE Standards  | Power Output |
| ---             |     ---      |
| 802.3af (PoE)   |              |
| 802.3at (PoE+)  |              |
| 802.3bt (PoE++) |              |

&nbsp;
---
&nbsp;

Which device consumes the most power? __SPI - `show power inline`__
~~~
!@CoreBABA
show power inline
~~~

<br>

> __ITSM__  
> Title: 1st Job of a Switch - PoE  
> Description: Purchase switches with PoE - 802.3af,at,bt  
> Justification: Switches need to supply the right amount of power depending on the needs of end devices.  

<br>
<br>

---
&nbsp;

### ⚙️ 2. SVI (Switch Virtual Interface)

<br>

> __ITSM__  
> Title: 2nd Job of a Switch - SVI  
> Description: Configure IP addresses on switches  
> Justification: Segment network traffic to reduce security risks and network traffic congestion.  

<br>

~~~
!@CoreBABA
conf t
 hostname coreBaba-#$34T#
 enable secret pass
 service password-encryption
 no logging console
 no ip domain-lookup
 line cons 0
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int gi 0/1
  no shut
  no switchport
  ip add 10.#$34T#.#$34T#.4 255.255.255.0
 int vlan 1
  no shut
  ip add 10.#$34T#.1.4 255.255.255.0
  desc DEFAULT-VLAN
 int vlan 10
  no shut
  ip add 10.#$34T#.10.4 255.255.255.0
  desc WIFI-VLAN
 int vlan 50
  no shut
  ip add 10.#$34T#.50.4 255.255.255.0
  desc CCTV-VLAN
 int vlan 100
  no shut
  ip add 10.#$34T#.100.4 255.255.255.0
  desc VOICE-VLAN
 end
~~~

<br>

Verify Connectivity: 

~~~
!@cmd
ping 10.#$34T#.1.4
~~~

<br>

Although unsecure, why do some companies still utilize a Flat Network? *Simple and low cost*  
__BUT__  
*You get what you pay for*
- __Slow network traffic__ | Performance Bottlenecks
- __Security Risks__ | Succeptible to attacks 
- __Single point of failure__

<br>
<br>

---
&nbsp;

# ⭐ Fundamental Security Concepts
1. __C__
2. __I__
3. __A__

&nbsp;
---
&nbsp;

### 🔐 Confidentiality
### 5 Phases of Ethical Hacking
__1. Reconnaissance - gather information.__

### `cia.gov`    vs    `neu.edu.ph`   vs   `sti.edu.ph`   vs   `dpwh.gov.ph`

<br>

~~~
!@cmd
ping 10.#$34T#.1.4
ping 10.#$34T#.1.2
~~~

<br>

~~~
!@cmd
nmap -sP 10.28.0.0/24
nmap -O 10.28.0.0/24
~~~

<br>

__2. Scanning - find open ports, active devices, and services. Find Vulnerabilities__
~~~
!@cmd
nmap -v 10.#$34T#.1.2
~~~

<br>

Is port __23/Telnet__ open?  
Is port __445/Microsoft-DS & 139/ServerMessageBlock__ open?  

<br>

__3. Gaining Access - Utilize weaknesses and establish connectivity__
*How to access port 445 because you don't have a Firewall!*
~~~
!@cmd
net use \\10.28.0.x\ipc$
net use x: /delete
net use x: \\10.28.0.x\c$
~~~

<br>

__4. Maintain Access - Install backdoors, rootkits, or Trojan for continued access.__
ex. Keylogger

<br>

__5. Clear Tracks - remain under the radar. Wipe logs, conceal files, manipulate timestamps.__
Detect who is connected to you
~~~
!@cmd
netstat -s -p tcp
~~~

<br>
<br>

---
&nbsp;

### 🎯 Exercise 02: Why use VPN when you are WFH
~~~
!@CoreTAAS
conf t
 username admin privilege 15 secret pass
 line vty 0 14
  password pass
  login local
  exec-timeout 0 0
  end
~~~

<br>

__Implement Secure Protocols: SSH__

| 🔑 | Public | Private | 🔑 |
| --- | ---   | ---     | --- |

<br>

~~~
!@CoreTAAS
conf t
 ip domain name sec.com
 crypto key generate rsa
 2048
 ip ssh version 2
 line vty 0 14
  transport input all
  end
~~~

<br>
<br>

---
&nbsp;

### ✉️ Integrity
~~~
!@cmd
certutil -hashfile [FILE] sha256
~~~

<br>
<br>

---
&nbsp;

### 🔀 Availability
*Avoid a single point of failure*

<br>

Expensive Switches have __Loop Avoidance__

<br>

Execute a persistent ping
~~~
!@cmd
ping 10.#$34T#.1.2 -t
~~~

<br>

Combine Cables to achieve higher Bandwidth.

<br>

~~~
!@CoreBABA & CoreTAAS
conf t
 int range fa0/10-12
  channel-group 1 mode active
  exit
 int po1
  switchport trunk encaps dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
  end
show int po1 | inc BW
~~~

<br>
<br>

---
&nbsp;

### ⚙️ 3. DHCP / BOOTPS & BOOTPC
*In a network, which device should be a DHCP Server? __It depends.__*

| Network     | DHCP Device |
| ---         |     ---     |
| SOHO        | Router      |
|             |             |
| Enterprise  |             |
| Medium Biz  | Firewall    |
| Large Biz   | Core Switch |

<br>

> __ITSM__  
> Title: 3rd Job of a Switch - DHCP  
> Description: Provide IP addresses, and more, to end devices.  
> Justification: Devices needs IP address to communicate within a network.  

<br>

~~~
!@CoreTAAS
conf t
 ip dhcp excluded-address 10.#$34T#.1.1 10.#$34T#.1.100
 ip dhcp excluded-address 10.#$34T#.10.1 10.#$34T#.10.100
 ip dhcp excluded-address 10.#$34T#.50.1 10.#$34T#.50.100
 ip dhcp excluded-address 10.#$34T#.100.1 10.#$34T#.100.100
 ip dhcp pool POOLDATA
  network 10.#$34T#.1.0 255.255.255.0
  default-router 10.#$34T#.1.4
  domain-name MGMTDATA.COM
  dns-server 10.#$34T#.1.10
 ip dhcp pool POOLWIFI
  network 10.#$34T#.10.0 255.255.255.0
  default-router 10.#$34T#.10.4
  domain-name WIFIDATA.COM
  dns-server 10.#$34T#.1.10
  option 43 ip 10.#$34T#.10.7
 ip dhcp pool POOLCCTV
  network 10.#$34T#.50.0 255.255.255.0
  default-router 10.#$34T#.50.4
  domain-name CCTVDATA.COM
  dns-server 10.#$34T#.1.10
 ip dhcp pool POOLVOICE
  network 10.#$34T#.100.0 255.255.255.0
  default-router 10.#$34T#.100.4
  domain-name VOICEDATA.COM
  dns-server 10.#$34T#.1.10
  option 150 ip 10.#$34T#.100.8
  end
~~~

<br>
<br>

---
&nbsp;

### ⚙️ 4. VLAN Creation & VLAN Management
*Ports must be placed in the correct VLANs.*

<br>

*How to check what ports belong to what VLAN? __SVB - `show vlan brief`__*

~~~
!@CoreBABA
show vlan brief
~~~

&nbsp;
---
&nbsp;

Just because there's an SVI doesn't mean there's a VLAN.

<br>

> __ITSM__  
> Title: 4th Job of a Switch - VLAN Creation & VLAN Management  
> Description: Create VLANs and assign switchports to a specific VLAN.  
> Justification: By default, all switchports belong to VLAN 1.  

<br>

~~~
!@CoreBABA
conf t
 vlan 1
  name MGMTVLAN
 vlan 10
  name WIFIVLAN
 vlan 50
  name CCTVVLAN
 vlan 100
  name VOICEVLAN
  end
~~~

&nbsp;
---
&nbsp;

Place Switchports in their correct VLAN.

~~~
!@CoreBABA
conf t
 int fa 0/2
  switchport mode access
  switchport access vlan 10
 int fa 0/4
  switchport mode access
  switchport access vlan 10
 int fa0/6
  switchport mode access
  switchport access vlan 50
 int fa0/8
  switchport mode access
  switchport access vlan 50
 int fa 0/3
  switchport mode access
  switchport access vlan 100
 int fa 0/5
  switchport mode access
  switchport voice vlan 100
  switchport access vlan 1
 int fa 0/7
  switchport mode access
  switchport voice vlan 100
  switchport access vlan 1
 end
~~~

<br>

*What happens when a device is connected to a VLAN that does not exist? __Orphan-ports__*

<br>
<br>

---
&nbsp;

## 📠 Enterprise Communication
*How often are meetings conducted in your work place?*

<br>

Cisco Unified Call Manager | [Unified Communications and Collaboration.](https://www.cisco.com/c/en/us/products/unified-communications/index.html)
  - POTS (__Analog__)
  - VOIP (__ePhone__)

&nbsp;
---
&nbsp;

### Requirements to make IP Phones Operational
7.
6.
5.
4.
3. I__  _____       Did your phone get the correct IP?
2. M__  _____
1. P__

<br>
<br>

---
&nbsp;

## ⚙️ 5. MAC Learning & MAC Reservation
*What is in a MAC Address?*
- OUI (Organizationally Unique Identifier)
- UI

<br>

How switches forward data? __Frame Forwarding__

~~~
!@Windows
arp /ah

!@Linux
arp -a
~~~

<br>

How to view the MAC addresses learned by the Switch? __SMAC - `show mac address-table`__
~~~
!@CoreBABA
show mac address-table
~~~

<br>

| Camera         | MAC Address      |
| ---            | ---              |
| Camera fa0/6   | #camera6macadd#  |
| Camera fa0/8   | #camera8macadd#  |

<br>

Assign a specific IP address to a device.

> __ITSM__  
> Title: 5th Job of a Switch - MAC Learning & MAC Reservation  
> Description: Reserve IP addresses for Cameras  
> Justification: To maintain reliable network access.  

~~~
!@CoreBABA
conf t
 ip routing
 ip dhcp pool CAMERA6
  host 10.#$34T#.50.6 255.255.255.0
  client-identifier #camera6macadd#
 ip dhcp pool CAMERA8
  host 10.#$34T#.50.8 255.255.255.0
  client-identifier #camera8macadd#
 end
~~~

<br>

Verify DHCP: __SIDB - `show ip dhcp bindings`__

~~~
!@CoreBABA
show ip dhcp bindings
~~~

&nbsp;
---
&nbsp;

Review the jobs of a switch:
 1. &nbsp;
 2. &nbsp;
 3. &nbsp;
 4. &nbsp;
 5. &nbsp;
 
<br>
<br>

---
&nbsp;

### 🔴 RED Team
Hack your LAN to better protect it.
1. Run __\_D3PentestVM__
2. Login to the VM
> Username: kali  
> Password: kali  

<br>

> __ITSM__  
> Title: Protect the most important switch in your office
> Description: - RootBridge = CoreTAAS : Primary
>              - 2ndRootBridge = CoreBABA : Secondary
> Justification: To protect the network from layer 2 attacks.

<br>
<br>

---
&nbsp;

## 🔒 Secure Layer 2 Network
*Why should you buy an expensive switch?*

1. MAC Address Learning
2. MAC Address Filtering
3. MAC Address Forwarding
4. Layer 2 Loop Avoidance

<br>

&nbsp;
---
&nbsp;

### PortSec
*Ensure your devices don't get swapped.*
Guard the switchports so that it can't be replaced by hacking devices.

<br>

~~~
!@BABA
config t
 int fa0/6
  switchport mode access
  switchport port-security
  switchport port-security mac-address Sticky
  switchport port-security maximum 1
  switchport port-security violation shutdown
 int fa0/8
  switchport mode access
  switchport port-security
  switchport port-security mac-address Sticky
  switchport port-security maximum 1
  switchport port-security violation shutdown
  end
show port-security address
show int status err-disable
~~~

<br>

Make ports work again.

~~~
@CoreBABA
config t
 int fa0/6
  no switchport port-security
  shut
  no shut
 int fa0/8
  no switchport port-security
  shut
  no shut
  end
show int status err-disable
~~~

&nbsp;
---
&nbsp;

### Spanning Tree
*What switches hate the most?*

~~~
!@cmd
ping 10.#$34T#.1.100 -t
~~~

<br>

How to spot a healthy switch.
 - Lights are green - Super Healthy
 - Lights are amber - You are protected

<br>

__How to get fired immediately.__
~~~
!@CoreTAAS & CoreBABA
config t
 default int range fa0/10-12
 no spanning-tree vlan 1-999
 end
~~~

<br>

Save your network
~~~
config t
 spanning-tree vlan 1-999
 end
~~~

&nbsp;
---
&nbsp;
  
### `32768   vs   28672   vs   24576`

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

~~~
!@CoreTAAS
conf t
 spanning-tree vlan 1-1000 root primary
 end
~~~

<br>

~~~
!@CoreBABA
conf t
 spanning-tree vlan 1-1000 root secondary
 end
~~~

<br>
<br>

---
&nbsp;

### 📃 Full Script
<details>
<summary>Show Script</summary>
	
~~~
!@coreBaba
conf t
 hostname coreBaba-#$34T#
 enable secret pass
 service password-encryption
 no logging console
 no ip domain-lookup
 line cons 0
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int gi 0/1
  no shut
  no switchport
  ip add 10.#$34T#.#$34T#.4 255.255.255.0
 int vlan 1
  no shut
  ip add 10.#$34T#.1.4 255.255.255.0
  desc VLANMGMTDATA
 int vlan 10
  no shut
  ip add 10.#$34T#.10.4 255.255.255.0
  desc VLANMGMTWIFI
 int vlan 50
  no shut
  ip add 10.#$34T#.50.4 255.255.255.0
  desc VLANMGMTCCTV
 int vlan 100
  no shut
  ip add 10.#$34T#.100.4 255.255.255.0
  desc VLANMGMTVOICE
 end

!@switchport
conf t
 vlan 1
  name MGMTVLAN
 vlan 10
  name WIFIVLAN
 vlan 50
  name CCTVVLAN
 vlan 100
  name VOICEVLAN
 int fa 0/2
  switchport mode access
  switchport access vlan 10
 int fa 0/4
  switchport mode access
  switchport access vlan 10
 int fa 0/6
  switchport mode access
  switchport access vlan 50
 int fa 0/8
  switchport mode access
  switchport access vlan 50
 int fa 0/3
  switchport mode access
  switchport access vlan 100
 int fa 0/5
  switchport mode access
  switchport voice vlan 100
  switchport access vlan 1
 int fa 0/7
  switchport mode access
  switchport voice vlan 100
  switchport access vlan 1
 end

!@camera
conf t
 ip routing
 ip dhcp pool CAMERA6
  host 10.#$34T#.50.6 255.255.255.0
  client-identifier #camera6macadd#
 ip dhcp pool CAMERA8
  host 10.#$34T#.50.8 255.255.255.0
  client-identifier #camera8macadd#
 end
~~~

</details>

<br>
<br>

---
&nbsp;

### 💾 Save the configurations
~~~
!@CoreTAAS & CoreBABA
copy run start
~~~

<br>
<br>

---
&nbsp;

## 🔧 Configure CUCM
### 📠 Setup a mini call center

~~~
!@CUCM
conf t
 hostname CUCM-#$34T#
 enable secret pass
 service password-encryption
 no logging console
 no ip domain-lookup
 line cons 0
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int fa 0/0
  no shut
  ip add 10.#$34T#.100.8 255.255.255.0
 end
~~~

<br>
<br>

---
&nbsp;

### Know the jobs of a Call Manager

<br>

## ⚙️ 1. Analog Phones (RJ11)
*Why do companies still use Analog phones?*

<br>

~~~
!@CUCM
conf t
 dial-peer voice 1 pots
  destination-pattern #$34T#00
  port 0/0/0
 dial-peer voice 2 pots
  destination-pattern #$34T#01
  port 0/0/1
 dial-peer voice 3 pots
  destination-pattern #$34T#02
  port 0/0/2
 dial-peer voice 4 pots
  destination-pattern #$34T#03
  port 0/0/3
 end
~~~

<br>

Verify Functionality:

~~~
!@CUCM
show dial-peer voice summary
csim start #$34T#00
~~~

&nbsp;
---
&nbsp;

Modify the tone of the phone.
~~~
!@CUCM
conf t
 voice-port 0/0/0
  cptone dutch
  end
~~~

<br>
<br>

---
&nbsp;

## ⚙️ 2. IP Phones (RJ45) - Cisco Skinny Client Control Protocol (SCCP)
*What kind of phones do enterprise use?*

### Requirements to make IP Phones Operational
7.
6.
5.
4. T___:  S___:  S__:
3. IP Address
2. MAC Address
1. Power (PoE)

<br>
<br>

---
&nbsp;

~~~
!@CUCM
conf t
 no telephony-service
 telephony-service
  no auto assign
  no auto-reg-ephone
  max-ephones 5
  max-dn 20
  ip source-address 10.#$34T#.100.8 port 2000
  end
~~~

<br>

*Why 10.#$34T#.100.8? __TFTP__*

<br>

Ephone 1 MAC: #ephone1macadd#  
Ephone 2 MAC: #ephone1macadd#  

&nbsp;
---
&nbsp;

~~~
!@CUCM
conf t
 ephone-dn 1
  number #$34T#11
 ephone-dn 2
  number #$34T#22
 ephone-dn 3
  number #$34T#33
 ephone-dn 4
  number #$34T#44
 ephone-dn 5
  number #$34T#55
 ephone-dn 6
  number #$34T#66
 ephone-dn 7
  number #$34T#77
 ephone-dn 8
  number #$34T#88
 ephone-dn 9
  number #$34T#99
 ephone 1
  mac-address #ephone1macadd#
  type 8945
  button 1:1 2:2 3:3 4:4
 ephone 2
  mac-address #ephone2macadd#
  type 8945
  button 1:5 2:6 3:7 4:8
  end
~~~

<br>

> [!TIP]
> Still no numbers? Because IP Phones need to generate configuration files. __MANDATORY__

<br>

~~~
!@CUCM
conf t
 telephony-service
  create cnf-files
 !
 ephone 1
  restart
 ephone 2
  restart
  end
~~~

<br>

> [!NOTE]
> Depending on the ephone, __`create cnf-files`__ will need to be pasted twice.

<br>
<br>

---
&nbsp;

## ⚙️ 3. Video Calls
~~~
!@CUCM
conf t
 ephone 1
  video
  voice service voip
  h323
  call start slow
 ephone 2
  video
  voice service voip
  h323
  call start slow
end
~~~

<br>
<br>

---
&nbsp;

## ⚙️ 4. Allow Incoming & Outgoing Calls
~~~
!@CUCM
conf t
 voice service voip
 ip address trusted list
  ipv4 0.0.0.0 0.0.0.0
 end
~~~

<br>

~~~
!@CUCM
conf t
 dial-peer voice 11 Voip
  destination-pattern 11..
  session target ipv4:10.11.100.8
  codec g711ULAW
 dial-peer voice 12 Voip
  destination-pattern 12..
  session target ipv4:10.12.100.8
  codec g711ULAW
 dial-peer voice 21 Voip
  destination-pattern 21..
  session target ipv4:10.21.100.8
  codec g711ULAW
 dial-peer voice 22 Voip
  destination-pattern 22..
  session target ipv4:10.22.100.8
  codec g711ULAW
 dial-peer voice 31 Voip
  destination-pattern 31..
  session target ipv4:10.31.100.8
  codec g711ULAW
 dial-peer voice 32 Voip
  destination-pattern 32..
  session target ipv4:10.32.100.8
  codec g711ULAW
 dial-peer voice 41 Voip
  destination-pattern 41..
  session target ipv4:10.41.100.8
  codec g711ULAW
 dial-peer voice 42 Voip
  destination-pattern 42..
  session target ipv4:10.42.100.8
  codec g711ULAW
 dial-peer voice 51 Voip
  destination-pattern 51..
  session target ipv4:10.51.100.8
  codec g711ULAW
 dial-peer voice 52 Voip
  destination-pattern 52..
  session target ipv4:10.52.100.8
  codec g711ULAW
 dial-peer voice 61 Voip
  destination-pattern 61..
  session target ipv4:10.61.100.8
  codec g711ULAW
 dial-peer voice 62 Voip
  destination-pattern 62..
  session target ipv4:10.62.100.8
  codec g711ULAW
 dial-peer voice 71 Voip
  destination-pattern 71..
  session target ipv4:10.71.100.8
  codec g711ULAW
 dial-peer voice 72 Voip
  destination-pattern 72..
  session target ipv4:10.72.100.8
  codec g711ULAW
 dial-peer voice 81 Voip
  destination-pattern 81..
  session target ipv4:10.81.100.8
  codec g711ULAW
 dial-peer voice 82 Voip
  destination-pattern 82..
  session target ipv4:10.82.100.8
  codec g711ULAW
 dial-peer voice 91 Voip
  destination-pattern 91..
  session target ipv4:10.91.100.8
  codec g711ULAW
 dial-peer voice 92 Voip
  destination-pattern 92..
  session target ipv4:10.92.100.8
  codec g711ULAW
 end
~~~

<br>
<br>

---
&nbsp;

## ⚙️ 5. Interactive Voice Response System (IVRS)
*How do large call centers handle numerous calls?*

<br>

~~~
!@CUCM
config t
 dial-peer voice 69 voip
  service rivanaa out-bound
  destination-pattern #$34T#69
  session target ipv4:10.#$34T#.100.8
  incoming called-number #$34T#69
  dtmf-relay h245-alphanumeric
  codec g711ulaw
  no vad
 !
 telephony-service
  moh "flash:/en_bacd_music_on_hold.au"
 !
 application
  service rivanaa flash:app-b-acd-aa-3.0.0.2.tcl
   paramspace english index 1        
   param number-of-hunt-grps 2
   param dial-by-extension-option 8
   param handoff-string rivanaa
   param welcome-prompt flash:en_bacd_welcome.au
   paramspace english language en
   param call-retry-timer 15
   param service-name rivanqueue
   paramspace english location flash:
   param second-greeting-time 60
   param max-time-vm-retry 2
   param voice-mail 1234
   param max-time-call-retry 700
   param aa-pilot #$34T#69
  service rivanqueue flash:app-b-acd-3.0.0.2.tcl
   param queue-len 15
   param aa-hunt1 #$34T#00
   param aa-hunt2 #$34T#01
   param aa-hunt3 #$34T#22
   param aa-hunt4 #$34T#66
   param queue-manager-debugs 1
   param number-of-hunt-grps 4
   end
~~~

<br>

> [!WARNING]
Configurations for IVRS cannot be overwritten. In case of wrong configurations, paste the commands below to the call manager then repaste the correct IVRS configurations.

<br>

~~~
!@CUCM
config t
 application
  no service callqueue flash:app-b-acd-2.1.2.2.tcl
  no service rivanaa flash:app-b-acd-aa-2.1.2.2.tcl
  end
~~~

<br>
<br>

---
&nbsp;

Review the jobs of a call manager:
 1. &nbsp;
 2. &nbsp;
 3. &nbsp;
 4. &nbsp;
 5. &nbsp;
  
<br>
<br>

---
&nbsp;

### Requirements to make IP Phones Operational
7. A____
6. G71__  G72__
5. R__
4. TFTP:  SCCP:  SIP:
3. IP Address
2. MAC Address
1. Power (PoE)

<br>

## SPAN
~~~
!@CoreBABA (Serial)
conf t
 monitor session 1 source interface fa0/3,fa0/5,fa0/7
 monitor session 1 destination interface fa0/1,fa0/9
 end
~~~

<br>

__Remove SPAN__
~~~
!@CoreBABA (Serial)
conf t
 no monitor session 1 source interface fa0/3,fa0/5,fa0/7
 no monitor session 1 destination interface fa0/1,fa0/9
 end
~~~

&nbsp;
---
&nbsp;

## ☁️ Remote Access | [JUMPSERVER](https://www.jumpserver.com/)
### 🎯 Exercies 06: Attempt to establish a telnet session with the call manager

<br>

Is the device pingable?

~~~
@cmd
10.#$34T#.100.8
~~~

<br>
<br>

---
&nbsp;

### 📃 Full Script

<details>
<summary>Show Script</summary>
	
~~~
!@CUCM
conf t
 hostname CUCM-#$34T#
 enable secret pass
 service password-encryption
 no logging console
 no ip domain-lookup
 line cons 0
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int fa 0/0
  no shut
  ip add 10.#$34T#.100.8 255.255.255.0
 end

!@alog & ephone
conf t
 dial-peer voice 1 pots
  destination-pattern #$34T#00
  port 0/0/0
 dial-peer voice 2 pots
  destination-pattern #$34T#01
  port 0/0/1
 dial-peer voice 3 pots
  destination-pattern #$34T#02
  port 0/0/2
 dial-peer voice 4 pots
  destination-pattern #$34T#03
  port 0/0/3
 end

conf t
 no telephony-service
 telephony-service
  no auto assign
  no auto-reg-ephone
  max-ephones 5
  max-dn 20
  ip source-address 10.#$34T#.100.8 port 2000
  create cnf-files
 ephone-dn 1
  number #$34T#11
 ephone-dn 2
  number #$34T#22
 ephone-dn 3
  number #$34T#33
 ephone-dn 4
  number #$34T#44
 ephone-dn 5
  number #$34T#55
 ephone-dn 6
  number #$34T#66
 ephone-dn 7
  number #$34T#77
 ephone-dn 8
  number #$34T#88
 ephone-dn 9
  number #$34T#99
 ephone 1
  mac-address #ephone1macadd#
  type 8945
  button 1:1 2:2 3:3 4:4
  restart
 ephone 2
  mac-address #ephone2macadd#
  type 8945
  button 1:5 2:6 3:7 4:8
  restart
 end

!@video call
conf t
 ephone 1
  video
  voice service voip
  h323
  call start slow
 ephone 2
  video
  voice service voip
  h323
  call start slow
end

!@incoming and outgoing
conf t
 voice service voip
 ip address trusted list
 ipv4 0.0.0.0 0.0.0.0
 end

conf t
 dial-peer voice 11 Voip
  destination-pattern 11..
  session target ipv4:10.11.100.8
  codec g711ULAW
 dial-peer voice 12 Voip
  destination-pattern 12..
  session target ipv4:10.12.100.8
  codec g711ULAW
 dial-peer voice 21 Voip
  destination-pattern 21..
  session target ipv4:10.21.100.8
  codec g711ULAW
 dial-peer voice 22 Voip
  destination-pattern 22..
  session target ipv4:10.22.100.8
  codec g711ULAW
 dial-peer voice 31 Voip
  destination-pattern 31..
  session target ipv4:10.31.100.8
  codec g711ULAW
 dial-peer voice 32 Voip
  destination-pattern 32..
  session target ipv4:10.32.100.8
  codec g711ULAW
 dial-peer voice 41 Voip
  destination-pattern 41..
  session target ipv4:10.41.100.8
  codec g711ULAW
 dial-peer voice 42 Voip
  destination-pattern 42..
  session target ipv4:10.42.100.8
  codec g711ULAW
 dial-peer voice 51 Voip
  destination-pattern 51..
  session target ipv4:10.51.100.8
  codec g711ULAW
 dial-peer voice 52 Voip
  destination-pattern 52..
  session target ipv4:10.52.100.8
  codec g711ULAW
 dial-peer voice 61 Voip
  destination-pattern 61..
  session target ipv4:10.61.100.8
  codec g711ULAW
 dial-peer voice 62 Voip
  destination-pattern 62..
  session target ipv4:10.62.100.8
  codec g711ULAW
 dial-peer voice 71 Voip
  destination-pattern 71..
  session target ipv4:10.71.100.8
  codec g711ULAW
 dial-peer voice 72 Voip
  destination-pattern 72..
  session target ipv4:10.72.100.8
  codec g711ULAW
 dial-peer voice 81 Voip
  destination-pattern 81..
  session target ipv4:10.81.100.8
  codec g711ULAW
 dial-peer voice 82 Voip
  destination-pattern 82..
  session target ipv4:10.82.100.8
  codec g711ULAW
 dial-peer voice 91 Voip
  destination-pattern 91..
  session target ipv4:10.91.100.8
  codec g711ULAW
 dial-peer voice 92 Voip
  destination-pattern 92..
  session target ipv4:10.92.100.8
  codec g711ULAW
 end
 
!@IVRS
config t
 dial-peer voice 69 voip
  service rivanaa out-bound
  destination-pattern #$34T#69
  session target ipv4:10.#$34T#.100.8
  incoming called-number #$34T#69
  dtmf-relay h245-alphanumeric
  codec g711ulaw
  no vad
 !
 telephony-service
  moh "flash:/en_bacd_music_on_hold.au"
 !
 application
  service rivanaa flash:app-b-acd-aa-3.0.0.2.tcl
   paramspace english index 1        
   param number-of-hunt-grps 2
   param dial-by-extension-option 8
   param handoff-string rivanaa
   param welcome-prompt flash:en_bacd_welcome.au
   paramspace english language en
   param call-retry-timer 15
   param service-name rivanqueue
   paramspace english location flash:
   param second-greeting-time 60
   param max-time-vm-retry 2
   param voice-mail 1234
   param max-time-call-retry 700
   param aa-pilot #$34T#69
  service rivanqueue flash:app-b-acd-3.0.0.2.tcl
   param queue-len 15
   param aa-hunt1 #$34T#00
   param aa-hunt2 #$34T#01
   param aa-hunt3 #$34T#22
   param aa-hunt4 #$34T#66
   param queue-manager-debugs 1
   param number-of-hunt-grps 4
   end
~~~

</details>

<br>
<br>

---
&nbsp;

### 💾 Save the configurations
~~~
!@CUCM
copy run start
~~~

<br>
<br>

---
&nbsp;

## 🌐 Site Connectivity
*When to use UTP and Fibre Optic*

<br>

[IEEE Ethernet Standards](https://www.ccnaacademy.com/2018/09/ieee-ethernet-standards_16.html)

  | Name            | Speed | IEEE  |
  | ---             |  ---  |  ---  |
  | Ethernet        |       |       |
  | FastEthernet    |       |       |
  | GigEthernet     |       |       |
  | TenGigEthernet  |       |       |

<br>
<br>

---
&nbsp;

## 🔧 Configure EDGE
### 🏨 Establish connectivity to your enterprise.
*How to know if you are connected to PLDT? __SCN - `show cdp neighbor`__*

~~~
!@EDGE
show cdp neighbor
~~~

<br>
<br>

---
&nbsp;

~~~
!@EDGE
conf t
 hostname EDGE-#$34T#
 enable secret pass
 service password-encryption
 no logging cons
 no ip domain lookup
 line cons 0
  password pass
  login
  exec-timeout 0 0
  exit
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int gi 0/0/0
  no shut
  ip add 10.#$34T#.#$34T#.1 255.255.255.0
  desc INSIDE
 int gi 0/0/1
  no shut
  ip add 200.0.0.#$34T# 255.255.255.0
  desc OUTSIDE
 int loopback 0
  ip add #$34T#.0.0.1 255.255.255.255
  desc VIRTUALIP
  end
~~~

<br>
<br>

---
&nbsp;

### ⚙️ Configure routing protocols
~~~
!@EDGE
conf t
 ip routing
 ip route 10.11.0.0 255.255.0.0 200.0.0.11 254
 ip route 10.12.0.0 255.255.0.0 200.0.0.12 254
 ip route 10.21.0.0 255.255.0.0 200.0.0.21 254
 ip route 10.22.0.0 255.255.0.0 200.0.0.22 254
 ip route 10.31.0.0 255.255.0.0 200.0.0.31 254
 ip route 10.32.0.0 255.255.0.0 200.0.0.32 254
 ip route 10.41.0.0 255.255.0.0 200.0.0.41 254
 ip route 10.42.0.0 255.255.0.0 200.0.0.42 254
 ip route 10.51.0.0 255.255.0.0 200.0.0.51 254
 ip route 10.52.0.0 255.255.0.0 200.0.0.52 254
 ip route 10.61.0.0 255.255.0.0 200.0.0.61 254
 ip route 10.62.0.0 255.255.0.0 200.0.0.62 254
 ip route 10.71.0.0 255.255.0.0 200.0.0.71 254
 ip route 10.72.0.0 255.255.0.0 200.0.0.72 254
 ip route 10.81.0.0 255.255.0.0 200.0.0.81 254
 ip route 10.82.0.0 255.255.0.0 200.0.0.82 254
 ip route 10.91.0.0 255.255.0.0 200.0.0.81 254
 ip route 10.92.0.0 255.255.0.0 200.0.0.82 254
 ip route 10.#$34T#.0.0 255.255.0.0 10.#$34T#.#$34T#.4 253
 no ip route 10.#$34T#.0.0 255.255.0.0 200.0.0.#$34T# 254
 end
~~~

<br>

~~~
!@CUCM
conf t
 ip routing
 ip route 0.0.0.0 0.0.0.0 10.#$34T#.100.4 254
 end
~~~

<br>

~~~
!@CoreBABA
conf t
 ip route 0.0.0.0 0.0.0.0 10.#$34T#.#$34T#.1 254
 end
~~~

&nbsp;
---
&nbsp;

Verify: *How can you check the list of routes?  __SIR - `show ip route`__*

~~~
!@CoreBABA, CUCM, EDGE
show ip route
~~~

&nbsp;
---
&nbsp;

*How do you configure routes on windows?*

~~~
!@cmd
route add 10.0.0.0 mask 255.0.0.0 10.#$34T#.1.4
route add 200.0.0.0 mask 255.255.255.0 10.#$34T#.1.4
~~~

<br>
<br>

---
&nbsp;

### ⚙️ 2. OSPF ROUTING
*At what capacity do you want your devices to run?*

~~~
!@edge
conf t
router ospf 1
router-id #$34T#.0.0.1
network 200.0.0.0 0.0.0.255 area 0
network 10.#$34T#.#$34T#.0 0.0.0.255 area 0
network #$34T#.0.0.1 0.0.0.0 area 0
int gi 0/0/0
ip ospf network point-to-point
end
~~~

<br>

~~~
@coreBaba
conf t
router ospf 1
router-id 10.#$34T#.#$34T#.4
network 10.#$34T#.0.0 0.0.255.255 area 0
int gi0/1
ip ospf network point-to-point
~~~

<br>

~~~
@cucm
conf t
router ospf 1
router-id 10.#$34T#.100.8
network 10.#$34T#.100.0 0.0.0.255 area 0
end
~~~

&nbsp;
---
&nbsp;

*Verify: How to check if OSPF is working? <br>
  __SIP - `show ip protocols`__ <br>
  __SION - `show ip ospf neighbor`__ <br>
  __SIRO - `show ip route ospf`__* <br>

&nbsp;
---
&nbsp;

### Now that routing is in place, there's no need to jump to access CUCM.
Ping

~~~
!@cmd
ping 10.#$34T#.1.2                 CoreTAAS
ping 10.#$34T#.1.4                 CoreBABA
ping 10.#$34T#.100.8               CUCM
ping 10.#$34T#.#$34T#.1            EDGE
~~~

<br>
<br>

---
&nbsp;


### Dedicated Line vs Internet VPN

<br>
<br>

## 🧱 Setup a Firewall (CSR1000v)

<br>

__Ordinary Firewall vs NGFW__

<br>
<br>

### `fbi.gov`   vs   `neu.edu.ph`   vs   `dpwh.gov.ph`
- Threat Defense
- Intrusion Detection
- Open Ports: HTTP, HTTPS, SSH, DNS

<br>

__Setup CSR1000v__

~~~
conf t
 hostname FW-EDGE
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
  ip add 192.168.103.11 255.255.255.0
  no shut
 !
 username admin privilege 15 secret pass
 ip http server
 ip http secure-server
 ip http authentication local
 end
wr
~~~

<br>
<br>

### Wireless Deployment

