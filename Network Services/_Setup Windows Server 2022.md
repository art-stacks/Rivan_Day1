
<!-- Monitor Number = #$34T# -->


## Requirements
1. Windows Server 2022 Evaluation ISO
2. Type 2 Hypervisor (Such as VMWare Workstation, VirtualBox, Hyper-V, etc)

<br>
<br>

---
&nbsp;

## Setup the Virtual Machine (VMware Workstation)
1. Select __New Virtual Machine__

<br>

![wInstall_01](../img/01_Win2022.png)

&nbsp;
---
&nbsp;

2. For the type of configuration, choose __Typical (recommended)__

<br>

![wInstall_02](../img/02_Win2022.png)

&nbsp;
---
&nbsp;

3. For guest operating system installation, choose __I will install the operating system later.__

<br>

![wInstall_03](../img/03_Win2022.png)

&nbsp;
---
&nbsp;

4. The guest operating system will be __Microsoft Windows__ version __Windows Server 2022__

<br>

![wInstall_04](../img/04_Win2022.png)

&nbsp;
---

5. Keep the Disk Capacity to __60 GB__. Then, make sure to select __Split virtual disk into multiple files.__

<br>

![wInstall_05](../img/05_Win2022.png)

&nbsp;
---
&nbsp;

6. Select __Customize Hardware..__

<br>

![wInstall_06](../img/06_Win2022.png)

&nbsp;
---
&nbsp;

7. Set the following:
  - Memory: __8GB__
  - Processors: __4 Processor, 2 Cores/Per__
  - CD/DVD:__Use ISO Image File (Attach the ISO of Windows Server EVAL 2022)__
  - Network Adapter: __Bridge (Replicate)__
    - Add an additional Network Adapter:
      - __Network Adapter 2: NAT__
  Then select __Close__

<br>

![wInstall_07](../img/07_Win2022.png)

&nbsp;
---
&nbsp;

8. Finally, __Finish__ the setup

<br>

![wInstall_08](../img/08_Win2022.png)

&nbsp;
---
&nbsp;

9. Before we can start the VM, we will __add 4 additional Hard Disks__ for another lab. Select __Edit Virtual Machine Settings__

<br>

![wInstall_09](../img/09_Win2022.png)

&nbsp;
---
&nbsp;

10. __Add__ Hardware. Then, select __Hard Disk__.

<br>

![wInstall_10](../img/10_Win2022.png)

&nbsp;
---
&nbsp;

11. Select the following settings:
  - Disk Type: __NVMe__
  - Select a Disk: __Create a new virtual disk__
  - Maximum Disk size: __6 GB__. Then __Split virtual disk into multiple files__
  - Leave the name at default.
  - Then __Finish__

Simply repeat this process to add 3 more hard disks with the following sizes: __7 GB__, __8 GB__, __9 GB__

Expected output:

<br>

![wInstall_11](../img/11_Win2022.png)

&nbsp;
---
&nbsp;

12. Finally, we can __Power On__ the virtual machine.
> [!Warning]
> Once the virtual machine is powered on, you __MUST__ click on the __Center__ of the VM. Then, press __Enter__ otherwise you will have to restart the VM.

<br>

![wInstall_12](../img/12_Win2022.png)

&nbsp;
---
&nbsp;

13. When booted successfully, leave the language to default. Then, select __Next__ and __Install Now__

<br>

![wInstall_13](../img/13_Win2022.png)

&nbsp;
---
&nbsp;

14. For Operationg system, select the 2nd option __Windows Server 2022 Standard Evaluation (Desktop Experience)__

<br>

![wInstall_14](../img/14_Win2022.png)

&nbsp;
---
&nbsp;

15. __Accept__ the license terms.

<br>

![wInstall_15](../img/15_Win2022.png)

&nbsp;
---
&nbsp;

16. Choose __Custom Install__

<br>

![wInstall_16](../img/16_Win2022.png)

&nbsp;
---
&nbsp;

17. Select __Drive 0__. Then, simply wait for the installation to finish.
> [!Note]
> The system will restart after installation.

<br>

![wInstall_17](../img/17_Win2022.png)
![wInstall_18](../img/18_Win2022.png)

&nbsp;
---
&nbsp;

18. Set a password for the Administrator account. __C1sc0123__

<br>

![wInstall_19](../img/19_Win2022.png)

&nbsp;
---
&nbsp;

19. Use CTRL + ALT + INSERT to login to the VM

<br>
<br>

---
&nbsp;

## Setup Winserver 2022 for network services.
### 1. Turn off the firewall

~~~powershell
@powershell
set-netfirewallprofile -name public,private,domain -enabled false
~~~

Verify:

~~~powershell
@powershell
get-netfirewallprofile
~~~

&nbsp;
---
&nbsp;

### 2. Set proper IP addressing.
Open the __Run__ window by pressing `Windows + R` button. Then enter `ncpa.cpl`

<br>

![wInstall_20](../img/20_Win2022.png)

<br>

First off, we need to verify which Network Adapter is connected to __NAT__, and which one is connected to __Bridge__.
To achieve this, __right click__ on one of the LAN Cards of the virtual machine. Then, select __Disconnect__.

<br>

![wInstall_21](../img/21_Win2022.png)

When disconnected, one of the Network Adapters within the Virtual Machine will be __unplugged__

<br>

![wInstall_22](../img/22_Win2022.png)

That means, the LAN card we disconnected is the one that's connected to the VMs network adapter. In this example, the __Bridged LAN__ was disconnected, which means the __Ethernet0__ is the bridged connection.

For the sake of convenience, rename the network adapter as follows:
| LAN Card | WinServer Network Adapter |
| ---      | ---                       |
| Bridged  | TunayNaLAN                |
| NAT      | TunayNaWIFI               |

> [!Note]
> Don't forget to reconnect the LAN Card

Expected output:

<br>

![wInstall_23](../img/23_Win2022.png)

<br>
<br>

Now that we know which Network Adapter is which, we need to set a static IP address on __TunayNaLAN__

1. Right click __TunayNaLan__ and select __Properties__.

<br>

![wInstall_24](../img/24_Win2022.png)

<br>
<br>

2. Select __Internet Protocol Veriosn 4 (TCP/IPv4)__, then __Properties__.
Set the following settings:
  - __Use the following IP address:__
    - IP address: __10.#$34T#.1.8__
    - Subnet Mask: __255.255.255.0__
    - Default Gateway: __Leave this blank__

  - __Use the following DNS server address:__
    - Preffered DNS Server: __127.0.0.1__
    - Alternate DNS Server: __Leave this blank__

<br>

![wInstall_25](../img/25_Win2022.png)

3. Next, select __Advanced__ then choose the __DNS__ tab.
  - Under DNS Suffix for this connection: __azure#$34T#.com__
  - Then, under Append these DNS suffixes (in order), select __Add__.
    - Simply add the exact DNS Suffix that was previously assigned: __azure#$34T#.com__

Expected output:

<br>

![wInstall_26](../img/26_Win2022.png)

Confirm the changes by selecting __Ok__ on each open window.

4. Next, we need to set static routes so that the virtual machine can connect to not only the LAN, but including other classmate's network.
~~~cmd
@cmd
ip route 10.0.0.0 mask 255.0.0.0 10.#$34T#.1.4
ip route 200.0.0.0 mask 255.255.255.0 10.#$34T#.1.4
~~~

5. Verification - To ensure that everything was done correctly.
~~~cmd
@cmd
ipconfig
~~~

The assigned domain name __azure#$34T#.com__ must appear on the network adapters.

~~~cmd
@cmd
ping 10.#$34T#.1.4
ping 10.#$34T#.1.2
ping 10.#$34T#.100.8
ping 200.0.0.#$34T#
~~~

Pings must be successful

&nbsp;
---
&nbsp;

### 3. Download  necessary files
Now that IP addressing is in place, the Virtual Machine must have access to both the internet and the LAN.

1. Open a browser and go to: https://www.github.com/art-stack/Rivan_Day1
Download the repository

<br>

![wInstall_27](../img/27_Win2022.png)

After download, you __MUST__ move the repository to the __C: Drive__ then __extract__. 

> [!Note]
> This is to avoid permission errors with the web server later.

2. Next, search and download the following apps:
  - [Hmail Server](https://www.hmailserver.com/)
  - [Thunderbird](https://www.thunderbird.net/en-US)


### 4. Rename the Windows Server 2022 Virtual Machine
Security 101: *DO NOT name your servers based on their purpose.*

~~~powershell
rename-computer snoopy#$34T#
~~~

Then restart the VM to apply the changes.

~~~powershell
restart-computer
~~~

<br>
<br>
<br>

That's about it. Your Windows Server 2022 Virtual Machine is now ready for labbing.
