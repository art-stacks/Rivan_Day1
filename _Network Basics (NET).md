
<!-- Your monitor number = #$34T# -->


# 👋 Welcome to Rivan
*"There's no better teacher than experience"*


&nbsp;

## 📋 Prove what you are doing.
 - Create a Github account: https://github.com/

Import the repositories.
 - Rivan_Day1 : https://github.com/art-stacks/Rivan_Day1
 - RivanCorp_CNETPLUS : https://github.com/rivancorp/cnetplus


<br>
<br>

---
&nbsp;


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


# 💻 Build your network. 


<br>
<br>

---
&nbsp;


## 🧱 Hierarchical Network Design
  *What is the most important part of a network? __The Core__*

<br>

Most common kinds of network architectures.
 - SOHO   
 - 2-tier 
 - 3-tier           
 - Spine-leaf    

<br>

CORE Layer (__CoreTAAS__ & __CoreBABA__) - High Speed and Availability
  > [!NOTE]
  >*"A Network Engineer MUST avoid a single point of failure.
   __Always have a backup.__"*


<br>
<br>

---
&nbsp;


## 🔌 Wired and wireless network.

<br>

> [!NOTE]
> A network must be Flexible. Reliable. __AVAILABLE__.


<br>


### 📶 PLDT AP vs Wireless Controller & Autonomous AP

<br>

Wifi Mesh
 - Wired Backhaul
 - Wireless Backhaul

<br>

Wifi standards | [IEEE (Institute of Electrical and Electronics Engineers)](https://standards.ieee.org/beyond-standards/the-evolution-of-wi-fi-technology-and-standards/)

<br>

| Gen    | IEEE     | Frequency  |
| ---    | ---      | ---        |
| Wifi 4 | 802.11n  | 2.4/5GHz   |
| Wifi 5 | 802.11ac | 5GHz       |
| WiFi 6 | 802.11ax | 2.4/5/6GHz |
| WiFi 7 | 802.11be | 2.4/5/6GHz |


<br>
<br>

---
&nbsp;


## 🔍 Implement security solutions.
*What is more valuable than gold? __Data__*

<br>

Network security infrastructure
 - NGFW, UTM, IDS
 - Security Policies
     - Windows Local Security Policy
 - Surveillance
     - IP Cameras (__CAM6__ & __CAM8__)

<br>
<br>

---
&nbsp;


## 📠 Enterprise Communication
*How often are meetings conducted in your work place?*

<br>

Cisco Unified Call Manager | [Unified Communications and Collaboration.]
  - POTS (__Analog__)
  - VOIP (__ePhone__)


<br>
<br>

---
&nbsp;


## 🌐 Internet Connectivity
*When to use UTP and Fibre Optic*

<br>

[IEEE Ethernet Standards](https://www.ccnaacademy.com/2018/09/ieee-ethernet-standards_16.html)

  | Name            | Speed   | F - IEEE - U |
  | ---             |  ---    |  ---         |
  | Ethernet        | 10Mbps  | 802.3i       |
  | FastEthernet    | 100Mbps | 802.3u       |
  | GigEthernet     | 1Gbps   | .3z / .3ab   |
  | TenGigEthernet  | 10Gbps  | .ae / .an    |

<br>

  - RJ45 Jack
  - SFP (Small Form-factor Pluggable)

<br>

  | Copper                                           | Single-mode fiber                    |
  | ---                                              | ---                                  |
  | Conductor, Bedding, Sheathing                    | Core, Cladding, Coating              |
  | Affected by electrical and magnetic interference | Comprised of insulated glass strands |

<br>
<br>

# 🔧 Configure the Network
*How can you tell if a device is expensive? It has a __Console Port__*

<br>

Serial Cable
  - VGA, USB
  - Ugreen


<br>
<br>

---
&nbsp;


## 🔧 Configure CoreTAAS
### ⚙️ Initial configurations

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
  name VIDEOVLAN
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
  desc VIDEO-VLAN
 int vlan 100
  no shut
  ip add 10.#$34T#.100.2 255.255.255.0
  desc VOICE-VLAN
 end
~~~


<br>
<br>

---
&nbsp;


## 🔧 Configure CoreBABA
Know the jobs of a Layer 3 Switch

### ⚙️ 1. __POE__
> [!NOTE]
> If you need PoE functionality on a non-PoE switch, use a PoE injector.


<br>
<br>

---
&nbsp;


### ⚙️ 2. SVI (Switch Virtual Interface)
~~~
!@CoreBABA
conf t
 hostname CoreBABA-#$34T#
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
 int vlan 1
  no shut
  ip add 10.#$34T#.1.4 255.255.255.0
  desc DEFAULT-SVI
 int vlan 10
  no shut
  ip add 10.#$34T#.10.4 255.255.255.0
  desc WIRELESS-SVI
 int vlan 50
  no shut
  ip add 10.#$34T#.50.4 255.255.255.0
  desc VIDEO-SVI
 int vlan 100
  no shut
  ip add 10.#$34T#.100.4 255.255.255.0
  desc VOICE-SVI
 end
~~~


<br>
<br>

---
&nbsp;


### ⚙️ 3. DHCP / BOOTPS & BOOTPC

| Network     | DHCP Device |
| :---:       |     ---     |
| SOHO        | Router      |
|             |             |
| Enterprise                |
| Medium Biz  | Firewall    |
| Large Biz   | Core Switch |

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
 ip dhcp pool POOLVIDEO
  network 10.#$34T#.50.0 255.255.255.0
  default-router 10.#$34T#.50.4
  domain-name VIDEODATA.COM
  dns-server 10.#$34T#.1.10
 ip dhcp pool POOLVOICE
  network 10.#$34T#.100.0 255.255.255.0
  default-router 10.#$34T#.100.4
  domain-name VOICEDATA.COM
  dns-server 10.#$34T#.1.10
  option 150 ip 10.#$34T#.100.8
  end
~~~


&nbsp;
---
&nbsp;


DHCP (Dynamic Host Configuration Protocol)
                            
| Option              |    Value    |
| ---                 |    :---:    |
| Address Subnet Mask |      1      |
| Default Gateway     |      3      |
| DNS Server          |      6      |
| Domain Name         |     15      |
| Domain Controller   |     43      |
| Lease Time          |     51      |
| Client Identifier   |     61      |
| TFTP Server         |    150      |


<br>
<br>

---
&nbsp;


### ⚙️ 4. VLAN Creation & VLAN Management
~~~
!@CoreBABA
show vlan brief
~~~


&nbsp;
---
&nbsp;


Just because there's an SVI doesn't mean there's a VLAN.

~~~
!@CoreBABA
conf t
 vlan 10
  name WIRELESS-VLAN
 vlan 50
  name VIDEO-VLAN
 vlan 100
  name VOICE-VLAN
  end
~~~


&nbsp;
---
&nbsp;


Place Switchports in their correct VLAN.

~~~
!@CoreTAAS
conf t
 int fa0/1
  switchport mode access
  switchport access vlan 10
 int fa0/2
  switchport mode access
  switchport access vlan 10
 int fa0/3
  switchport mode access
  switchport access vlan 50
 int fa0/4
  switchport mode access
  switchport access vlan 50
 int fa0/5
  switchport mode access
  switchport access vlan 1
  switchport voice vlan 100
  mls qos trust device cisco-phone
  end
show vlan brief
~~~

~~~
!@CoreBABA
conf t
 int fa0/1
  switchport mode access
  switchport access vlan 1
 int fa0/2
  switchport mode access
  switchport access vlan 10
 int fa0/4
  switchport mode access
  switchport access vlan 50
 int fa0/5
  switchport mode access
  switchport access vlan 1
  switchport voice vlan 100
  mls qos trust device cisco-phone
 int fa0/6
  switchport mode access
  switchport access vlan 100
  end
show vlan brief
~~~


<br>
<br>

---
&nbsp;


### ACCESS VS TRUNK
~~~
!@CoreTAAS, CoreBABA
conf t
 int range fa0/8-10
  channel-group 1 mode active
  channel-protocol lacp
 int po1
  switchport trunk encaps dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
  end
show int trunk
show int po1 | inc BW
!
~~~


<br>


__L3 Etherchannel__
~~~
!@CoreTAAS
conf t
 int range fa0/11-12
  no switchport
  channel-group 10 mode passive
  channel-protocol lacp
 int po10
  no switchport
  no shut
  ip add 10.#$34T#.#$34T#.2  255.255.255.252
  end
show ip int br
~~~

~~~
!@CoreBABA
conf t
 int range fa0/11-12
  no switchport
  channel-group 10 mode passive
  channel-protocol lacp
 int po10
  no switchport
  no shut
  ip add 10.#$34T#.#$34T#.6  255.255.255.252
  end
show ip int br
~~~


<br>
<br>

---
&nbsp;


## ⚙️ 5. MAC Learning & MAC Reservation
~~~
!@CoreTAAS,CoreBABA
show mac address-table
~~~


&nbsp;
---
&nbsp;


| Camera         | MAC Address      |
| ---            | ---              |
| Camera fa0/6   | #camera6macadd#  |
| Camera fa0/8   | #camera8macadd#  |


&nbsp;
---
&nbsp;


Assign a specific IP address to a device.

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


&nbsp;
---
&nbsp;


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


### 📃 Full Script
<details>
<summary>Show Script</summary>
	
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
  name VIDEOVLAN
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
  desc VIDEO-VLAN
 int vlan 100
  no shut
  ip add 10.#$34T#.100.2 255.255.255.0
  desc VOICE-VLAN
 !
 int fa0/1
  switchport mode access
  switchport access vlan 10
 int fa0/2
  switchport mode access
  switchport access vlan 10
 int fa0/3
  switchport mode access
  switchport access vlan 50
 int fa0/4
  switchport mode access
  switchport access vlan 50
 int fa0/5
  switchport mode access
  switchport access vlan 1
  switchport voice vlan 100
  mls qos trust device cisco-phone
 int range fa0/8-10
  channel-group 1 mode active
  channel-protocol lacp
 int range fa0/11-12
  no switchport
  channel-group 10 mode passive
  channel-protocol lacp
 int po10
  no switchport
  no shut
  ip add 10.#$34T#.#$34T#.2  255.255.255.252
 int po1
  switchport trunk encaps dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
 !
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
 ip dhcp pool POOLVIDEO
  network 10.#$34T#.50.0 255.255.255.0
  default-router 10.#$34T#.50.4
  domain-name VIDEODATA.COM
  dns-server 10.#$34T#.1.10
 ip dhcp pool POOLVOICE
  network 10.#$34T#.100.0 255.255.255.0
  default-router 10.#$34T#.100.4
  domain-name VOICEDATA.COM
  dns-server 10.#$34T#.1.10
  option 150 ip 10.#$34T#.100.8
  end
~~~

~~~
!@CoreBABA
conf t
 hostname CoreBABA-#$34T#
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
  name WIRELESS-VLAN
 vlan 50
  name VIDEO-VLAN
 vlan 100
  name VOICE-VLAN
 int vlan 1
  no shut
  ip add 10.#$34T#.1.4 255.255.255.0
  desc DEFAULT-SVI
 int vlan 10
  no shut
  ip add 10.#$34T#.10.4 255.255.255.0
  desc WIRELESS-SVI
 int vlan 50
  no shut
  ip add 10.#$34T#.50.4 255.255.255.0
  desc VIDEO-SVI
 int vlan 100
  no shut
  ip add 10.#$34T#.100.4 255.255.255.0
  desc VOICE-SVI
 int fa0/1
  switchport mode access
  switchport access vlan 1
 int fa0/2
  switchport mode access
  switchport access vlan 10
 int fa0/4
  switchport mode access
  switchport access vlan 50
 int fa0/5
  switchport mode access
  switchport access vlan 1
  switchport voice vlan 100
  mls qos trust device cisco-phone
 int fa0/6
  switchport mode access
  switchport access vlan 100
 int range fa0/8-10
  channel-group 1 mode active
  channel-protocol lacp
 int range fa0/11-12
  no switchport
  channel-group 10 mode passive
  channel-protocol lacp
 int po10
  no switchport
  no shut
  ip add 10.#$34T#.#$34T#.6  255.255.255.252
 int po1
  switchport trunk encaps dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
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

Reuirements for IP Phones to work:
1. &nbsp;
2. &nbsp;
3. &nbsp;
4. &nbsp;
5. &nbsp;
6. &nbsp;
7. &nbsp;


<br>
<br>

---
&nbsp;


## ⚙️ 1. Analog Phones
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


<br>
<br>

---
&nbsp;


## ⚙️ 2. IP Phones - Cisco Skinny Client Control Protocol (SCCP)
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


&nbsp;
---
&nbsp;


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
 no dial-peer voice #$34T# Voip
 end
~~~


<br>
<br>

---
&nbsp;


## ⚙️ 5. Interactive Voice Response System (IVRS)

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

!@anlog & ephone
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
 no dial-peer voice #$34T# Voip
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


## 🌐 Site Connectivity
### 🏨 Establish connectivity to your enterprise.

Fortigate Port = #P0RT#


&nbsp;
---
&nbsp;


*What is the maximum distance of a UTP cable? 100m?*

Network Scopes
  - 🏠 LAN                  Local Area Network
  - 🌎 WAN                  Wide Area Network

<br>

PLDT Home vs PLDT Enterprise
  - 🌃 MAN                  Metropolitan Area Network
                         PLDT Enterprise Metro Ethernet

<br>

Transport technologies
  - Leased Line
  - SDWAN
  - MPLS VPLS            (Pseudowire, L3 & L2)
  - VPN                  (EVPN)


<br>
<br>


### EDGE vs Firewall

Jobs of an EDGE Router:  
1. &nbsp;
2. &nbsp;
3. &nbsp;
4. &nbsp;
5. &nbsp;

<br>

Jobs of a Firewall:  
1. &nbsp;
2. &nbsp;
3. &nbsp;
4. &nbsp;
5. &nbsp;


<br>

~~~
!@FW-EDGE
config system global
 set hostname FW-EDGE-#$34T#
 end
config system admin
 edit rivan
  set accprofile super_admin
  set vdom root
  set password pass
  next
 edit admin
  set accprofile super_admin
  set vdom root
  set password pass
  end
show system admin
~~~

~~~
!@FW-EDGE
config system virtual-switch
 edit #P0RT#
  config port
   delete #P0RT#1
   delete #P0RT#2
   delete #P0RT#3
   delete #P0RT#4
   end
  end
config system interface
 edit TAAS-LACP
  set type aggregate
  set member #P0RT#1 #P0RT#2
  set status up
  set lacp-mode active
  set vdom root
  set ip 10.#$34T#.#$34T#.1/30
  set allowaccess ping https http ssh telnet
  next
 edit BABA-LACP
  set type aggregate
  set member #P0RT#3 #P0RT#4
  set status up
  set lacp-mode active
  set vdom root
  set ip 10.#$34T#.#$34T#.5/30
  set allowaccess ping https http ssh telnet
  next
 edit wan1
  set vdom root
  set mode static
  set type physical
  set ip 200.0.0.#$34T# 255.255.255.0
  set allowaccess ping https http ssh telnet
  set status up
  next
 edit loopback0
  set vdom root
  set type loopback
  set status up
  set ip #$34T#.0.0.1 255.255.255.255
  set allowaccess ping https http ssh telnet
  end
~~~


Verification Commands
~~~
!@FW-EDGE
diagnose netlink aggregate name TAAS-LACP
diagnose netlink aggregate name BABA-LACP
~~~


<br>
<br>

---
&nbsp;


### ⚙️ OSPF ROUTING
~~~
!@FW-EDGE
config router ospf
 set router-id #$34T#.0.0.1
 config area
  edit 0.0.0.0
  end
 config network
  edit 1
   set prefix 10.#$34T#.#$34T#.0/30
   set area 0.0.0.0
   next
  edit 2
   set prefix 10.#$34T#.#$34T#.4/30
   set area 0.0.0.0
   next
  edit 3
   set prefix #$34T#.0.0.1/32
   set area 0.0.0.0
   next
  edit 4
   set prefix 200.0.0.0/24
   set area 0.0.0.0
   end
 config ospf-interface
  edit FW-TAAS
   set interface TAAS-LACP
   set status enable
   set network-type point-to-point
   next
  edit FW-BABA
   set interface BABA-LACP
   set status enable
   set network-type point-to-point
   end
  end
get router info ospf neighbor
get router info ospf status
get router info routing-table all
~~~

<br>

~~~
!@CoreTAAS
conf t
 ip routing
 router ospf 1
  router-id 10.#$34T#.#$34T#.2
  network 10.#$34T#.0.0 0.0.255.255 area 0
 int po1
  ip ospf network point-to-point
  end
~~~

<br>

~~~
!@CoreBABA
conf t
 ip routing
 router ospf 1
  router-id 10.#$34T#.#$34T#.4
  network 10.#$34T#.0.0 0.0.255.255 area 0
 int po1
  ip ospf network point-to-point
  end
~~~

<br>

~~~
!@CUCM
conf t
 router ospf 1
  router-id 10.#$34T#.100.8
  network 10.#$34T#.100.0 0.0.0.255 area 0
  end
~~~


&nbsp;
---
&nbsp;


### Now that routing is in place, there's no need to jump to access CUCM.
~~~
!@cmd
ping 10.#$34T#.1.2                 CoreTAAS
ping 10.#$34T#.1.4                 CoreBABA
ping 10.#$34T#.100.8               CUCM
ping 10.#$34T#.#$34T#.1            EDGE
~~~

~~~
!@cmd
nmap -v 10.#$34T#.1.2 
nmap -v 10.#$34T#.1.4
nmap -v 10.#$34T#.100.8
nmap -v 10.#$34T#.#$34T#.1
~~~


<br>
<br>

---
&nbsp;


### 🧱 FIREWALL POLICY

~~~
!@FW-EDGE
config system zone
 edit LAN-ZONE
  set intrazone allow
  set interface TAAS-LACP BABA-LACP
  end
config firewall policy
 edit 1
  set name INSIDE-TO-OUTSIDE
  set srcintf LAN-ZONE
  set dstintf wan1
  set srcaddr all
  set dstaddr all
  set action accept 
  set schedule always
  set service ALL
  set nat enable
  next
 edit 2
  set name OUTSIDE-TO-INSIDE
  set srcintf wan1
  set dstintf LAN-ZONE
  set srcaddr all
  set dstaddr all
  set action accept 
  set schedule always
  set service ALL
  set nat disable
  end
show firewall policy
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


# 🎯 REVIEW
What are the jobs of a switch?
 1. &nbsp;
 2. &nbsp;
 3. &nbsp;
 4. &nbsp;
 5. &nbsp;


&nbsp;
---
&nbsp;


What are the jobs of a call manager/voice gateway?
 1. &nbsp;
 2. &nbsp;
 3. &nbsp;
 4. &nbsp;
 5. &nbsp;


&nbsp;
---
&nbsp;

 
What are the jobs of a router?
 1. &nbsp;
 2. &nbsp;
 3. &nbsp;
 4. &nbsp;
 5. &nbsp;


&nbsp;
---
&nbsp;

 
What are the jobs of a firewall?
 1. &nbsp;
 2. &nbsp;
 3. &nbsp;
 4. &nbsp;
 5. &nbsp;


<br>
<br>

---
&nbsp;


## Network Services
- Deploy WinServer VM
- DNS
- Web Server
- IIS

<br>

| NetAdapter | VNIC    |
| ---        | ---     |
| 1          | NAT     |
| 2          | VMNet 2 |

<br>

~~~
!@powershell-ise
set-netfirewallprofile -name private,public,domain -enabled false
rename-computer snoopy#$34T#
ncpa.cpl
~~~
