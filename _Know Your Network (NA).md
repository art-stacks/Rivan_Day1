
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


# 💻 Build your network. 


<br>
<br>


## 🔧 Configure CoreTAAS
### ⚙️ 1. Initial configurations

~~~
!@CoreTAAS
conf t
 hostname CoreTAAS-#$34T#
 enable password pass
 no logging cons
 no ip domain lookup
 line cons 0
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
  end
show run | s line
!
~~~

<br>
<br>

__User Accounts__
~~~
!@CoreTAAS
conf t
 username admin privilege 15 password pass
 username rivan privilege 15 password C1sc0123
 username user1 privilege 1  password pass
 !
 line cons 0
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login local
  exec-timeout 0 0
 end
show run | s username
!
~~~

<br>
<br>

__Secure Passwords__
~~~
!@CoreTAAS
conf t
 username ___ privilege 15 secret pass
 end
show run | s username
!
~~~

<br>

~~~
!@CoreTAAS
conf t
 service password-encryption
 end
~~~


&nbsp;
---
&nbsp;


__First 5 - H.E.S.No__

~~~
!@CoreTAAS
conf t
 Hostname CoreTAAS-#$34T#
 Enable secret pass
 Service password-encryption
 No logging console
 No ip domain lookup
 end
~~~


&nbsp;
---
&nbsp;


### ⚙️ 2. Protect Console & Remote Access
~~~
!@CoreTAAS
conf t
 line cons 0
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
  end
~~~


&nbsp;
---
&nbsp;


### ⚙️ 3. Create SVI (Switch Virtual Interface)
~~~
!@CoreTAAS
conf t
 int vlan 1
  ip add 10.#$34T#.1.2 255.255.255.0
  description DEFAULT-VLAN
  end
~~~

<br>

Verify: How to check IP addresses? __SIIB - `show ip interface brief`__
~~~
!@CoreTAAS
show ip int brief
~~~

<br>

By default, 
  Switchports = On 
  SVIs = off

  
<br>
<br>

---
&nbsp;


### 🎯 Exercise 02: Turn on VLAN 1

~~~
!@CoreTAAS
conf t
 int vlan 1
  no shut
  end
show ip int br
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 03: Add the other SVIs

Task:
 1. CoreTAAS must have the following SVIs
   - VLAN 1
       - IP address: 10.#$34T#.1.2
       - Description: DEFAULT-VLAN
       - Status: UP

   - VLAN 10
     - IP address: 10.#$34T#.10.2
     - Description: WIFI-VLAN
     - Status: UP

   - VLAN 50
     - IP address: 10.#$34T#.50.2
     - Description: CCTV-VLAN
     - Status: UP

   - VLAN 100
     - IP address: 10.#$34T#.100.2
     - Description: VOICE-VLAN
     - Status: UP

<br>

~~~
!@CoreTAAS
conf t
 int vlan 1
  ip add 10.#$34T#.1.2 255.255.255.0
  description DEFAULT-VLAN
  no shut
  exit
 int vlan __
  ip add __.__.__.__ 255.255.255.0
  __  __
  __  __
  exit
 int vlan __
  ip add __.__.__.__ 255.255.255.0
  __  __
  __  __
  exit
 int vlan __
  ip add __.__.__.__ 255.255.255.0
  __  __
  __  __
  exit
 int vlan __
  ip add __.__.__.__ 255.255.255.0
  __  __
  __  __
  end
~~~

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
</details>


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
<br>

---
&nbsp;


### ⚙️ 2. SVI (Switch Virtual Interface)

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


&nbsp;
---
&nbsp;


Verify Connectivity: 

~~~
!@cmd
ping 10.#$34T#.1.4
~~~


<br>
<br>

---
&nbsp;


### ⚙️ 3. DHCP / BOOTPS & BOOTPC
*In a network, which device should be a DHCP Server? __It depends.__*

| Network     | DHCP Device |
| :---:       |     ---     |
| SOHO        |             |
|             |             |
| Enterprise                |
| Medium Biz  |             |
| Large Biz   |             |

<br>

Can Windows be a DHCP Server? Yes, Server Manager.

~~~
!@CoreBABA
conf t
 ip dhcp excluded-address 10.#$34T#.1.1 10.#$34T#.1.100
 ip dhcp excluded-address 10.#$34T#.10.1 10.#$34T#.10.100
 ip dhcp excluded-address 10.#$34T#.50.1 10.#$34T#.50.100
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
  option 43 ip 10.#$34T#.10.#$34T#
 ip dhcp pool POOLCCTV
  network 10.#$34T#.50.0 255.255.255.0
  default-router 10.#$34T#.50.4
  domain-name CCTVDATA.COM
  dns-server 10.#$34T#.1.10
  exit
~~~


<br>
<br>

---
&nbsp;

### 🎯 Exercise 04: Configure CoreBABA as a DHCP server for VoIP Devices.

Task:
1. CoreBABA must act as a DHCP Server for devices in VLAN 100 with the following settings
    - The first 100 IPs must be reserved.
    - The DHCP pool name must be 'POOLVOICE'
    - The default gateway must be CoreBABA.
    - The domain name must be 'VOICEDATA.COM'
    - The DNS Server must be your Windows Server.
    - Set CUCM as the TFTP server for DHCP clients.
    - Set a lease time of 5 days.

~~~
!@CoreBABA
conf t
 ip dhcp excluded-address __.__.__.__  __.__.__.__
 ip dhcp pool ______
  network 10.#$34T#.100.0 255.255.255.0
  default-______  ______
  ______  ______
  ______  
  option ___  ip 10.#$34T#.__.__
  lease 5 0 0
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

~~~
!@CoreBABA
conf t
 vlan 1
  name MGMTVLAN
 vlan 10
  name WIFIVLAN
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
 int fa 0/3
  switchport mode access
  switchport access vlan 100
 int fa 0/5
  switchport mode access
  switchport voice vlan 100
  switchport access vlan 1
  mls qos trust device cisco-phone
 int fa 0/7
  switchport mode access
  switchport voice vlan 100
  switchport access vlan 1
  mls qos trust device cisco-phone
 end
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 05: Place Cameras to their correct VLANs based on the topology.

Task:
 1. Create VLAN 50 and name it 'CCTVVLAN'
 2. Place IP cameras to their correct VLAN.

~~~
!@CoreBABA
conf t
 vlan ____
  ____  ____
  exit
 int ____
  ____  ____  access
  ____  access ____  ____
  exit
 int ____
  ____  ____  access
  ____  access ____  ____
  end
~~~


<br>
<br>

---
&nbsp;


## ⚙️ 5. MAC Learning & MAC Reservation
*What does it mean to say Layer 2 in networking?*

<br>

How to view the MAC addresses learned by the Switch? __SMAC - `show mac address-table`__

~~~
!@CoreBABA
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


Verify DHCP: __SIDB - `show ip dhcp bindings`__

~~~
!@CoreBABA
show ip dhcp bindings
~~~


<br>
<br>

---
&nbsp;


### ⚖️ Ensure Availability through redundancy and loadbalance

~~~
!@coreBaba, coreTaas
conf t
 int range fa0/10-12
  switchport trunk encapsulation dot1q
  switchport mode trunk
  channel-group 1 mode active
  channel-protocol lacp
  end
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

!@dhcp
conf t
 ip dhcp excluded-add 10.#$34T#.1.1 10.#$34T#.1.100
 ip dhcp excluded-add 10.#$34T#.10.1 10.#$34T#.10.100
 ip dhcp excluded-add 10.#$34T#.50.1 10.#$34T#.50.100
 ip dhcp excluded-add 10.#$34T#.100.1 10.#$34T#.100.100
 ip dhcp pool POOLDATA
  network 10.#$34T#.1.0 255.255.255.0
  default-router 10.#$34T#.1.4
  domain-name MGMTDATA.COM
  dns-server 10.#$34T#.1.10
  exit
 ip dhcp pool POOLWIFI
  network 10.#$34T#.10.0 255.255.255.0
  default-router 10.#$34T#.10.4
  domain-name WIFIDATA.COM
  dns-server 10.#$34T#.1.10
  option 43 ip 10.#$34T#.10.#$34T#
  exit
 ip dhcp pool POOLCCTV
  network 10.#$34T#.50.0 255.255.255.0
  default-router 10.#$34T#.50.4
  domain-name CCTVDATA.COM
  dns-server 10.#$34T#.1.10
  exit
 ip dhcp pool POOLVOICE
  network 10.#$34T#.100.0 255.255.255.0
  default-router 10.#$34T#.100.4
  domain-name VOICEDATA.COM
  dns-server 10.#$34T#.1.10
  option 150 ip 10.#$34T#.100.8
  exit

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
  mls qos trust device cisco-phone
 int fa 0/7
  switchport mode access
  switchport voice vlan 100
  switchport access vlan 1
  mls qos trust device cisco-phone
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


### ☁️ Remote Access
Access the CoreSwitches without the console cable.
~~~
@cmd
ping 10.#$34T#.1.2
ping 10.#$34T#.1.4
~~~


&nbsp;
---
&nbsp;


When a device is pingable you can scan it.
~~~
@cmd
nmap -v 10.#$34T#.1.2
nmap -v 10.#$34T#.1.4
~~~

Is port 23 open?

Enter port 23 via __SecureCRT__


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

## ⚙️ 1. Analog Phones
*Why do companies still use Analog phones? Mobile vs Analog*

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
show dial-peer voice summary     !SDVS
csim start #$34T#00
~~~


<br>
<br>

---
&nbsp;


## ⚙️ 2. IP Phones - Cisco Skinny Client Control Protocol (SCCP)
*What kind of phones do enterprise use?*

<br>

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
*How do large call centers handle numerous calls?*

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


## 🔧 Configure EDGE
### 🏨 Establish connectivity to your enterprise.
*How do you gain access to the internet?*

<br>


*How to know if you are connected to PLDT? __SCN - `show cdp neighbor`__*

~~~
!@EDGE
show cdp neighbor
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 07: Review of First 5 (HESNo)
Task:
 1. Set the hostname to EDGE-#$34T#
 2. Protect access to the global configuration mode using a password that is hashed with md5 encryption. 
    The password must be 'pass'
 3. Make sure any plain text passwords are encrypted in the configuration file.
 4. The device must not be allowed to send logs on the console.
 5. The device must not assume non-cisco commands are domain names.

<br>

~~~
!@EDGE
conf t
 ____  ____
 enable  ____  ____
 service  ____
 no ____  ____  ____
 no ip ____  ____
 end
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 08: Review of Protecting the console and terminal.

Task:
Protect Console
 1. Set a password on the console.
    The password must be 'pass'
 2. When connecting to the console, the device must require only a password.
 3. If a user is inactive for 30 minutes and 30 seconds, the session must end.

<br>

Protect Remote Access
 1. Set a password on the first 15 virtual teletype lines.
    The password must be 'pass'
 2. When connecting to the console, the device must require only a password.
 3. If a user is inactive for 12 hours, the session must end.

<br>

~~~
!@EDGE
conf t
 line ____  __
  ____  ____
  ____
  ____  __  __
  exit
 line ____  __
  ____  ____
  ____
  ____  __  __
  end
~~~


<br>
<br>

---
&nbsp;


### ⚙️ IP addressing
~~~
!@EDGE
conf t
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
What are the jobs of a router?
 1. &nbsp;
 2. &nbsp;
 3. &nbsp;
 4. &nbsp;
 5. &nbsp;
 6. &nbsp;


<br>
<br>

---
&nbsp;


### ⚙️ 1. Static Routing
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
 ip route 10.#$34T#.0.0 255.255.0.0 10.#$34T#.#$34T#.4 254
 !
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

Scan

~~~
!@cmd
nmap -v 10.#$34T#.1.2 
nmap -v 10.#$34T#.1.4
nmap -v 10.#$34T#.100.8
nmap -v 10.#$34T#.#$34T#.1
~~~

<br>

Telnet via SecureCRT

<br>
<br>

---
&nbsp;

# 🎯 REVIEW

Must know show commands: 
| Abbreviated   | Full Command |
| ---           | ---          |
| SS            |              |
| SR            |              |
| CRS           |              |
| SIIB          |              |
| SVB           |              |
| SIDB          |              |
| SMAC          |              |
| SDVS          |              |
| SIP           |              |
| SIR           |              |
| SION          |              |
| SIRO          |              |

&nbsp;
---
&nbsp;

First 5 commands:
| Abbreviated   | Full Command |
| ---           | ---          |
| H             |              |
| E             |              |
| S             |              |
| No            |              |
| No            |              |


&nbsp;
---
&nbsp;


Commands to protect console, in order:

~~~
!@Cisco
config t
~~~


&nbsp;
---
&nbsp;


Commands to protect remote access, in order:

~~~
!@Cisco
config t
~~~


&nbsp;
---
&nbsp;


Commands to configure DHCP, in order:

~~~
!@Cisco
config t
 ip dhcp excluded-address 10.0.1.1 10.0.0.100
 __ ____ ____ mypool
  ____ 10.0.1.0 255.255.255.0
  ____ 10.0.1.1
  ____ mypool.com
  ____ 10.0.1.10
~~~


&nbsp;
---
&nbsp;


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


<br>
<br>

---
&nbsp;


## Python & JSON CrashCourse

### Lab Setup

CSR1000v:
  Name: UTM-PH
  
  | NetAdapter   |        |
  | ---          | ---    |
  | NetAdapter   | NAT    |
  | NetAdapter 2 | VMNet2 |
  | NetAdapter 3 | VMNet3 |


TinyCore (yvm.ova):
  Name: BLDG-PH
  
  | NetAdapter   |                    |
  | ---          | ---                |
  | NetAdapter   | VMNet3             |


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
<br>

---
&nbsp;


## JSON (JavaScript Object Notation)
- Data Representation Format
- Lightweight and Easy to Read/Write
- Easily Integrate with most languages

### Data Types

| Type                | JSON          |
| ---                 | ---           |
| "Cisco"             | Strings       |
| 10                  | Integer       |
| 10.0                | Float         |
| True                | Boolean (t/f) |
| [1,"Router"]        | Array         |
| {"vendor": "cisco"} | Object        |


<br>
<br>

---
&nbsp;


### 🎯 Exercise 09:


__4F.json__
~~~json
{
    "4F-Devices": {
        "Router": {
            "Vendor": ["Cisco", "Juniper", "Aruba", "Arista"],
            "Deployment": ["Operational", "Testing", "Retired"],
            "Stock": 20,
            "Maintenance": false
        },
        
        "Firewall": {
            "Vendor": ["Cisco", "Fortinet", "Palo Alto", "Sophos"],
            "Deployment": ["Operational", "Testing", "Retired"],
            "Stock": 12,
            "Maintenance": false
        }
    }
}
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 10: Create a sample valid JSON Data describing the EDGE-Router

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

---
&nbsp;


## RESTCONF
*What information do you need to configure a router interface?*

> Interface:
  > If-Name
  > IP address
  > Subnet Mask
  > Shutdown: Enabled/Disable


~~~
!@UTM-PH
conf t
 username admin priv 15 secret pass
 ip http server
 ip http secure-server
 restconf
 end
~~~


On a Folder:  
~~~
!@cmd
curl.exe -k `
  -u admin:pass `
  -H "Accept: application/yang-data+json" `
  https://192.168.102.11/restconf/data/ietf-interfaces:interfaces `
  -o interface.json
~~~

~~~
!@cmd
curl.exe -k `
  -u admin:pass `
  -H "Accept: application/yang-data+xml" `
  https://192.168.102.11/restconf/data/ietf-interfaces:interfaces `
  -o interface.xml
~~~

~~~
!@cmd
curl.exe -k `
  -u admin:pass `
  -H "Accept: application/yang-data+json" `
  https://192.168.102.11/restconf/data/ietf-yang-library:modules-state `
  -o modules.json
~~~


<br>
<br>

---
&nbsp;


## Python

__Install Necessary Libraries__
~~~
!@cmd
py -m pip install --upgrade pip
py -m pip install netmiko
py -m pip install paramiko
~~~

<br>

| Type                | JSON          | Python        |
| ---                 | ---           | ---           |
| "Cisco"             | Strings       | Strings       |
| 10                  | Integer       | Integer       |
| 10.0                | Float         | Float         |
| True                | Boolean (t/f) | Boolean (T/F) |
| [1,"Router"]        | Array         | List          |
| {"vendor": "cisco"} | Object        | Dictionary    |
| Null                | null          | None          |

<br>

~~~python
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
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 11: From py_dictionary, print the float value 1.0 from key_float.


<br>
<br>

---
&nbsp;


### 🎯 Exercise 12: From py_dictionary, store the string value '5', from key_list, in a variable called, sample. Then, print the value of sample.


<br>
<br>

---
&nbsp;


### 🎯 Exercise 13: From py_dictionary, print the string 'data' from key_dictionary.


<br>
<br>

---
&nbsp;


__rivanlib.py__
~~~python

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
~~~


__csr.py (PLAIN)__
~~~python
from netmiko import ConnectHandler

# Device Info
device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.102.11',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23
}

# Device Configurations
command = [
    'int loopback 1',
    'ip add 1.1.1.1 255.255.255.255'
]


if __name__ == "__main__":

    # Access Device
    access_cli = ConnectHandler(**device)
    access_cli.enable()

    # Push Configs
    access_cli.send_config_set(command)
    siib = access_cli.send_command('show ip int brief')
    access_cli.disconnect()

    print(siib)
~~~


<br>
<br>

---
&nbsp;


## AironetPy

__aironet.py__
~~~python
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
~~~


<br>
<br>

---
&nbsp;


## Session Initiation Protocol

~~~
!@CUCM - Session Initiation Protocol
conf t
 voice service voip
  allow-connections h323 to sip
          
  allow-connections sip to h323
  allow-connections sip to sip
  supplementary-service h450.12
 sip
   bind control source-interface fa0/0
   bind media source-interface fa0/0
   registrar server expires max 600 min 60
 voice register global
  mode cme
  source-address 10.#$34T#.100.1 port 5060
  max-dn 12
  max-pool 12
  authenticate register
  create profile sync syncinfo.xml
 voice register dn 1
   number #$34T#23
   allow watch
   name #$34T#23
 voice register dn 2
   number #$34T#24
   allow watch
   name #$34T#24
  voice register pool 1
    id mac #mym0bilemac#
    number 1 dn 1
    dtmf-relay sip-notify
    username #$34T#23 password #$34T#23
    codec g711ulaw
  voice register pool 2
    id mac #othm0bilemac#
    number 1 dn 2
    dtmf-relay sip-notify
    username #$34T#24 password #$34T#24
    codec g711ulaw
	end
~~~
