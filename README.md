MAC Address Spoofer

Description

This Python script is a MAC Address Spoofer designed to alter the Media Access Control (MAC) address of a network interface on a device. The MAC address is a unique identifier assigned to network interfaces for communications within a network segment. By spoofing the MAC address, users can change their device's identity on a network, which can be useful for testing, privacy, or security-related purposes in ethical hacking scenarios.

Note: This tool is intended for educational purposes and should only be used in environments where you have explicit permission to perform such actions. Unauthorized MAC address spoofing may violate network policies or laws.

Features





Generate Random MAC Address: Creates a random MAC address with the prefix 08:00:00:xx:xx:xx.



Select from Known MAC Addresses: Choose a MAC address from a predefined list of vendor-specific MAC addresses (e.g., Apple, Cisco, VMware).



Scan Network for MAC Addresses: Scans the local network using the arp command to discover MAC addresses of connected devices and allows spoofing one of them.



Display Current MAC Addresses: Lists the MAC addresses of all network interfaces on the system.



Reset to Default MAC Addresses: Restores network interfaces to their original MAC addresses stored in a default_macs.txt file.



Developer Information: Displays details about the developer, including name, roll number, degree, and course subject.

Prerequisites





Operating System: Linux or macOS (requires ifconfig and arp commands; Windows is not supported).



Python Version: Python 3.x.



Permissions: Root/administrator privileges are required to modify network interface settings.



Dependencies: No external Python libraries are required; uses standard libraries (subprocess, random, os, datetime).

Installation





Clone the repository:

git clone https://github.com/<your-username>/mac-address-spoofer.git



Navigate to the project directory:

cd mac-address-spoofer



Ensure you have the necessary permissions to run the script (e.g., use sudo on Linux).

Usage

Run the script with root privileges:

sudo python3 mac_spoofer.py

Menu Options





Generate a random MAC address: Creates a random MAC address and applies it to a specified network interface.



Select a MAC address from a list: Choose from a predefined list of vendor-specific MAC addresses.



Scan the network for devices: Scans the network using arp -a and allows spoofing a discovered MAC address.



Display all current MAC addresses: Shows the current MAC addresses of all network interfaces.



Reset to default MAC addresses: Restores the original MAC addresses from the default_macs.txt file.

Example

$ sudo python3 mac_spoofer.py
Developer Name: Siyam Haider
Roll Number: 21I-1571
Section: T
Degree: Cybersecurity
Campus: FAST NUCES ISB
Course Subject: Ethical Hacking
Current Date and Time: 2025-06-09 21:21:00.123456

A MAC address spoofer is a tool or software application used to alter the Media Access Control (MAC) address of a network interface on a computer or device. 
The MAC address is a unique identifier assigned to network interfaces for communications within a network segment. 
By spoofing the MAC address, users can change their device's identity on a network.

MAC Address Spoofer
1. Generate a random MAC address (02:00:00:xx:xx:xx)
2. Select a MAC address from a list of known MAC addresses
3. Scan the current network for other devices and select one of their MAC addresses
4. Display all current MAC addresses
5. Reset all adapters to their default MAC addresses
Choose an option (1/2/3/4/5): 

File Structure





mac_spoofer.py: The main Python script containing the MAC address spoofing logic.



default_macs.txt: A file automatically generated to store the original MAC addresses of network interfaces for restoration.

How It Works





Initialization: On first run, the script checks for the existence of default_macs.txt. If it doesn't exist, it creates the file by saving the current MAC addresses of all network interfaces.



MAC Address Generation: Generates random MAC addresses or allows selection from a predefined list of vendor-specific MACs.



Network Scanning: Uses the arp -a command to discover devices on the local network and their MAC addresses.



Spoofing: Uses ifconfig to change the MAC address of a specified network interface (requires
