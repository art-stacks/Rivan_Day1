
<!-- Your monitor number = #$34T# -->


# 👋 Welcome to Rivan
*"There's no better teacher than experience"*

&nbsp;

## 📋 Prove what you are doing.
 - Create a Github account: https://github.com/

<br>

Import the repositories.
 - Rivan_Day1 : https://github.com/art-stacks/Rivan_Day1
 - SecPlus701 : https://github.com/rivancorp/SECplus701
 - RivanSecPlus701 : https://github.com/rivancorp/RivanSecPlus701


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

  - WiFi 6     IEEE 802.11ax
  - WiFi 7     IEEE P802.11be


<br>
<br>

---
&nbsp;


## 🔍 Implement security solutions.

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


# 🔧 Access the CLI
*How can you tell if a device is expensive? It has a __Console Port__*

<br>

Serial Cable
  - VGA, USB
  - Ugreen


<br>
<br>

---
&nbsp;


# 📤 IT Service Management

<br>

### Lab Setup
__1. Run the *IR-ElasticSys* virtual machine & Setup a WINSERVER VM__  

<br>

__2. VM Login information:__
> Username: root  
> Password: C1sc0123

<br>

__3. Get the IP address of the VM.__  
Enter the command inside the VM
~~~bash
@IR-ElasticSys
ip addr
~~~

<br>

__4. Add a hostname mapping.__  
Access the __hosts__ file located on `c:\Windows\System32\drivers\etc`  
Then, enter add the following mapping to the hosts file:
~~~
192.168.102.133  rivan.cloudsoc.com
~~~

> [!Note]
> __192.168.102.133__ must be your virtual machine IP address.

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
### 🏃 Service Delivery Team
http://rivan.cloudsoc.com/otrs/index.pl  
> Username: admin   
> Password: C1sc0123  


&nbsp;
---
&nbsp;


### 🙇 Service Desk
http://rivan.cloudsoc.com/otrs/customer.pl  
> Username: user1  
> Password: C1sc0123


&nbsp;
---
&nbsp;


## 📦 Operational Support System
*How easy is it to bring home items from your company?*


&nbsp;
---
&nbsp;


### Acquisition/Procurement Process
1. Purchasing Process
2. Negotiation with Suppliers
3. Purchase, Invoice, Payments, & Receipts


<br>
<br>


### Assignment/Accounting Process
1. A Central asset tracking system
2. Ownership
3. Classification


<br>
<br>

---
&nbsp;


### 🎯 Exercise 01: Create a Customer User Account

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


### Monitoring/Asset Tracking
1. Inventory Every Asset
2. Associate a ticket with the asset
3. Enumeration
4. Asset Tag


<br>
<br>

---
&nbsp;


### 🎯 Exercise 02: Register Windows Server 2025 to your company's database.

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
### ⭐ 1. Register CoreTAAS to your company's database, including a *FAQ* to configure the devices.

__BootStrap Configurations__
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
  desc DEFAULT-SVI
 int vlan 10
  no shut
  ip add 10.#$34T#.10.2 255.255.255.0
  desc WIRELESS-SVI
 int vlan 50
  no shut
  ip add 10.#$34T#.50.2 255.255.255.0
  desc VIDEO-SVI
 int vlan 100
  no shut
  ip add 10.#$34T#.100.2 255.255.255.0
  desc VOICE-SVI
 end
~~~


<br>
<br>

---
&nbsp;


## 🚀 Deploy CoreBABA
### 🎯 Exercies 03: Register CoreBABA to your company's database.

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


## Know the jobs of a Switch
### ⚙️ 1. __POE__
*Are there switches that don't support POE? __Yes__.*
> [!NOTE]
> If you need PoE functionality on a non-PoE switch, use a PoE injector.

<br>

| IEEE Standards  | Power Output |
| ---             |     ---      |
| 802.3af (PoE)   |              |
| 802.3at (PoE+)  |              |
| 802.3bt (PoE++) |              |

<br>

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


# ⭐ Fundamental Security Concepts
1. __C__
2. __I__
3. __A__


&nbsp;
---
&nbsp;


### 🔐 Confidentiality

*How to access port 445 because you don't have a Firewall!*
~~~
!@cmd
net use \\10.3.3.x\ipc$ /user:administrator C1sc0123
net use x: /delete
net use x: \\10.3.3.x\c$
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 04: Why use VPN when you are WFH
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

*__Confidentiality__ is the security concept that ensures data is protected from unauthorized access or __Disclosure__.*


<br>

~~~
!@CoreTAAS
conf t
 username admin privilege 15 secret pass
 username _____ privilege 15 secret pass
 !
 ip domain name sec.com
 crypto key generate rsa
 2048
 ip ssh version 2
 !
 line vty 0 14
  transport input all
  login local
  exec-timeout 0 0
  end
~~~

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
  commands configure include interface GigabitEthernet0/1 
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


### ✉️ Integrity
~~~
!@cmd
certutil -hashfile            md5
~~~


<br>
<br>

---
&nbsp;


### 🔀 Availability
*Avoid a single point of failure*

1. Load Balancing
2. Failover
3. Backup
4. Rate Limiting / DDoS Protection
5. CDN (Content Delivery Networks)
6. RAID Storage


<br>


Execute a persistent ping
~~~
!@cmd
ping 10.#$34T#.1.2 -t
~~~

<br>

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
<br>

---
&nbsp;


### 🔴 RED Team
Hack your LAN to better protect it.
1. Run __\_Pentest__
2. Login to the VM
> Username: admin  
> Password: pass  

3. Run yersinia

~~~
@_Pentest
sudo yersinia -G
~~~


<br>
<br>


🔴 __Creating a Rogue DHCP Server:__
- WireShark
- Pentest

<br>

__\_Pentest__
~~~
!@linux
nmcli connection add \
type ethernet \
con-name TUNAYNALAN \
ifname eth0 \
ipv4.method manual \
ipv4.addresses 10.#$34T#.1.20/24 \
autoconnect yes

nmcli connection up TUNAYNALAN
~~~


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


<br>


🔴 __DHCP Starvation Attack:__
*Sending DHCP DISCOVER Packet*

| States      | Type      |
| ---         | ---       |
| Discover    | Broadcast |
| Offer       | Unicast   |
| Request     | Broadcast |
| Acknowledge | Unicast   |


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
!@CoreTAAS
conf t
 vtp mode server
 vtp domain SEC
 vtp version 1
 vlan 10
  name WIRELESS-VLAN
 vlan 50
  name VIDEO-VLAN
 vlan 100
  name VOICE-VLAN
  end
~~~

~~~
!@CoreBABA
conf t
 vtp mode server
 vtp domain SEC
 vtp version 1
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


## ⚙️ 5. MAC Learning & MAC Reservation
How to view the MAC addresses learned by the Switch? __SMAC - `show mac address-table`__
~~~
!@CoreTAAS,CoreBABA
show mac address-table
~~~

<br>

| Camera         | MAC Address      |
| ---            | ---              |
| Camera fa0/6   | #camera6macadd#  |
| Camera fa0/8   | #camera8macadd#  |


<br>

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


# IT Service Management Components

<br>

## 1.0 Tickets

### ALERT MANAGEMENT

1. Security Alert - Created automatically by security tools (SIEM, EDR, IDS/IPS, email security, etc.) when suspicious activity is detected. Requires triage to determine whether the alert is a false positive or a real threat.

<br>
<br>

2. False Positive Review - Documents alerts determined to be benign to improve future detections.


&nbsp;
---
&nbsp;


### INCIDENT RESPONSE

1. Security Incident - Confirmed security event requiring response and remediation.


<br>
<br>


2. Malware - Investigation of malware or ransomware infections.


<br>
<br>


3. Phishing - Investigation of phishing emails or malicious websites.


<br>
<br>


4. Digital Forensics - Collection and preservation of digital evidence after a security incident.


&nbsp;
---
&nbsp;


### INVESTIGATION & THREAT HUNTING

1. Investigation - Detailed analysis of suspicious activity that has not yet been confirmed as malicious.


<br>
<br>


2. Threat Hunting - Proactive search for hidden threats based on intelligence or hypotheses.


<br>
<br>


3. Threat Intelligence - Management of threat intelligence and IOC information.


&nbsp;
---
&nbsp;


### VULNERABILITY MANAGEMENT

1. Vulnerability - Tracks discovered vulnerabilities through remediation.


<br>
<br>


2. Risk Assessment - Evaluates security risks for systems, projects, or business changes.


&nbsp;
---
&nbsp;


### IDENTITY & ACCESS MANAGEMENT

1. Access Request - User requests for new accounts, VPN access, privileged access, or permission changes.


<br>
<br>


2. Access Review - Periodic audit of user and administrator permissions.


&nbsp;
---
&nbsp;


### GOVERNANCE, RISK, AND COMPLIANCE

1. Compliance - Activities supporting audits, regulatory requirements, and policy compliance.


<br>
<br>


2. Policy Exception - Request to temporarily deviate from an established security policy.


<br>
<br>

---
&nbsp;


## 2.0 Queues

<br>

### 1. [SOC] Tier 1 - First-line monitoring and triage.  

  > Sub Queues
  > - Alert Triage - Monitor dashboards, acknowledge alerts, create tickets.
  > - Monitoring - Identify false positives, classify alerts, gather initial evidence.
  > - Threat Validation - Correlate basic logs, enrich alerts with threat intelligence.
  > - Escalation/T2 Review - Document findings and transfer tickets to Tier 2.


&nbsp;
---
&nbsp;


### 2. [SOC] Tier 2 - Incident Responder (Investigation & Escalation)  

  > Sub Queues
  > - Incident Investigation - Detailed investigation of escalated alerts.
  > - Incident Response - Contain compromised systems, isolate endpoints, coordinate recovery.
  > - Malware and Phishing Analysis - Analyze malicious files, review persistence mechanisms, identify IOCs, phishing emails, URLs, attachments, remove malicious emails.
  > - Endpoint and Network Investigation - Review processes, registry changes, persistence, EDR telemetry. Analyze NetFlow, firewall logs, IDS alerts, VPN activity.
  > - Account Compromise - Investigate suspicious logins, disable compromised accounts, enforce password resets.


&nbsp;
---
&nbsp;


### 3. [SOC] Tier 3 - SOC Manager, CISO, Threat Intelligence Lead  

  > Sub Queues
  > - Threat Hunting - Hunt for attacker behaviors and unknown compromises.
  > - Digital Forensics - Acquire and analyze disk images, memory captures, maintain evidence.
  > - Security Engineering - Configure SIEM, SOAR, EDR, log collectors, automation.
  > - SOAR (Security Orchestration and Automation) - Develop playbooks, automate repetitive analyst tasks.
  > - Advance Malware Analysis - Reverse engineer malware, identify capabilities, produce detection signatures.


<br>
<br>

---
&nbsp;


## Services

<br>

### 1. [SOC] Network Security  

  > Sub Queues
  > - Firewall - Investigate blocked connections, review firewall logs, implement approved firewall rule changes, analyze suspicious traffic.
  > - IDS/IPS - Investigate IDS alerts, tune signatures, validate exploits, block malicious traffic.
  > - VPN - Investigate abnormal VPN logins, validate MFA, review geolocation anomalies, disable compromised accounts.
  > - DNS Security - Investigate DNS tunneling, block malicious domains, analyze DNS queries.
  > - Web Proxy - Investigate web access violations, block malicious URLs, review proxy logs.
  > - Network Access Control (NAC) - Services that protect and monitor the organization's network.


&nbsp;
---
&nbsp;


### 2. [SOC] Endpoint Security  

  > Sub Queues
  > - Endpoint Detection and Response - Investigate endpoint alerts, isolate hosts, collect forensic artifacts, remove malware.
  > - Antivirus/Anti-Malware - Review malware detections, update signatures, validate quarantined files.
  > - Endpoint Management - Verify security policies, investigate missing agents, enforce encryption.
  > - Disk Encryption - Verify BitLocker/FileVault compliance, recover encryption keys, investigate encryption failures.


&nbsp;
---
&nbsp;


### 3. [SOC] Identity and Access  

  > Sub Queues
  > - Identity and Access Management - Investigate authentication failures, create or disable accounts, review permissions.
  > - Active Directory Services - Investigate account lockouts, review group memberships, disable compromised accounts.
  > - Multi-Factor Authentication - Reset MFA devices, investigate MFA failures, enroll new users.
  > - Privileged Access Management - Issue administrator access, review privileged sessions, rotate privileged credentials.


&nbsp;
---
&nbsp;


### 4. [SOC] Security Monitoring  

  > Sub Queues
  > - SIEM - Investigate correlation alerts, create dashboards, tune rules, validate events.
  > - SOAR - Develop automation playbooks, validate automated responses, optimize workflows.
  > - Log Management - Verify log ingestion, troubleshoot missing logs, maintain log retention.


&nbsp;
---
&nbsp;


### 5. [SOC] Email Security  

  > Sub Queues
  > - Email Protection - Review spoofing attempts, analyze email headers, block malicious senders.
  > - Email Security Gateway - Investigate phishing campaigns, quarantine malicious emails, update detection rules.


&nbsp;
---
&nbsp;


### 6. [SOC] Application Security  

  > Sub Queues
  > - Web Application Firewall (WAF) - Investigate SQL injection and XSS attempts, tune WAF policies, review attack logs.
  > - Application Security - Investigate authentication issues, review application logs, coordinate with developers.
  > - API Security - Investigate abnormal API usage, review authentication failures, block abusive clients.


&nbsp;
---
&nbsp;


### 7. [SOC] Data Protection Services  

  > Sub Queues
  > - Data Loss Prevention - Investigate policy violations, block sensitive file transfers, review exfiltration attempts.
  > - File Integrity Monitoring - Review file modifications, validate system changes, investigate tampering.
  > - Backup and Recovery - Verify backup integrity, investigate backup failures, coordinate secure recovery after incidents.


&nbsp;
---
&nbsp;


### 8. [SOC] Vulnerability and Compliance Services  

  > Sub Queues
  > - Vulnerability Management - Review scan results, prioritize remediation, verify patch deployment.
  > - Patch Management - Validate patch compliance, investigate failed updates, schedule remediation.
  > - Compliance Monitoring - Generate audit reports, validate security controls, monitor policy adherence.


<br>
<br>

---
&nbsp;


## Service Level Agreements  

<br>

### 1. Critical Incident SLA  

> Active cyberattack or business-critical security incident requiring immediate response.
>
> <br>
> 
> Immediately acknowledge the incident, contain affected systems, isolate compromised hosts, coordinate with Incident Response, notify management, restore services, and conduct post-incident review.


&nbsp;
---
&nbsp;


### 2. High Priority SLA    

> Confirmed or highly suspected security incident requiring urgent investigation.
>
> <br>
>
> Investigate logs, validate indicators of compromise (IOCs), isolate affected endpoints if needed, block malicious IPs/domains, coordinate with IT for remediation.


&nbsp;
---
&nbsp;


### 3. Medium Priority SLA  

> Security event requiring analysis but not considered business critical.
>
> <br>
>
> Review logs, correlate SIEM events, validate alerts, request additional information, recommend remediation if necessary.


&nbsp;
---
&nbsp;


### 4. Low Priority SLA  

> Minor security events or scheduled work that do not require urgent handling. >
>
> <br>
> 
> Review tickets during business hours, perform routine investigations, verify changes, document findings.


&nbsp;
---
&nbsp;


### 5. Informational SLA  

> Non-urgent requests with no immediate security impact.
>
> <br>
> 
> Update documentation, close informational tickets, provide reports, archive evidence.


<br>
<br>

---
&nbsp;


🔴 __CDP Flooding Attack__
Verify:
~~~
!@CoreBABA
show process cpu | inc uti
~~~


<br>
<br>

---
&nbsp;


## ITSM Change Process

### STEP 1 - User reports an issue to [Tier 1 NOC] with the internet slowing down  

__Ticket__  
- Type: Incident  
- To: [NOC] Tier 1 - Monitoring & First Response  
- Service: [NOC] Infrastructure & Application Monitoring  
- SLA: Performance Management SLA  
- Subject: Network Issue  
- Priority: 4 High  

<br>

- Text:   
~~~
The network is very slow, and we are unable to reliably connect to services such as servers and printers. 
Additionally, IP phone extensions/numbers are disappearing intermittently. 
This is impacting our ability to make and receive calls.
~~~


&nbsp;
---
&nbsp;


__Admin [Rivan Cyber] responds to ticket.__  
- Reply  
~~~
Hi user1,

Thank you for reporting this issue.

We are currently investigating the network performance problems and the IP phone registration issue. 
Initial checks show possible network congestion or a connectivity disruption affecting multiple services.

Thank you for your patience while we work to resolve this.

Best regards,
IT Support Team
~~~


<br>
<br>

---
&nbsp;


### STEP 2 - User checks the logs, then discover that Certain Switches have unusually high traffic.

__Change Owner__
- Subject: Network Issue T2 Escalation
- Text: 
~~~
Issue summary:
  Network extremely slow
  Cannot access servers and printers
  IP phones losing registration
  Multiple users affected

Troubleshooting performed by Tier 1:
  Verified issue affects multiple users
  Confirmed both wired/wireless impacted
  Restarted affected workstation(s)
  Verified no local NIC errors
  Basic connectivity tests failed/intermittent

Reason for escalation:
  Issue appears to be infrastructure-related (core switch / firewall / VoIP system). 
  Requires Tier 2 investigation.
~~~


&nbsp;
---
&nbsp;


__Update the User__
- Reply
~~~
Hi user1,

Your ticket has been escalated to our Tier 2 Network Team for further investigation. 
They are currently reviewing the infrastructure components involved.

We will provide updates as soon as more information is available.

Thank you for your patience.
~~~


<br>
<br>

---
&nbsp;


### STEP 3 - Create an ITSM Change with a Work Order for Change [Request] Creation 

__ITSM Change__
- Title: Implement Port Security on Access Switches to Prevent MAC Flooding
- Description: 
~~~
Network is currently slow caused by a traffic congestion from CoreSwitches
CoreSwitches consuming high CPU usage caused by a flood of MAC Addresses.
Switches are currently lacking proper security implementations to prevent L2 attacks.
~~~


<br>


- Category: 4 High
- Impact: 4 High
- Priority: 4 High


&nbsp;
---
&nbsp;


__WorkOrder [REQUEST]__
- Title: Change Request Creation
- Workorder Type: Approval
- Planned Time: +1 Day
- Description:  
~~~
Users reported slow connectivity. Investigation identified high CPU utilization on Cisco access switch due to MAC address table flooding. The switch is vulnerable to MAC flooding attack.
Requesting change approval to implement port security configuration on affected access ports.

Reason for Change:
Proposed Solution:

~~~

 
<br>
<br>

---
&nbsp;


### STEP 4 - Create a Work Order for [Impact Analysis] & Plan Assessment

__ITIL-Based Impact Analysis Framework__  
- Identify the Scope of the Change  
- Identify Stakeholders  
- Assess Impact Levels  
- Identify Risks   
- Analyze Dependencies  
- Document Findings  
- Decision Support  


&nbsp;
---
&nbsp;


__WorkOrder [IMPACT ANALYSIS]__  
- Title: Technical & Risk Assestment / Action Plan  
- Workorder Type: Approval  
- Planned Time: +1 Day  
- Description:  
~~~
Technical Analysis
Enabling port security may:
  Temporarily disrupt connected devices
  Cause port shutdown if misconfigured
  Requires maintenance window
  Minimal downtime expected (per access port configuration)
  
  
Risk Assessment:
Risk	            Likelihood	   Impact	Mitigation
Port shutdown	    Medium	       Medium	Configure restrict mode first
User disconnection	Low	Low	       Change   during maintenance window
Misconfiguration	Low	Medium	   Peer     review config


Impact Scope
Affected Devices:
Cisco Access Switch SW-ACC-01
SW-ACC-02


Affected Users:
Office Floor 2 (~45 users)
No impact to core or WAN
~~~


<br>
<br>

---
&nbsp;


### STEP 5 - Create a Work Order for [Approval/Denial]

__Work Order [APPROVAL/DENIAL]__  
- Title:  CAB Review Approval/Denial  
- Workorder Type: Decision  
- Planned Time: +1 Day  
- Description:  
~~~
Approval Considerations
- Minimal downtime
- Security Imporvement
- Backout Plan

Decision:
 Proposed Maintenance Window
 Schedule: 22:00 - 23:30
~~~


<br>
<br>

---
&nbsp;


### STEP 6 - Create a Work Order for [Implementation]  

__Work Order [IMPLEMENTATION]__  
Title: Implementation Procedure   
- Workorder Type: Workorder  
- Planned Time: +1 Day  
- Description:  
~~~
Pre-implementation Tasks:
Backup Configs:

!@Cisco
copy run start
copy run ftp:

- Save external backup to TFTP
- Notify users of maintenance window
- Confirm monitoring alerts configured

Implementation:
PORT SECURITY
!@CoreTAAS,CoreBABA
conf t
 int fa0/4
  switchport mode access
  switchport port-security
  switchport port-security maximum 1
  switchport port-security violation shutdown
  switchport port-security mac-address sticky
  end

DHCP SNOOPING
!@CoreBABA
conf t
 ip dhcp snooping
 ip dhcp snooping vlan 1,10,50,100
 !
 int po1
  ip dhcp snooping trust
 int fa0/1
  no ip dhcp snooping trust
  exit
 !
 no ip dhcp snooping information option
 !
 interface range fa0/1-12
  ip dhcp snooping limit rate 10
  end
show ip dhcp snooping
show ip dhcp snooping binding


DAI Dynamic Arp Inspection
!@CoreBABA
conf t
 ip arp inspection vlan 1,10,50,100
 !
 int range fa0/2-6,po1
  ip arp inspection trust
 int fa0/1
  no ip arp inspection trust
  end
show ip arp inspection
show ip arp inspection statistics
 
 
Post Implementation
- CPU utilization normalized
- MAC address table state
- No unexpected port shutdowns
- Users confirmed stable connectivity [Ticket Reply]
~~~


<br>
<br>

---
&nbsp;


### STEP 7 - Create a Work Order for Post Implementation Review PIR [Report]  

__Work Order [REPORT/REVIEW]__  
Title: PIR Incident Report  
- Workorder Type: PIR  
- Planned Time: +1 Day  
- Description:  
~~~
Review Date: 3 days - 1 week after change

Port security was configured on the core switches to improve network security by limiting MAC addresses per port and preventing unauthorized device connections.
The objective was to enhance network access control and reduce the risk of rogue devices.

Observations
- CPU usage reduced from 85% → 18%
- No further MAC flooding detected
- No user complaints
- Port violations logged correctly
~~~


<br>
<br>

---
&nbsp;


### STEP 8 - Create Conditions to allow Change States

__A Review on the 5 ITSM Change Process__

1. __REQUEST__

| OBJECT    | SELECTOR | ATTRIBUTE | OPERATOR | VALUE            |
| ---       | ---      | ---       | ---      | ---              |
| WORKORDER | REQUEST  | STATE     | IS       | ACCEPTED         |
|           |          |           |          |                  |
| CHANGE    | 0000xxxx | STATE     | SET      | PENDING APPROVAL |


<br>
<br>


2. __IMPACT ANALYSIS__

| OBJECT    | SELECTOR         | ATTRIBUTE | OPERATOR | VALUE            |
| ---       | ---              | ---       | ---      | ---              |
| WORKORDER | IMPACT ANALYSIS  | STATE     | IS       | ACCEPTED         |
|           |                  |           |          |                  |
| CHANGE    | 0000xxxx         | STATE     | SET      | APPROVED         |


<br>
<br>


3. __APPROVAL__

| OBJECT    | SELECTOR         | ATTRIBUTE | OPERATOR | VALUE            |
| ---       | ---              | ---       | ---      | ---              |
| WORKORDER | APPROVAL         | STATE     | IS       | ACCEPTED         |
|           |                  |           |          |                  |
| CHANGE    | 0000xxxx         | STATE     | SET      | IN PROGRESS      |


<br>
<br>


4. __IMPLEMENTATION__

| OBJECT    | SELECTOR         | ATTRIBUTE | OPERATOR | VALUE            |
| ---       | ---              | ---       | ---      | ---              |
| WORKORDER | IMPLEMENTATION   | STATE     | IS       | ACCEPTED         |
|           |                  |           |          |                  |
| CHANGE    | 0000xxxx         | STATE     | SET      | PENDING PIR      |


<br>
<br>


5. __REVIEW/REPORT__

| OBJECT    | SELECTOR | ATTRIBUTE | OPERATOR | VALUE   |
| ---       | ---      | ---       | ---      | ---     |
| WORKORDER | REVIEW   | STATE     | IS       | CLOSED  |
|           |          |           |          |         |
| CHANGE    | 0000xxxx | STATE     | SET      | SUCCESS |


<br>
<br>

---
&nbsp;


### STEP 9 - Report on every single Work Order to Change states

### 1. __REQUEST__

Terms:  
  - __RFC (Request for Change)__ : Formal proposal  
  - __Change Record__            : The official tracking object  
  - __Change Initiator__         : Person submitting the RFC  
  - __Business Justification__   : Why this change is needed  
  - __Change Category__          : Infrastructure / Application / Network / Security  
  - __Priority__                 : Based on Impact + Urgency  


&nbsp;
---
&nbsp;


### 2. __IMPACT ANALYSIS__
Terms:  
  - __Impact__                  : Business/service effect if change fails
  - __Risk__                    : Likelihood × Impact
  - __Risk Matrix__             : Used to score change
  - __CI (Configuration Item)__ : Component in CMDB
  - __Dependency Mapping__      : Relationship between systems
  - __Rollback Plan__           : Recovery procedure
  - __Mitigation Plan__         : Risk reduction actions


&nbsp;
---
&nbsp;


### 3. __APPROVAL/DENIAL__
Terms:  
  - __CAB (Change Advisory Board)__ : Group reviewing changes  
  - __ECAB__                        : Emergency CAB  
  - __Change Manager__  
  - __Approval Workflow__  
  - __Segregation of Duties__  
  - __Compliance & Audit Trail__  


&nbsp;
---
&nbsp;


### 4. IMPLEMENTATION

Terms:
  - __Change Window__
  - __Maintenance Window__
  - __Work Orders__
  - __Deployment Plan__
  - __Backout Plan__
  - __Release Management__
  - __Technical Validation__

<br>

Control Mechanisms  
  - Real-time monitoring  
  - Peer review  
  - Go/No-Go decision checkpoint  
  - Change freeze policies  
  

&nbsp;
---
&nbsp;

  
### 5. REVIEW/REPORT

Terms:  
  - __PIR (Post Implementation Review)__  
  - __RCA (Root Cause Analysis)__   
  - __Lessons Learned__  
  - __KPI (Key Performance Indicator)__  
  - __Change Success Rate__  
  - __Continuous Improvement__  


<br>
<br>

---
&nbsp;


### 📃 Full Script
<details>
<summary>Show Script</summary>
	
~~~
!@CoreBaba
conf t
 hostname CSW-BABA-#$34T#
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

!@switchport
conf t
 vlan 10
  name WIRELESS-VLAN
 vlan 50
  name VIDEO-VLAN
 vlan 100
  name VOICE-VLAN
 !
 int fa0/1
  switchport mode access
  switchport access vlan 1
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
 int fa0/6
  switchport mode access
  switchport access vlan 100
  end

!@trunking and etherchannel
conf t
 int range fa0/8-10
  channel-group 1 mode active
  channel-protocol lacp
 int po1
  switchport trunk encaps dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
 int range fa0/11-12
  no switchport
  channel-group 10 mode passive
  channel-protocol lacp
 int po10
  no switchport
  no shut
  ip add 10.#$34T#.#$34T#.6  255.255.255.252
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
### 📠 Enterprise Communication   

Cisco Unified Call Manager | [Unified Communications and Collaboration.](https://www.cisco.com/c/en/us/products/unified-communications/index.html)
  - POTS (__Analog__)
  - VOIP (__ePhone__)

<br>

| PBX (Private Branch Exchange) | PSTN (Public Switched Telephone Network)  |
| ---                           | ---                                       |
| Private Carrier               | Public Carrier Infrastructure             |
| Trad (Analog/Digital)         | Analog (POTS)                             |
| IP PBX (VoIP-Based)           | ISDN (Integrated Service Digital Network) |
| Cloud PBX (Hosted)            | T1/E1                                     |


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

### ⚙️ 1. Analog Phones (RJ11)
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


## ⚙️ 2. IP Phones (RJ45) - Cisco Skinny Client Control Protocol (SCCP)
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
 !
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
### 🏨 Establish connectivity to your enterprise.
*How do you gain access to the internet?*

Fortigate Port = #P0RT#

&nbsp;
---
&nbsp;


~~~
!@FW-EDGE
config system global
 set hostname FW-EDGE-#$34T#
 end
config system admin
 edit admin
  set accprofile super_admin
  set vdom root
  set password pass
  next
 edit rivan
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


~~~
Jobs of an EDGE Router:
1. 
2. 
3. 
4. 
5. 

Jobs of a Firewall:
1. 
2. 
3. 
4. 
5. 
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


<br>
<br>

---
&nbsp;


## 🧱 Setup a Firewall (CSR1000v)
*`Ordinary Firewall` vs `NGFW` vs `WAF`*

<br>
<br>

### `fbi.gov`   vs   `neu.edu.ph`   vs   `dpwh.gov.ph`
__Setup CSR1000v__

~~~
!@FWVM-EDGE
conf t
 hostname FWVM-EDGE
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

