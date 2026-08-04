
<!-- Your monitor number = #$34T# -->

### Set WinServer VM as a DNS server

Make sure VM has 2 NetAdapters:
| Network Adapter  |                     |
| ---              | ---                 |
| NetAdapter       | NAT                 |
| NetAdapter 2     | Bridged (Replicate) |

<br>

On the real PC, set the DNS of VMNet8 as the IP of WinServer VM's NAT IP (208.8.8.x)

<br>
<br>

---
&nbsp;

# 🌐 Domain Name System
*Connect to websites through IP addresses alone.*

~~~cmd
@cmd
ping google.com         ___.___.___.___
ping cisco.com          ___.___.___.___
ping rivanit.com        ___.___.___.___
~~~

&nbsp;
## 📋 Task 01 - Set up your own DNS Server.

### 📦 Install Windows DNS Server
~~~Powershell
@powershell
Install-WindowsFeature -name dns -includeManagementTools
~~~

<br>

### 📂 Create a Zone File for __rivan#$34T#.com__
  - Forward & Reverse lookup zones
    - DNS Records

~~~cmd
@cmd
ping ns.nemsu.com
ping www
ping imap
ping pop
ping smtp
~~~

<br>
<br>

---
&nbsp;

### 🎯 Exercise 01: Configure additional DNS records for the following devices:

| Alias |     | Device       | Host |     | Device       | Host |
| ---   | --- | ---          | ---  | --- | ---          | ---  | 
| Web   |     | __CoreBABA__ | cb   |     | __WLC__      | wc   |
| SMTP  |     | __CoreTaas__ | ct   |     | __Cam6__     | c6   |
| IMAP  |     | __CUCM__     | cm   |     | __Cam8__     | c8   |
| POP3  |     | __EDGE__     | ed   |     | __Ephone1__  | e1   |
|       |     | __AP__       | ap   |     | __Ephone2__  | e2   |

<br>

<details>
<img width="791" height="572" alt="image" src="https://github.com/user-attachments/assets/cb06cdca-2878-4640-9d28-2f5af0732dc4" />
</details>

<br>
<br>

---
&nbsp;

### 🎯 Exercise 02: Configure DNS for __`itsolutions#$34T#.com`__ with the following DNS records:

| Alias |     | Device       | Host     |     | Device       | Host     |
| ---   | --- | ---          | ---      | --- | ---          | ---      | 
| Web   |     | __CoreBABA__ | coreprim |     | __WLC__      | wifictrl |
| SMTP  |     | __CoreTaas__ | coresec  |     | __Cam6__     | cam6     |
| IMAP  |     | __CUCM__     | callm    |     | __Cam8__     | cam8     |
| POP3  |     | __EDGE__     | edge     |     | __Ephone1__  | ep1      |
|       |     | __AP__       | wifiap   |     | __Ephone2__  | ep2      |

<br>

<details>
  <img width="790" height="568" alt="image" src="https://github.com/user-attachments/assets/78d9b21d-4692-4e98-adeb-23a68419b62c" />
</details>

<br>
<br>

---
&nbsp;

## 📋 Task 02 - Create a website for __rivan#$34T#.com__

### 📦 Install Windows Web Server
~~~Powershell
@powershell
Install-WindowsFeature -name Web-Server -includeManagementTools
~~~

<br>

### 📂 Create the website

| Site name           | Physical path | Bindings |
| ---                 | ---           | ---      |
| __rivan#$34T#.com__ | officebiz     | All:80   |

<br>

<details>
  <img width="1080" height="772" alt="image" src="https://github.com/user-attachments/assets/c1a6cef6-e9c2-4af8-9cef-6b08ab497958" />
</details>

<br>
<br>

---
&nbsp;

### 🎯 Exercise 03: Configure a website for __`itsolutions#$34T#.com`__ using the web directory, cellbiz

| Site name                 | Physical path | Bindings |
| ---                       | ---           | ---      |
| __itsolutions#$34T#.com__ | cellbiz       | All:80   |

<br>

<details>
  <img width="1073" height="769" alt="image" src="https://github.com/user-attachments/assets/1e27136e-490c-472d-9c42-c0099cb1c7a7" />
</details>

<br>
<br>

---
&nbsp;

### 📦 Powershell Script for DNS Zones & Records
~~~powershell
@powershell
add-DnsServerPrimaryZone -Name "rivan#$34T#.com" -ZoneFile "rivan#$34T#.com.dns"

﻿add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name ns -ipv4address 10.#$34T#.1.7
add-DnsServerResourceRecord -zonename rivan#$34T#.com -Cname -name www -hostname ns.rivan#$34T#.com
add-DnsServerResourceRecord -zonename rivan#$34T#.com -Cname -name imap -hostname ns.rivan#$34T#.com
add-DnsServerResourceRecord -zonename rivan#$34T#.com -Cname -name pop -hostname ns.rivan#$34T#.com
add-DnsServerResourceRecord -zonename rivan#$34T#.com -Cname -name smtp -hostname ns.rivan#$34T#.com

add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name cb -ipv4address 10.#$34T#.1.4
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name ct -ipv4address 10.#$34T#.1.2
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name cm -ipv4address 10.#$34T#.100.8
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name ed -ipv4address 10.#$34T#.#$34T#.1
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name e1 -ipv4address 10.#$34T#.100.101
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name e2 -ipv4address 10.#$34T#.100.102
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name c6 -ipv4address 10.#$34T#.50.6
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name c8 -ipv4address 10.#$34T#.50.8
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name ap -ipv4address 10.#$34T#.10.3
~~~

&nbsp;
---
&nbsp;

### 📦 Powershell Script for Website configuration
~~~powershell
@powershell
New-Website -name "rivan#$34T#.com" -hostheader "www.rivan#$34T#.com" -physicalpath "d:\webs\officebiz"
~~~

<br>
<br>

---
&nbsp;

## 🌐 Recursive Resolver
*What happens when a dns server does not know how to map a domain name?*

- DNS stub resolver
 - Authoritative Root server
 - TLD
 - SLD
 - NS

<br>

~~~
@cmd
nslookup -type=NS com. a.root-servers.net
nslookup -type=NS rivanit.com d.gtld-servers.net
nslookup -type=NS rivanit.com ns1.dns-parking.com
~~~

<br>
<br>

---
&nbsp;

### 🎯 Exercise 04: Use NSLookup to determine the DNS servers and record information for __`en.wikipedia.org`__ __`www.facebook.com`__

~~~
@cmd
nslookup -type=NS ___  ________________
~~~

<br>
<br>

---
&nbsp;

### 📦 Powershell Script to Remove DNS Forwarders
~~~powershell
Remove-DnsServerForwarder -ipAddress 10.11.1.10, 10.12.1.10, 10.21.1.10, 10.22.1.10, 10.31.1.10, 10.32.1.10, 10.41.1.10, 10.42.1.10,10.51.1.10, 10.52.1.10, 10.61.1.10, 10.62.1.10, 10.71.1.10, 10.72.1.10, 10.81.1.10, 10.82.1.10, 10.91.1.10, 10.92.1.10 -PassThru
~~~

&nbsp;
---
&nbsp;

### 📦 Powershell Script to Add DNS Forwarders
~~~powershell
Add-DnsServerForwarder -ipAddress 10.11.1.10, 10.12.1.10, 10.21.1.10, 10.22.1.10, 10.31.1.10, 10.32.1.10, 10.41.1.10, 10.42.1.10,10.51.1.10, 10.52.1.10, 10.61.1.10, 10.62.1.10, 10.71.1.10, 10.72.1.10, 10.81.1.10, 10.82.1.10, 10.91.1.10, 10.92.1.10 -PassThru
~~~

<br>

>[!NOTE]
>You do not forward queries to yourself

<br>
<br>

---
&nbsp;

### Secondary Zone & Zone Transfer
1. Create Secondary Zone for each local DNS Server
  - Specify the Primary zone that will be used for Zone transfer

2. Right click the Primary Zone you wish to share to other DNS Servers and Allow Zone Transfer to any server. Make sure it also notifies the IPs for updates.

<br>
<br>

---
&nbsp;

### 🔢 Set a DNS server for Windows, Linux, & Cisco

~~~
@Cisco
conf t
 ip domain lookup
 ip name-server 10.#$34T#.1.10
 end
ping ns.ccna#$34T#.com
~~~

~~~
@Linux
nano /etc/resolve.conf

10.#$34T#.1.10

ping ns.ccna#$34T#.com
~~~
<br>
<br>

---
&nbsp;

## 📋 File Transfer
Upload configurations to FTP Server. (CoreTaas, CoreBaba, CUCM, EDGE)

~~~
@Cisco
copy run ftp:10.#$34T#1.8
~~~

<br>

How to copy the current IOS of a Cisco Switch for backup.

~~~
@Cisco
archive upload-sw ftp://ccna#$34T#.com
~~~
<br>
<br>

---
&nbsp;

# 📧 Mail Server System Design
*How are emails recieved and sent? __IMAP__, __POP3__, __SMTP__*

Create an MX record on the Zone file.
	Install .NET Framework 3.5 Features
 

### Vulnerabilities of Hosting Mail Servers

### Secure Mail Server
DMARC
SSL Certificate






### Exercise - Create users and emails for ccna#$34T#.com and bpiph#$34T#.com

  User1: ac
  Pass: C1sc0123
  
  User: Support

  Pass: C1sc0123





















