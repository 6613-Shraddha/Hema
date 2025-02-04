#Tools to perform footprinting and reconnaissance
Footprinting and reconnaissance are used to collect basic information about the target systems in order to exploit them.
The target information is IP location information, routing information, business information, address, phone number and DNS records.

#1.Recon-ng (Using Kali Linux)
Recong0-ng is a full feature Web Reconnaissance framework used for information gathering purpose as well as
network detection. This tool is written in python, having independent modules, database interaction and other features.
You can download the software from www.bitbucket.org. This Open Source Web Reconnaissance tool requires kali Linux Operating system.

1.Run the Application Recon-ng or open the terminal of Kali-Linux and type recon-ng and hit enter.
2.Enter the command “show modules” to show all independent modules available.
3.You can search for any entity within a module. For example, in above figure, the command “Search Netcraft” is used.
4.To use the Netcraft module, use the command syntax “use recon/domain-hosts/Netcraft” and hit enter.
5.Set the source by the command “set source [domain].” Press enter to continue. Type Run to execute and press enter.

#2.FOCA Tool
FOCA stands for Fingerprinting Organizations with Collected Archives. FOCA tool finds Metadata,
and other hidden information within a document may locate on web pages. Scanned searches can be downloaded and
Analyzed. FOCA is a powerful tool which can support various types of documents including Open Office,
Microsoft Office, Adobe InDesign, PDF, SVG, and others. Search uses three search engines, Google, Bing, and DuckDuckGo.

1.Download the software FOCA from https://www.elevenpaths.com. Now,Go to Project > New Project.
2.Now, Enter the Project Name, Domain Website, Alternate Website (if required), Directory to save the results, Project Date. Click Create to proceed.
3.Select the Search Engines, Extensions, and other parameters as required. Click on Search All Button.
4.Once Search completes, the search box shows multiple files. You can select the file, download it, Extract Metadata, and gather other information like username, File creation date, and Modification.

#3.Windows Command Line Utilities
onsider a network where you have access to a Windows PC connected to the Internet. Using Windows-based tools,
let's gather some information about the target. You can assume any target domain or IP address, in our case, we are using example.com as a target.

1- Open Windows Command Line (cmd) from Windows PC
2 -Enter the command “ Ping example.com ” to ping.
   From the output, you can observe and extract the following information:
➢ Example.com is live
➢ IP address of example.com.
➢ Round Trip Time
➢ TTL value
➢ Packet loss statistics
3- Now, Enter the command “ Ping example.com –f –l 1500 ” to check the value of fragmentation.
   The output shows “ Packet needs to be fragmented but DF set ” which means 150o bits will require being fragmented.
   Let’s try again with smaller value: 1400
   Output again shows “ Packet needs to be fragmented but DF set ” which means 140o bits will require being fragmented.
   Let’s try again with smaller value: 1300
   Output again shows “ Packet needs to be fragmented but DF set ” which means 130o bits will require being fragmented.
   Let’s try again with smaller value: 1200
   The output shows the reply now, which means 120o bits will not require being fragmented.
   You can try again to get the more appropriate fragment value.

#3.a.Tracert using Ping
1. Enter the command “ Tracert example.com ” to trace the target.
   From the output, you can get the information about hops between the source (your PC)
   and the destination (example.com), response times and other information.

#3.b.Tracert
Tracert options are available in all operating system as a command line feature. Visual traceroute, graphical
and other GUI based traceroute applications are also available. Traceroute or Tracert
command results in the path information from source to destination in the hop by hop manner.
The result includes all hops in between source to destination. The result alsoincludes latency between these hops.
Run the below cmd : tracert 200.100.50.3 , tracert 200.100.50.2, tracert 200.100.50.1

#3.c.DNS Zone Transfer Enumeration Using NSLookup
Nslookup (stands for “Name Server Lookup”) is a useful command for getting information from the DNS server.
It is a network administration tool for querying the Domain Name System (DNS)
to obtain domain name or IP address mapping or any other specific DNS record. It is also used to troubleshoot DNS-related problems.

1. Go to Windows command line (CMD) and enter Nslookup and press Enter.
2. Command prompt will proceed to " > " symbol.
3. Enter " server <DNS Server Name> " or " server <DNS Server Address>". server dns.google
4. Enter set type=any and press Enter. It will retrieve all records from a DNS server.
5. Enter ls -d ipspecilist.net this will display the information from the target domain (if allowed).

#3.d.Website Copier tool (HTTrack)
1.Download and Install the WinHTTrack Website Copier Tool from the website http://www.httrack.com.
2.HTTrack Website Copier tool installation.
3.Click Next
4.Enter a Project name, as in our case, Testing_Project.
5.Click on Set Options button.
6.Go to Scan Rules Tab and Select options as required.
7.Enter the Web Address in the field and Click Next. www.example.com
8.Click Next.
9.Click Browse Mirrored Website.
10.Select your favorite web browser.
Observed the above output. Example.com website is copied into a local directory and browsed from there.
Now you can explore the website in an offline environment for the structure of the website and other parameters.

#3.e.Whois Lookup Tools for Mobile – DNS Tools, Whois, Ultra Tools Mobile
"WHOIS" helps to gain information regarding domain name, ownership information. IP Address, Netblock data, Domain Name Servers and other information’s.
Regional Internet Registries (RIR) maintain WHOIS database. WHOIS lookup helps to find out who is behind the target domain name.
1- Go to the URL https://www.whois.com/
2- A search of Target Domain google.com

#3.f.Smart Whois
1.can download software “SmartWhois” from www.tamos.com for Whois lookup as shown
2. Search for the target domain

#3.g.eMailTracker Pro
eMailTrackerPro is a Windows based email tracker that can be used to monitor employees, senders and recipients.
1.Click on Trace Headers/Trace email address and enter the Message Header and click Okay.
The Status of the Trace will be shown inside Trace Reports

#1.b Scan the network using the following tools:
1. Hping2 / Hping3
Hping is a command-line TCP/IP packet assembler and analyzer tool that is used to send customized TCP/IP packets
and display the target reply as ping command display the ICMP Echo Reply packet from targeted host.
Steps:
    1. To create an ACK packet:root@kali:~# hping3 –A 192.168.0.1
    2. To create SYN scan against different ports:root@kali:~# hping3 -8 1-600 –S 10.10.50.202
    3. To create a packet with FIN, URG, and PSH flags setsroot@kali:~# hping3 –F –P -U 10.10.50.202

2. Advanced IP Scanner
Advanced IP Scanner is a fast and powerful network scanner with a user-friendly interface.
In seconds, Advanced IP Scanner can locate all computers on your wired or wireless local network and scan their ports
Steps:
    1.192.168.0.90-110

3.Angry IP Scanner
Angry IP Scanner (or simply ipscan) is an open-source and cross-platform network scanner designed to be fast and simple to use.
It scans IP addresses and ports as well as has many other features.
Steps:
  IPRange-  195.80.116.0 to 195.80.116.225
  Hostname  e-estonia.com   IP: /24

4. Masscan
MASSCAN is TCP port scanner which transmits SYN packets asynchronously and produces results similar to nmap, the most famous port scanner
Steps:
    root@kali:~# masscan -p22,80,445 192.168.1.0/24
5. CurrPorts
   Steps:
       1. Run the application Currports on Windows Server 2016 and observe theprocess
       2.Run the HTTP Trojan created in the previous lab
       The new process is added to the list.
       You can observe the process name, Protocol, Local and remote port and IP address information.
       3. For more detail, right click on httpserver.exe and go to properties
       Properties are showing more details about tcp connection.
       4. Go to Windows 7 machine and initiate the connection as mentioned in the previous lab using a web browser.
       Connection successfully established.
       5. Back to Windows Server 2016, Kill the connection
       6. To verify, retry to establish the connection from windows 7.
6. Colasoft Packet Builder software enables to create the customized network packets.
   These Customized Network packets can penetrate the network for attacks.
   Steps:
       1. Click on Add
       2. Select the Packet type from the drop-down option.

#Practical 3
a. Perform Enumeration using the following tools:
    i. Nmap
NMAP, as we know, is a powerful networking tool which supports many features andcommands.
Operating System detection capability allows to send TCP and UDP packet and observe the response from the targeted host
Steps:
    target = 192.168.0.109
    Command = nmap -O -v 192.168.0.109

b. NetBIOS Enumeration Tool
NetBIOS stands for Network Basic Input Output System. It Allows computer
communication over a LAN and allows them to share files and printers. NetBIOS names are used to identify network devices over TCP/IP (Windows).
Steps:
    netstat -a
    
c.SuperScan 
SuperScan is a multi-functional tool that will help you manage your network and make sure your connections
and TCP ports are working as well as they should be. One of the best features or advantages of this tool is
just how quickly it works. The scans are made very rapidly and faster than with most other scanning tools out there.

steps: 127.0.0.1

d. Hyena
Hyena is GUI based, NetBIOS Enumeration tool that shows Shares, User login information and other related information

e. SoftPerfect Network Scanner Tool
SoftPerfect Network Scanner can ping computers, scan ports, discover shared folders and retrieve practically any information about network devices via WMI, SNMP, HTTP, SSH and 
PowerShell.
Steps:
    IPv4 From 192.168.1.0 To 192.168.1.255

#Practical 4
Perform the System Hacking using the following tools:
i. Winrtgen
Steps:
    1.To generate rainbow tables first we will have to modify the properties of WinRTGen according to our need,
      and to do so Click on “Add Table“. After this, a new box will appear named “Rainbow Table Properties”
    2.In the “Rainbow Table Properties” window we have the option to modify settings in order to generate rainbow tables according to our needs.
    The following properties can be modified: • Hash: The type of encryption we want the rainbow table to be generated. For example MD5, MD4, SHA1, etc.
    3. After assigning the values to the properties according to our needs click on “Benchmarks”. This will show the estimated time, Hash speed, Step speed, Table Pre-computing time, etc.
      that will be required to generate the Rainbow Table according to assigned properties.
    4. After “Benchmark” click on “Ok”. This will add the Rainbow Table to the queue in the main window of WinRTGen
    5. After this click on “Rainbow Table” You want to start processing and click “OK” .
    6. After clicking on ‘OK’ the WinRTGen” will start generating a rainbow table.
    7. After completion, the window will appear as follows.
    8. This table will be saved to your WinRTGen Directory.

ii.  PWDump
The Security Account Manager, or SAM for short, controls all user accounts and passwords. Every password is hashed before being saved in SAM. Passwords that are hashed and saved in SAM can be retrieved in the registry; simply open the Registry Editor and navigate to HKEY LOCAL MACHINESAM. SAM is located in C:\Windows\System32\config. 
This utility was created by Tarasco. This utility dumps the system’s SAM file’s credentials after extracting it.
Steps:
    1. Download the pwdump7
    2. cd to that dir till pwdump7
    3. run PwDump7.exe
    
iii. NTFS Stream Manipulation
NTFS is a filesystem that stores files utilizing two data streams known as NTFS data streams, as well as file attributes.
The first data stream contains the security descriptor for the file to be stored, such as permissions, while the second contains the data
contained within a file
Steps:
    1. Open the terminal and type the following command to create a file named file_1.txt.
    echo "this is file no 1" > file_1.txt
    2. Now, type the following command to write to the stream named secret.txt.
    echo "this is a hidden file inside the file_1.txt" > file_1.txt:secret.txt
    3. Dir
    4. The following command can be used to view or modify the stream hidden in file_1.txt
    cmd - notepad file_1.txt:secret.txt
    Hiding Trojan.exe in note.txt file stream:
    5. C:\test>type Trojan.exe > note.txt:Trojan.exe
    6. After hiding trojan.exe behind note.txt, we need to create a link to launch the trojan.exe file from the stream. T
    he following command is used to create a shortcut in the stream.
    C:\test>mklink game.exe note.txt:Trojan.exe
    7. Type game.exe to run the trojan that is hidden behind the note.txt. Here, game.exe is the shortcut created to launch trojan.exe.

iv. ADS Spy
AdSpy offers the most search options of any Ad Intelligence Tool, so you can find the data you want, how you want. Search in the usual way: ad text,
URL, page name. Search true data from user reactions in advert comments.
Steps:
    1. Open ADS Spy application and select the option if you want to: 
       • Quick Scan
       • Full Scan
       • Scan Specific Folder
    2. As we store the file in the Document folder, Selecting Document folder to scan particular folder only.
    3. Select an Option, if you want to scan for ADS, click “Scan the system for ADS”/ or click removes button to remove the file
    4. As shown in the figure below, ADS Spy has detected the Testfile.txt:hidden.txt file from the directory.

v. Snow
1. Create a text file with some data in the same directory where Snow Tool is installed.
2. Go to Command Prompt to the Snow where download
   Change the directory to run Snow tool
3. Snow –C –m “The Password is 12345” –p “password123” Hello.txt HelloWorld.txt
4. Go to the directory; you will a new file HelloWorld.txt. Open the File
5. Recovering Hidden Information. On destination, Receiver can reveal information by using the command: Snow –C –p “password123” HelloWorld.txt

vi. Quickstego
Image Steganography using QuickStego
1. Open QuickStego Application
2. Upload an Image. This Image is term as Cover, as it will hide the text.
3. Enter the Text or Upload Text File
4. Click Hide Text Button
5. Click Save Image . This Saved Image containing Hidden information is termed as Stego Object.

Recovering Data from Image Steganography using QuickStego
1. Open QuickStego
2. Click Get Text
3. Open and Compare Both Images
Left Image is without Hidden Text; Right Image is with hidden text

vii. Clearing Audit Policies
Enabling and Clearing Audit Policies
Steps:
    1. To check command’s available option Enter C:\Windows\system32> auditpol /?
    2. Enter the following command to enable auditing for System and
       Account logon: -C:\Windows\system32>auditpol /set /category:"System","Accountlogon" /success:enable /failure:enable
    3. To check Auditing is enabled, enter the command
       C:\Windows\system32>auditpol logon","System"/get /category:"Account
    4. To clear Audit Policies, Enter the following commandC:\Windows\system32>auditpol /clear
       Are you sure (Press N to cancel or any other key to continue)?Y
    5. To check Auditing, enter the command
       C:\Windows\system32>auditpol /get /category:"Account logon","System"

viii. Clearing Logs
1. Go to Kali Linux Machine
2. Open the /var directory
3. Go to Logs folder
4. Select any log file
5. Open any log file; you can delete

Practical 5
1. Use wireshark to sniff the network.
Wireshark is a GUI-based packet capture program. As noted, it comes with some command-line programs. There are a lot of advantages to using Wireshark.
Steps:
    1. Start Wireshark. Under the “Capture” header, select the “Interface List” option; or click on the “Interfaces” button on the toolbar:
        This will bring up a list of network interfaces that Wireshark is able to capture packets from:
    2. Select the network adapter (wired or wireless) that you are currently using to connect to the Internet, and hit the “Start” button.
    3. Wireshark is now capturing live network activity on your network interface.
       Notice that the list of packets is color-coded to highlight different types of network traffic.
       • Open your web browser and navigate to a few random web pages - observe that the network packets corresponding
         to your web browsing activity are captured and show up in Wireshark as well.
       • By default, the list of captured packets will keep scrolling automatically during a live capture.
         You can toggle this on/off using the AutoScroll toggle button in the toolbar.
       • After letting the capture run for a couple of minutes, press the stop capturebutton.  Do not close this capture session.
    4. Filtering the Packet List
       Wireshark allows us to filter the list based on different criteria using the “Filter” toolbar
       In the filter toolbar, type “http” and then click on “Apply”. The window will now list only captured packets related to HTTP traffic
    5. Examining HTTP Traffic
       The HTTP traffic that occurs during web browsing.
       • Stop and close any capture that you may have open, and start a new capture.
       • Set the filter to show only HTTP traffic.
    6. Start with the HTTP request sent from your web browser.
       • In your web browser, navigate to some webpage like http://www-scf.usc.edu/~csci571/Special/HTTP/proxy.html.
       • In the top frame of the Wireshark main window, look for the packet thatcorresponds to your request.
         This contains the URL in the “Info” section. Select this packet.
       • In the middle frame of the Wireshark window, expand the “Hypertext Transfer Protocol” section.
         Notice the details given for the:o GET requesto Host o User-Agent o Acceptso cookie o etc
    7. In the top frame of the Wireshark main window, find and select the “HTTP/1.1 200 OK” packet immediately
       below the request for proxy.html. This is the response containing the requested web page
    8. Again, expand the “Hypertext Transfer Protocol” section. Notice the details given foro Cache-Controlo Content-Typeo Server o Etc

2. Use SMAC for MAC Spoofing.
SMAC is a MAC address changer that has a simple-to-use graphical interface that enables the less experienced
user all the way up to the guru to change a piece of hardware’s MAC address.
Steps :
    1. Search the KLC in Start menu
    2. Click on that folder and you will see SMAC 2.0. Click on that launcher and the SMAC main window (Figure A) will open
    3. In the main window there is a check box that tells SMAC to show only active hardware. This checkbox is checked by default.
       Uncheck that box and your listing will grow, depending on the hardware on your machine
    4. Let’s change the MAC address of the Wired Marvell Yukon PCI-E Faster Ethernet Controller.
       To do this, select that entry from the list and click the Random button.
       The new, random MAC address is displayed in the New Spoofed MAC Address section.
    5. If you know you want to spoof your MAC address to that of a specific manufacturer you can
       select a different manufacturer from the drop-down list. When you make this selection, the address listed will change.
       You can keep hitting Random until you get an address you like (or you can just take the first random address you get).
    6. Once you have your address, select the Options menu and make sure Automatically Restart Adapter is checked.
       Once that is checked, hit the Update MAC Address button and the new MAC address will be applied.

3. Use Caspa Network Analyser.
When we correctly deployed Capsa, we cannot wait to start our first capture right away. Capsa 
7's new Start Page guides us start an accurate capture mission step by step:
steps:
    1. Double-click icon on the desktop.
    2. In the Start Page, select your NICs (multiple selections available) in the Capture panel first.
    3. Select any Network Profile in the Network Profile panel.
    4. Select Full Analysis in the Analysis Profile panel.
    5. Click the big Run button to start a capture right away.


Practical 6
a. Use Social Engineering Toolkit on Kali Linux to perform Social Engineering using Kali Linux.
We are using Kali Linux Social Engineering Toolkit to clone a website and send clone link to victim.
Once Victim attempt to login to the website using the link, his credentials will be extracted from Linux terminal.
Steps:
    1. Open Kali Linux
    2. Go to Application
    3. Click Social Engineering Tools
    4. Click Social Engineering Toolkit
    5. Enter “Y” to proceed.
    6. Type “1” for Social Engineering Attacks
    7. Type “2” for website attack vector
    8. Type “3” for Credentials harvester attack method
    9. Type “2” for Site Cloner
    10. Type IP address of Kali Linux machine ( 10.10.50.200 in our case).
        IP address for the post back in Harvester/Tabnabbing [10.10.50.200]
    11. Type target URL
        Enter the url to clone:https://www.example.com
    12. Now, http://10.10.50.200 will be used. We can use this address directly, but it is not an effective way in real scenarios.
        This address is hidden in a fake URL and forwarded to the victim. Due to cloning, the user could not identify the fake website unless
        he observes the URL. If he accidentally clicks and attempts to log in, credentials will be fetched to Linux terminal.
        In the figure below, we are using http://10.10.50.200 to proceed.
    13. Login using username and PasswordUsername: admin
        Password: Admin@123
    14. Go back to Linux terminal and observe.


b. Perform the DDOS attack using the following tools:
i. HOIC
   High Orbit Ion Cannon (HOIC) is a free, open-source network stress application developed by Anonymous, a hacktivist collective,
   to replace the Low Orbit Ion Cannon (LOIC). Used for denial of service (DoS) and distributed denial of service (DDoS) attacks,
   it functions by flooding target systems with junk HTTP GET and POST requests.
   The application can open up to 256 simultaneous attack sessions at once, bringing down a target system by sending a continuous stream of
   junk traffic until legitimate requests are no longer able to be processed

ii. LOIC
The LOIC was originally developed by Praetox Technologies as a stress testing application before becoming available within the public domain.
The tool is able to perform a simple dos attack by sending a large sequence of UDP, TCP or HTTP requests to the target server.   
Step 1: Run the tool.
Step 2: Enter the URL of the website in The URL field and click on Lock O. Then, select attack method (TCP, UDP or HTTP). I will recommend TCP to start.
        These 2 options are necessary to start the attack.
Step 3: Change other parameters per your choice or leave it to the default. Now click on the Big Button labeled as “IMMA CHARGIN MAH LAZER.”
        You have just mounted an attack on the target.

 e.Use the following tools to protect attacks on the web servers:
  i. ID Server
   Download and install ID Server tool.
   1. Enter URL or IP address of the target server
   2. Enter the Query The Server/button.
   3. Copy the Extracted information.
    Information such as Domain name, open ports, Server type and other information are extracted.


Practical 10
Use the following tools for cryptography
i. HashCalc
Calculating MD5 value using HashCalc
1. Open HashCalc tool.
2. Create a new file with some content in it as shown below.
3. Select Data Format as “File” and upload your file
4. Select Hashing Algorithm and Click Calculate
5. Now Select the Data Format to “Text String” and Type “IPSpecialist…” into Data filed and calculated MD5.
   MD5 Calculated for the text string “IPSpecialist…” is “a535590bec93526944bd4b94822a7625”
6. Now, let's see how MD5 value is changed from minor change
  Just lowering the case of single alphabet changes entire hashing value. MD5 Calculated for
  the text string “IPspecialist…” is “997bd71ad0158de71f6e97a57261b9a7”

ii. Advanced Encryption Package
1. Download and Install Advance Encryption Package Latest Version. In this Lab, we are using Advanced Encryption Package 2014 and
   2017 to ensure compatibilities on Windows 7 and Windows 10.
2. Select the File you want to Encrypt.
3. Set password
4. Select Algorithm
5. Click Encrypt
6. Compare both Files
7. Now, After forwarding it to another PC, in our case, in Windows 10 PC, decrypting it using Advanced Encryption package 2017.
8. Enter password
9. File Successfully decrypted.

iii.TrueCrypt
TrueCrypt is a leading disk encryption software program that lets you secure disk partitions on your Windows computer.
There are times when your hard drive is accessible by other people, such as in an office setting, while travelling, or at home.
The data you have on the PC may be vulnerable to attack and compromise your privacy. However, in these moments of risk,
TrueCrypt may just be the tool to protect your data.

1. Click Next two times on the following screens to create an encrypted file container with a standard TrueCrypt volume (
  those are the default options). Click Select File and browse to a location where you want to create the new container.
  Make sure it is not in the Dropbox folder if Dropbox is running. You can name the container anyway you want, e.g. holiday2010.avi.
2.Click Next on the encryption options page unless you want to change the encryption algorithm or hash algorithm.
  Select the volume size on the next screen. I suggest you keep it at a few hundred Megabytes tops.
3. You need to enter a secure password on the next screen. It is suggested to use as many characters as possible (24+) with upper and
  lower letters, numbers and special characters. The maximum length of a True Crypt password is 64 characters.
4. Now it is time to select the volume format on the next screen. If you only use Windows computers you may want to select NTFS as the file system.
If you use others you may be better of with FAT. Juggle the mouse around a bit and click on format once you are done with that.

iv. CrypTool
Cryptool is a free e-learning tool to illustrate the concepts of cryptography. Try Various Encryption/Decryption algorithms.



       
