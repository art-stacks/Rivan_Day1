
<!-- Your monitor number = #$34T# -->

# 👋 Welcome to Rivan
*"There's no better teacher than experience"*


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
 - 2-tier                 __Cisco Collapsed Campus Core__
 - 3-tier                 __Enterprise Network Design__
 - Spine-leaf             __Data Center Fabric__

<br>

CORE Layer (__CoreTAAS__ & __CoreBABA__) - High Speed and Availability
  > [!NOTE]
  >*"A Network Engineer MUST avoid a single point of failure.
   __Always have a backup.__"*

<br>

Examples:
  | __Protocol__                 | __Supported Devices__    |
  | ---                          | ---                      |
  | Etherchannel                 |                          |
  | FlexStack (Master Switch)    |                          |
  | VSS (Single logical switch)  |                          |
  | SSO (Stateful Switchover)
  | NSF (Non-stop Forwarding)


<br>
<br>

---
&nbsp;


## In-house vs MSP
On-Prem Devices vs RSTHayup Labs (3-tier Enterprise)

<br> 

~~~
!@CoreTAAS
conf t
 hostname CoreTAAS-#$34T#
 enable secret pass
 service password-encryption
 no ip domain lookup
 no logging cons
 line cons 0 
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int vlan 1
  ip add 10.#$34T#.1.2 255.255.255.0
  no shut
  end
~~~

~~~
!@CoreBABA
conf t
 hostname CoreBABA-#$34T#
 enable secret pass
 service password-encryption
 no ip domain lookup
 no logging cons
 line cons 0 
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int vlan 1
  ip add 10.#$34T#.1.4 255.255.255.0
  no shut
  end
~~~


&nbsp;
---
&nbsp;


### Remote Access

~~~
!@cmd
ping 10.#$34T#.1.2
ping 10.#$34T#.1.4

nmap -v 10.#$34T#.1.2
nmap -v 10.#$34T#.1.4
~~~

Telnet the following
- 10.#$34T#.1.2
- 10.#$34T#.1.4


<br>
<br>

---
&nbsp;


## DISCOVERY PROTOCOL
### 🎯 Exercise 01: [3-Tier] Identify port connections between switches.
~~~
!@Switches
show cdp neighbor
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

---
&nbsp;


### [3-Tier] SECURITY Best Practice 
Task 1.
- Disable CDP on Access Switches
- Enable LLDP on Access Switches but only transmit LLDP traffic to D1 & D2

Task 2.
- Disable CDP on Distribution Switches towards access switches
- Enable LLDP on D1 & D2, but only allow recieving traffic from A1,A2,A3


<br>
<br>


### Solution

Task 1.
- Disable CDP on Access Switches
- Enable LLDP on Access Switches but only transmit LLDP traffic to D1 & D2
~~~
!@A1,A2,A3
conf t
 no cdp run
 lldp run
 int range e1/1-2,e2/1-2
  lldp transmit
  no lldp receive
  end
~~~

<br>

Task 2.
- Disable CDP on Distribution Switches towards access switches
- Enable LLDP on D1 & D2, but only allow receiving traffic from A1,A2,A3
~~~
!@D1,D2
conf t
 lldp run
 int range e1/1-2,e2/1-2,e3/1-2
  no cdp enable
  no lldp transmit
  lldp receive
  end
~~~


<br>
<br>

---
&nbsp;


### [On-Prem]

~~~
!@CoreTAAS
conf t
 lldp run
 cdp run
 int range fa0/10-12
  no cdp enable
  no lldp transmit
  lldp receive
  end
~~~

~~~
!@CoreBABA
conf t
 lldp run
 no cdp run
 int range fa0/10-12
  lldp transmit
  no lldp receive
  end
~~~

 
<br>
<br>

---
&nbsp;


## Master the five superheroes of switching
### 1. QPID (802.1Q)

__Access vs Trunk Links__
~~~
!@CoreTAAS & CoreBABA
conf t
 default int fa0/10-12
 int range fa0/10-12
  switchport trunk encapsulation dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
  no shut
  end
show int trunk
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 02: [3-Tier] Trunk the links between C1 & C2
Task 1.
- Configure the Open standard protocol for trunking on the links between Core Switches.
- Make sure VLAN 1 is untagged on all switches.
- Allow all VLANs

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


&nbsp;
---
&nbsp;


~~~
!@C1,C2
conf t
 int range e0/1-3,e1/1-2,e2/1-2
  switchport trunk encapsulation dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
  no shut
  end
show int trunk
~~~

<br>

~~~
!@D1,D2
conf t
 int range e1/0-3,e2/0-3,e3/1-2
  switchport trunk encapsulation dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
  no shut
  end
show int trunk
~~~

<br>

~~~
!@A1,A2,A3
conf t
 int range e1/1-2,e2/1-2
  switchport trunk encapsulation dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
  no shut
  end 
show int trunk
~~~


<br>
<br>

---
&nbsp;


__How to get fired!__
~~~
!@CoreTAAS & CoreBABA
conf t
 no spanning-tree vlan 1-999
 end
~~~

<br>

__Save your network__
~~~
!@CoreTAAS & CoreBABA
conf t
 spanning-tree vlan 1-999
 end
~~~


&nbsp;
---
&nbsp;


### Frame Forwarding
Structure of an Ethernet Frame

| Layer  | Preamble | SFD | MAC Destination | MAC Source | 802.1Q TAG | Ethertype | Payload | FCS | IGP |
| ---    | ---      | --- | ---             | ---        | ---        | ---       | ---     | --- | --- |
| Length | 7        | 1   | 6               | 6          | 4          | 2         | 42-1500 | 4   | 12  |

<br>

### Error Handling
1. __Giants__  
2. __Runts__  
3. __CRC__  
4. __FCS Error__  
4. __Collisions__  
5. __Late Collisions__  
6. __Overruns__  


<br>
<br>

---
&nbsp;


### 2. DARNA (802.1D)
### `32768  vs  24576  vs  28672`

Properly configure the switch

~~~
!@CoreTAAS & C1
conf t
 spanning-tree mode pvst
 spanning-tree vlan 1-999 root primary
 end
~~~

~~~
!@CoreBABA & C2
conf t
 spanning-tree mode pvst
 spanning-tree vlan 1-999 root secondary
 end
~~~


<br>
<br>


__Determine Port Roles__
- Designated
- Root
- Alternate
- Back


<br>
<br>

---
&nbsp;


### Steps & Tie Breakers:
1. Identify the Root Bridge
    - Determine the Lowest Root Bridge ID (Priority & MAC) among all switches

2. Identify Port Roles
    - RP (Root Port) - 1 per Non-Root Bridge
    - DP (Designated Port) - 1 per link
    - AP (Alternate Port)

3. Tie Breakers
    - Lowest Path Cost to Root
    - Lowest Bridge ID 
    - Lowest port ID (Priority + Port Number) of the Other Switch(Sender)
    - Lowest local port ID (Priority + Port Number)


<br>
<br>

---
&nbsp;


### How to determine Port Cost
1. Short Path Cost Method (IEEE 802.1D)

| Link Speed | Default Cost |
| ---        | ---          |
| 10 Mbps    | 100          |
| 100 Mbps   | 19           |
| 1 Gbps     | 4            |
| 10 Gbps    | 2            |

<br>

2. Long Path Cost Method (IEEE 802.1t / 802.1D-2004)

| Link Speed | Default Cost |
| ---        | ---          |
| 10 Mbps    | 2_000_000    |
| 100 Mbps   | 200_000      |
| 1 Gbps     | 20_000       |
| 10 Gbps    | 2_000        |
| 100 Gbps   | 200          |
| 1 Tbps     | 20           |

<br>

~~~
!@CoreBABA
show spanning-tree pathcost method
~~~

<br>

__Port Cost__ = Reference Bandwidth / Link Speed
__Default Ref BW__ = 20_000_000_000 bps


<br>
<br>

---
&nbsp;


### 🎯 Exercise 03: Identify port roles.


![EX_STP](img/ex_stp.png)

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


### [3-Tier] Modify Path costs
Task 1.
- Configure all switches to use the Long Path Cost Method.
- Modify the Reference Bandwidth to 20 Pbs
- Lower the cost of D1's e1/3 interface so it becomes the root port.

<br>

__Solution__

<br>

Task 1.
- Configure all switches to use the Long Path Cost Method.
~~~
!@C1,C2,D1,D2,A1,A2,A3,A4
conf t
 spanning-tree pathcost method long
 end
show spanning-tree pathcost method
~~~

<br>

- Modify the Reference Bandwidth to 20 Pbs
~~~
!@C1,C2,D1,D2,A1,A2,A3,A4
conf t
 !spanning-tree reference-bandwidth cost 20000000000000000
 end
~~~

<br>

- Lower the cost of D1's e1/3 interface to 10 so it becomes the root port.
~~~
!@D1
conf t
 int e1/3
  spanning-tree cost 10
  end
~~~

<br>

Who is __DARNA__ (__802.1D__)
| BLK | LIS | LRN | FWD   |
| --- | --- | --- | ---   |
|     | 15s | 15s | = 30s |

<br>

1. Blocking (BLK) - Listens for BPDUs, does not forward data
2. Listening (LIS) - Listens for BPDUs, starts topology change timer
3. Learning (LRN) - Builds MAC address table but does not forward traffic
4. Forwarding (FWD) - Forwards user traffic and BPDUs


<br>
<br>

---
&nbsp;


### 3. ⚡ WONDERWOMAN (802.1W)
~~~
!@CoreTAAS & CoreBABA, !@C1,C2,D1,D2,A1,A2,A3,A4
conf t
 spanning-tree mode rapid-pvst
 end
show spanning-tree vlan 1
~~~

Discarding, Learning, Forwarding

<br>

STP Features
1. Portfast - Skips all STP negotiation and go straight to forwarding.
   - EDGE Port - Non-Switch link
   - NETWORK Port - Switch to Switch link
2. BPDU Guard - Shuts down a port that receives a BPDU.
3. LOOP Guard - When BPDUs is no longer recieved on Designated ports, keep the port blocked. | Blocking
4. Root Guard - Stops a port from accepting superior BPDUs. | Blocking
5. BPDUFilter - Will not send BPDUs until received.
6. UplinkFast - Recover quickly from uplink failure.
7. BackboneFast - Old ver of Uplinkfast

<br>

__Best Practice__

<br>

Access Layer                        |   
Distribution Layer (toward Access)  |   
Core/Trunk Links (between switches) |   

<br>

~~~
!@CoreTAAS
conf t
 spanning-tree backbonefast    !unnecessary for rstp (has built-in convergence)
 spanning-tree portfast bpdufilter default
 spanning-tree portfast bpduguard default
 int range fa0/1-8
  spanning-tree portfast  !edge
 !int range fa0/10-12
  !spanning-tree portfast !network
  end
~~~

~~~
!@CoreBABA
conf t
 spanning-tree uplinkfast    !unnecessary for rstp (has built-in convergence)
 spanning-tree portfast bpdufilter default
 spanning-tree portfast bpduguard default
 int range fa0/1-8
  spanning-tree portfast
 !int range fa0/10-12
  !spanning-tree portfast !network
  end
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 04: [3-Tier] Determine STP Features
What STP features should be applied on the network to optimize STP traffic and network performance.

~~~
!@A1,A2,A3
conf t
 int range e0/1-2
  spanning-tree portfast edge
  spanning-tree bpduguard enable
  spanning-tree bpdufilter enable
 int range e1/1-2,e2/1-2
  spanning-tree guard loop
  spanning-tree portfast network
  spanning-tree uplinkfast
  end
~~~

~~~
!@D1,D2
conf t
 int range e1/0-3,e2/0-3,e3/1-2
  spanning-tree portfast network
  spanning-tree guard loop
 int range e1/0,e1/3,e2/0,e2/3
  spanning-tree uplinkfast
  end
~~~

~~~
!@D2
conf t
 int e0/0
  spanning-tree portfast edge
  spanning-tree bpduguard enable
  spanning-tree bpdufilter enable
  end
~~~

~~~
!@C1,C2
conf t
 int range e0/1-3,e1/1-2,e2/1-2
  spanning-tree portfast network
  spanning-tree guard loop
  end
~~~

~~~
!@C2
conf t
 int range e0/1-3
  spanning-tree uplinkfast
  end
~~~


<br>
<br>

---
&nbsp;


### [3-Tier] NIST SP 800-41r1 network security guidance recommends to enable PortFast & BPDU Guard Globally.
~~~
!@Switches
! spanning-tree portfast default
! spanning-tree portfast bpduguard default
! spanning-tree portfast bpdufilter default
~~~

<br>

Who is __WONDERWOMAN__ (__802.1W__)
| DIS | LRN | FWD |
| --- | --- | --- |
|     |     |     |

<br>

1. Discarding (DIS) - Not forwarding user frames; discards traffic. Listens for BPDUs
2. Learning (LRN) - Builds MAC address table but does not forward user traffic
3. Forwarding (FWD) - Forwards user traffic and BPDUs


<br>
<br>

---
&nbsp;


### 4. SUPERMAN (802.1S)
Step 1: Configure VTP
~~~
!@CoreTAAS,C1,C2
conf t
 vtp domain ccnp
 vtp mode server
 vtp version 1
 end
~~~

~~~
!@CoreBABA,D1,D2,A1,A2,A3,A4
conf t
 vtp domain ccnp
 vtp version 1
 vtp mode client
 end
~~~


<br>


Step 2: Configure VLANs
~~~
!@CoreTAAS,C1,C2
conf t
 vlan 1-40
  exit
 vlan 41-70
  exit
 vlan 71-100
 end
~~~

~~~
!@CoreBABA
conf t
 int range fa0/2,fa0/4
  switchport mode access
  switchport access vlan 10
 int range fa0/6,fa0/8
  switchport mode access
  switchport access vlan 50
 int fa0/3
  switchport mode access
  switchport access vlan 100
 int range fa0/5,fa0/7
  switchport voice vlan 100
  end
~~~


<br>


Step 3: Enable 802.1S
~~~
!@CoreTAAS,CoreBABA,C1,C2,D1,D2,A1,A2,A3
conf t
 spanning-tree mode mst
 spanning-tree mst configuration
  name superman-stp
  revision 1
   instance 1 vlan 1-40
   instance 2 vlan 41-70
   instance 3 vlan 71-100
   end
show spanning-tree mst configuration
~~~


<br>


Reconfigure Port Priority
~~~
!@CoreTAAS,C1
config t
 spanning-tree mst 0 root primary
 spanning-tree mst 1 root secondary
 spanning-tree mst 2 root primary
 spanning-tree mst 3 root secondary
end
~~~

~~~
!@CoreBABA,C2
config t
 spanning-tree mst 0 root Secondary
 spanning-tree mst 1 root primary
 spanning-tree mst 2 root Secondary
 spanning-tree mst 3 root primary
end
~~~

Who is SUPERMAN (802.1S)
Multiple VLANs sharing a spanning tree instance,  
compared to PVST & RST where each VLANs is its own STP instance.


<br>
<br>

---
&nbsp;


### 5. X-MEN (802.1X)
> [!IMPORTANT]
> Configure WinServer 2022 for a RADIUS Server

<br>

Requirements:
- ACTIVE DIRECTORY
- NETWORK POLICY SERVER (RADIUS)


<br>


__Parser View__
~~~
!@CoreTAAS
conf t
 aaa new-model
 aaa authentication login default local
 aaa authorization exec default local
 line vty 0 14
  transport input all
  login authentication default
 !
 parser view T1
  secret pass
  commands exec include configure terminal
  commands exec include show ip interface brief
  commands exec include show interface *
  commands configure include interface
  commands configure include interface GigabitEthernet1 
  commands interface include shutdown
  commands interface include no shutdown
  exit
 username tier1 view T1 secret pass
 username tier2 privilege 15 secret pass
 end
~~~


<br>
<br>

---
&nbsp;


### [3-Tier] Configure AAA-Based local database authentication on C1 & C2 

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


## Port Aggregation
LACP vs PAGP

| Mode             | On  | Active/Desirable | Passive/Auto |
| ---              | --- | ---              | ---          |
| On               | [x] | [ ]              | [ ]          | 
| Active/Desirable | [ ] | [x]              | [x]          |
| Passive/Auto     | [ ] | [x]              | [ ]          |

~~~
!@CoreTAAS
conf t
 int range fa0/10-12
  channel-group 1 mode active
  port-channel load-balance src-mac
  end
show int po1 | inc BW
~~~

~~~
!@CoreBABA
conf t
 int range fa0/10-12
  channel-group 1 mode passive
  port-channel load-balance src-mac
  end
show int po1 | inc BW
~~~


<br>


How does Port-Channel load balance
- src-mac
- src-dst-ip
- extended

<br>

Set a minimum & maximum bundle links.
~~~
!@CoreTAAS,CoreBABA
conf t
 int po1
  lacp max-bundle 8
  port-channel min-links 2
  end
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 05: [3-Tier] Configure Etherchannel links
Note:
- Configure Etherchannel on the links between switches.
- Configure the Port-Channel Number base on the diagram.

Task1:
- C1 & C2 must use the open standard protocol for link aggregation. 
- C1 & C2 must both participate in forming link aggregation on all linked ports.
- If the number of bundled ports goes down to 2 or less, the port-channel must go down.

~~~
!@C1
conf t
 int range e0/1-3
  channel-group 40 mode active
 int range e1/1-2
  channel-group 11 mode active
 int range e2/1-2
  channel-group 12 mode active
 int po40
  port-channel min-links 3
  end
~~~

~~~
!@C2
conf t
 int range e0/1-3
  channel-group 40 mode active
 int range e1/1-2
  channel-group 21 mode active
 int range e2/1-2
  channel-group 22 mode active
 int po40
  port-channel min-links 3
  end
~~~


<br>
<br>


Task2:
- D1 & D2 must use the open standard protocol for link aggregation. 
- D1 & D2 must not participate but will form link aggregation on all linked ports.

~~~
!@D1
conf t
 int range e1/0,e1/3
  channel-group 11 mode passive
 int range e2/0,e2/3
  channel-group 21 mode passive
 int range e1/1-2
  channel-group 41 mode passive
 int range e2/1-2
  channel-group 42 mode passive
 int range e3/1-2
  channel-group 43 mode passive
  end
~~~

~~~
!@D2
conf t
 int range e1/0,e1/3
  channel-group 12 mode passive
 int range e2/0,e2/3
  channel-group 22 mode passive
 int range e1/1-2
  channel-group 44 mode passive
 int range e2/1-2
  channel-group 45 mode passive
 int range e3/1-2
  channel-group 46 mode passive
  end
~~~


<br>
<br>


Task3:
- A1, A2, and A3 must use the open standard protocol for link aggregation. 
- A1, A2, and A3 must participate in forming link aggregation on all linked ports.

~~~
!@A1
conf t
 int range e1/1-2
  channel-group 41 mode active
 int range e2/1-2
  channel-group 44 mode active
  end
~~~

~~~
!@A2
conf t
 int range e1/1-2
  channel-group 42 mode active
 int range e2/1-2
  channel-group 45 mode active
  end
~~~

~~~
!@A3
conf t
 int range e1/1-2
  channel-group 43 mode active
 int range e2/1-2
  channel-group 46 mode active
  end
~~~


<br>
<br>

---
&nbsp;


## IP ADDRESSING
### Switch Virtual Interface (SVI)

~~~
!@CoreTAAS
conf t
 int vlan 10
  description WIFIVLAN
  ip add 10.#$34T#.10.2 255.255.255.0
  no shut
  exit
 int vlan 50
  description CCTVVLAN
  ip add 10.#$34T#.50.2 255.255.255.0
  no shut
  exit
 int vlan 100
  description VOICEVLAN
  ip add 10.#$34T#.100.2 255.255.255.0
  no shut
  end
~~~

~~~
!@CoreBABA
conf t
 int vlan 10
  description WIFIVLAN
  ip add 10.#$34T#.10.4 255.255.255.0
  no shut
  exit
 int vlan 50
  description CCTVVLAN
  ip add 10.#$34T#.50.4 255.255.255.0
  no shut
  exit
 int vlan 100
  description VOICEVLAN
  ip add 10.#$34T#.100.4 255.255.255.0
  no shut
  end
~~~

~~~
!@P1
conf t
 int e0/0
  no shut
  ip add 10.1.10.101 255.255.255.224
  end
~~~

~~~
!@P2
conf t
 int e0/0
  no shut
  ip add 192.168.30.113 255.255.255.248
  end
~~~

~~~
!@P3
conf t
 int e0/0
  no shut
  ip add 10.1.20.60 255.255.255.240
  end
~~~

~~~
!@P4
conf t
 int e0/0
  ip add 10.1.10.102 255.255.255.224
  no shut
  end
~~~

  
<br>
<br>

---
&nbsp;


### DHCP
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
  option 43 ip 10.#$34T#.10.#$34T#
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


| DHCP Options | Unit |
| ---          | ---  |
| 1            |      |
| 2            |      |
| 43           |      |
| 42           |      |
| 150          |      |


<br>


DHCP States:
1.
2.
3.
4.

What type of data traffic is each state? (Unicast, Broadcast, Multicast)
Base on Wireshark.


<br>
<br>

---
&nbsp;


### 🎯 Exercise 06: [3-Tier] Configure DHCP Pool for SALES
Task 1.
- Use the IP address 192.168.50.0/24
- Apply the First Valid IP on C1, last Valid on C2
- Load balance between C1 & C2 
  - C1 must distribute .100 - .199 IPs
  - C2 must distribute .200 - .253 IPs
- Set the Domain name to SALES.COM
- The default Gateway must be the DHCP server that provided the IP address.

<br>

Task 2.
- Configure P5 as a dhcp client

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


### VLAN Management
*Did devices get IP from the correct VLAN?*

~~~
!@CoreBABA
conf t
 int range fa0/2,fa0/4
  switchport mode access
  switchport access vlan 10
  exit
 int range fa0/6,fa0/8
  switchport mode access
  switchport access vlan 50
  exit
 int fa0/3
  switchport mode access
  switchport access vlan 100
  exit
 int range fa0/5,fa0/7
  switchport mode access
  switchport access vlan 100
  switchport voice vlan 100
  mls qos trust device cisco-phone
  mls qos trust cos
  end
~~~


<br>


__Assign RSTVM to VLAN 1__
~~~
!@A3
conf t
 int e3/3
  no shut
  switchport mode access
  switchport access vlan 1
  end
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 07: [3-Tier] Assign end devices to their specified VLAN
| Device | VLAN    |
| ---    | ---     |
| P1     | ADMIN   |
| P2     | HR      | 
| P3     | FINANCE |
| P4     | ADMIN   |
| P5     | SALES   |

~~~
!@A1
conf t
 int e0/1
  switchport mode access
  switchport access vlan 10
 int e0/0
  switchport mode access
  switchport access vlan 30
  end
~~~

~~~
!@A2
conf t
 int e0/1
  switchport mode access
  switchport access vlan 20
 int e0/0
  switchport mode access
  switchport access vlan 10
  end
~~~

~~~
!@A3
conf t
 int e0/1
  switchport mode access
  switchport access vlan 50
  end
~~~


<br>
<br>

---
&nbsp;


## MAC Learning
### IP Reservation
~~~
!@CoreTAAS
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
<br>

---
&nbsp;


### Port Security
~~~
!@CoreBABA
conf t
 int fa0/6
  switchport mode access
  switchport port-security
  switchport port-security mac-address sticky
  switchport port-security maximum 1
  switchport port-security violation shutdown
  exit
 int fa0/8
  switchport mode access
  switchport port-security
  switchport port-security mac-address sticky
  switchport port-security maximum 1
  switchport port-security violation shutdown
  end
sh port-security address
sh int status err-disable
~~~

<br>

__Make Ports Alive again__
~~~
!@CoreBABA
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
~~~

 
<br>
<br>

---
&nbsp;


## Dynamic ARP Inspection & DHCP Snooping 
~~~
!@CoreBABA
conf t
 ip dhcp snooping
 ip dhcp snooping vlan 100
 no ip dhcp snooping information option
 !
 int po1
  ip dhcp snooping trust
  end
show ip dhcp snooping binding
~~~

~~~
!@CoreBABA
conf t
 ip arp inspection vlan 100
 int range fa0/1-8,fa0/10-12
  ip arp inspection trust
  exit
 ip arp inspection validate src-mac dst-mac ip
 end
~~~


<br>


__STATIC DAI__
~~~
!@CoreBABA
conf t
 ip arp inspection VLAN 1
 arp access-list STATIC-ARP
  permit ip host __.__.__.__  mac __.__.__.__

  exit
 ip arp inspection filter STATIC-ARP vlan 1
 ip arp inspection validate src-mac dst-mac ip
 
 int range fa0/2-12
  ip arp inspection trust
  end
~~~


<br>
<br>

---
&nbsp;


## Managing Enterprise Communication
~~~
!@CUCM
conf t
 hostname CUCM-#$34T#
 enable secret pass
 service password-encryption
 no ip domain lookup
 no logging cons
 line cons 0 
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int fa0/0
  ip add 10.#$34T#.100.8 255.255.255.0
  no shut
  end
~~~


<br>
<br>

---
&nbsp;


### Analog Phones
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

~~~
!@CUCM
conf t
 voice-port 0/0/0
  signal loopstart
  caller-id enable
  station-id name ANALOG1
  cptone PH  / US
 end
!
csim start #$34T#00
~~~


<br>
<br>

---
&nbsp;


### IP Phones
__Requirements for IP Phones to work__
1. &nbsp;
2. &nbsp;
3. &nbsp;
4. &nbsp;
5. &nbsp;
6. &nbsp;
7. &nbsp;

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
~~~


<br>
<br>

---
&nbsp;


### IP Phone Features (Video/Conference Calls)
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


### Incoming Calls
~~~
!@CUCM
conf t
 voice service voip
 ip address trusted list
 ipv4 0.0.0.0 0.0.0.0
 end
~~~


<br>
<br>

---
&nbsp;


### Outgoing Calls
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


### Remote Access - Jumpserver
*Can you reach CUCM from the PC?*

~~~
!@cmd
ping 10.#$34T#.100.8
~~~


<br>
<br>

---
&nbsp;


## 🔧 Configure EDGE
### 🏨 Establish connectivity.
*How do you gain access to the internet?*

~~~
!@EDGE
conf t
 hostname EDGE-#$34T#
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


### `Switch` vs `Routers`
~~~
!@CoreBABA
conf t
 int g0/1
  no switchport
  ip add 10.#$34T#.#$34T#.4 255.255.255.0
  no shut
  end
~~~


<br>
<br>

---
&nbsp;


## Site Connectivity
### Private Circuit
~~~
!@EDGE
conf t
 ip routing
 !
 router ospf 1
  router-id #$34T#.0.0.1
  network #$34T#.0.0.1 0.0.0.0 area 0
  network 10.#$34T#.#$34T#.0 0.0.0.255 area 0
  network 200.0.0.0 0.0.0.255 area 0
 int gi 0/0/0
  ip ospf network point-to-point
  end
~~~

~~~
!@CoreBABA
conf t
 router ospf 1
  router-id 10.#$34T#.#$34T#.4
   network 10.#$34T#.0.0 0.0.255.255 area 0
 int gi 0/1
  ip ospf network point-to-point
  end
~~~

~~~
!@CUCM
conf t
 router ospf 1
  router-id 10.#$34T#.100.8
  network 10.#$34T#.100.0 0.0.0.255 area 0
  end
~~~


<br>
<br>

---
&nbsp;


### Internet Access
~~~
!@EDGE
conf t
 int g0/0/0
  ip nat inside
  exit
 int g0/0/1
  ip nat outside
  end
~~~

~~~
!@EDGE
conf t
 ip access-list extended NAT-POLICY
  permit ip any any
  end
~~~

~~~
!@EDGE
conf t
 ip nat inside source list NAT-POLICY int g0/0/1 overload
 end
~~~

~~~
!@EDGE
conf t
 ip route 0.0.0.0 0.0.0.0 200.0.0.1
 ip name-server 8.8.8.8
 ip domain lookup
 ip domain lookup source-int g0/0/0
 end
~~~


<br>
<br>

---
&nbsp;


### Network Assurance (HSRP)

__PRIMARY__
~~~
!@C1
conf t
 track 1 int vlan 10 line-protocol
 interface Vlan 10
  standby 1 ip 10.1.10.105
  standby 1 priority 110
  standby 1 preempt
  standby 1 track 1 decrement 60
  end
~~~

~~~
!@CoreTAAS
config t
 hostname CoreTAAS-#$34T#-(PLDT)
 Track 1 Int gi 0/1 line-protocol
 int vlan 1
  standby 1 ip 10.#$34T#.1.16
  standby 1 preempt
  standby 1 Priority 150
  standby 1 Track 1 decrement 60
  end
~~~


<br>


__SECONDARY__
~~~
@C2
conf t
 interface Vlan 10
  standby 1 ip 10.1.10.105
  standby 1 priority 90
  end
~~~

~~~
!@CoreBABA
config t
 hostname CoreBABA-#$34T#-(GLOBE)
 Int vlan 1
  standby 1 ip 10.#$34T#.1.16
  standby 1 preempt
  standby 1 Priority 100
  end
~~~


<br>
<br>

---
&nbsp;


### Network Tunneling
~~~
!@EDGE
conf t
 no router ospf 1
 router ospf 1
  router-id #$34T#.0.0.1
  network 10.#$34T#.#$34T#.0 0.0.0.255 area 0
  default-information originate always
  end
~~~

~~~
!@EDGE
conf t
 int tun1
  ip add 172.16.1.#$34T# 255.255.255.0
  tunnel source g0/0/1
  tunnel mode gre multipoint
  no shut
  tun key 123
  ip nhrp authentication C1sc0123
  ip nhrp map multicast dynamic
  ip nhrp network-id 1337
  ip nhrp map 172.16.1.11 200.0.0.11
  ip nhrp map 172.16.1.12 200.0.0.12
  ip nhrp map 172.16.1.21 200.0.0.21
  ip nhrp map 172.16.1.22 200.0.0.22
  ip nhrp map 172.16.1.31 200.0.0.31
  ip nhrp map 172.16.1.32 200.0.0.32
  ip nhrp map 172.16.1.41 200.0.0.41
  ip nhrp map 172.16.1.42 200.0.0.42
  ip nhrp map 172.16.1.51 200.0.0.51
  ip nhrp map 172.16.1.52 200.0.0.52
  ip nhrp map 172.16.1.61 200.0.0.61
  ip nhrp map 172.16.1.62 200.0.0.62
  ip nhrp map 172.16.1.71 200.0.0.71
  ip nhrp map 172.16.1.72 200.0.0.72
  ip nhrp map 172.16.1.81 200.0.0.81
  ip nhrp map 172.16.1.82 200.0.0.82
  ip nhrp map 172.16.1.91 200.0.0.91
  ip nhrp map 172.16.1.92 200.0.0.92
  no ip nhrp map 172.16.1.#$34T# 200.0.0.#$34T#
  exit
  !
 no ip access-list extended NAT-POLICY
 ip access-list extended NAT-POLICY
  deny ip 10.#$34T#.0.0 0.0.255.255 10.11.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.12.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.21.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.22.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.31.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.32.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.41.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.42.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.51.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.52.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.61.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.62.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.71.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.72.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.81.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.82.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.91.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.92.0.0 0.0.255.255
  no deny ip 10.#$34T#.0.0 0.0.255.255 10.#$34T#.0.0 0.0.255.255
  permit ip any any
  exit
 !
 ip route 10.11.0.0 255.255.0.0 172.16.1.11 252
 ip route 10.12.0.0 255.255.0.0 172.16.1.12 252
 ip route 10.21.0.0 255.255.0.0 172.16.1.21 252
 ip route 10.22.0.0 255.255.0.0 172.16.1.22 252
 ip route 10.31.0.0 255.255.0.0 172.16.1.31 252
 ip route 10.32.0.0 255.255.0.0 172.16.1.32 252
 ip route 10.41.0.0 255.255.0.0 172.16.1.41 252
 ip route 10.42.0.0 255.255.0.0 172.16.1.42 252
 ip route 10.51.0.0 255.255.0.0 172.16.1.51 252
 ip route 10.52.0.0 255.255.0.0 172.16.1.52 252
 ip route 10.61.0.0 255.255.0.0 172.16.1.61 252
 ip route 10.62.0.0 255.255.0.0 172.16.1.62 252
 ip route 10.71.0.0 255.255.0.0 172.16.1.71 252
 ip route 10.72.0.0 255.255.0.0 172.16.1.72 252
 ip route 10.81.0.0 255.255.0.0 172.16.1.81 252
 ip route 10.82.0.0 255.255.0.0 172.16.1.82 252
 ip route 10.91.0.0 255.255.0.0 172.16.1.91 252
 ip route 10.92.0.0 255.255.0.0 172.16.1.92 252
 !
 no ip route 10.#$34T#.0.0 255.255.0.0 172.16.1.#$34T# 252
 end
~~~ 


<br>
<br>

---
&nbsp;


### OSPF vs EIGRP
~~~
!@EDGE
conf t
 int tun1
  no ip eigrp next-hop-self
  no ip split-horizon eigrp 100
  bandwidth 10000
  mtu 1400
  ip tcp adjust-mss 1360
 no router ospf 1
 router ospf 1
  router-id #$34T#.0.0.1
  network 10.#$34T#.#$34T#.0 0.0.0.255 area 0
  default-information originate always
 router eigrp 100
  no auto-summary
  router-id 200.0.0.#$34T#
  network 200.0.0.0 0.0.0.255
  network 172.16.1.0 0.0.0.255
  end
~~~

~~~
!@EDGE
conf t
 router ospf 1
  redistribute eigrp 100 subnets
  exit
 router eigrp 100
  redistribute ospf 1 metric 10000 100 255 1 1500
  end
~~~


<br>
<br>

---
&nbsp;


### Review  
Requirements for IP Phones to work  
1. &nbsp;
2. &nbsp;
3. &nbsp;
4. &nbsp;
5. &nbsp;
6. &nbsp;  
7. &nbsp;

<br>

~~~
!@cmd
nmap -v 10.#$43T#.100.8
~~~

<br>

How to monitor packets from a different network?

~~~
!@CoreBABA
conf t
 monitor session 1 source int fa0/3,fa0/5,fa0/7
 monitor session 1 destination int fa0/1,fa0/9
 end
~~~

<br>

~~~
!@CoreBABA
conf t
 no monitor session 1 source int fa0/3,fa0/5,fa0/7
 no monitor session 1 destination int fa0/1,fa0/9
 end
~~~


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


### 🎯 Exercise 08: Describe a product

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


### 🎯 Exercise 09: Create a sample valid JSON Data describing the EDGE-Router

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


### 🎯 Exercise 10: From py_dictionary, print the float value 1.0 from key_float.


<br>
<br>

---
&nbsp;


### 🎯 Exercise 11: From py_dictionary, store the string value '5', from key_list, in a variable called, sample. Then, print the value of sample.


<br>
<br>

---
&nbsp;


### 🎯 Exercise 12: From py_dictionary, print the string 'data' from key_dictionary.


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


<br>
<br>

---
&nbsp;


## YANG DATA MODELING LANGUAGE
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


### CRUD     What to do with data
- Create     Add new data
- Read       Retrieve existing data
- Update     Modify existing data
- Delete     Remove data


<br>


### HTTP Protocol Operations / Methods / Verbs
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


&nbsp;
---
&nbsp;


### Create a Python script that will save the configurations of CoreTAAS, CoreBABA, CUCM, & EDGE
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


&nbsp;
---
&nbsp;


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


&nbsp;
---
&nbsp;


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


&nbsp;
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

