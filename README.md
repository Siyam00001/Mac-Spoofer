# MAC Address Spoofer

## Description
This Python script is a MAC Address Spoofer designed to alter the Media Access Control (MAC) address of a network interface on a device. The MAC address is a unique identifier assigned to network interfaces for communications within a network segment. By spoofing the MAC address, users can change their device's identity on a network, which can be useful for testing, privacy, or security-related purposes in ethical hacking scenarios.

> **Note:** This tool is intended for educational purposes and should only be used in environments where you have explicit permission to perform such actions. Unauthorized MAC address spoofing may violate network policies or laws.

## Features
- **Generate Random MAC Address:** Creates a random MAC address with the prefix `08:00:00:xx:xx:xx`.
- **Select from Known MAC Addresses:** Choose a MAC address from a predefined list of vendor-specific MAC addresses (e.g., Apple, Cisco, VMware).
- **Scan Network for MAC Addresses:** Scans the local network using the `arp` command to discover MAC addresses of connected devices and allows spoofing one of them.
- **Display Current MAC Addresses:** Lists the MAC addresses of all network interfaces on the system.
- **Reset to Default MAC Addresses:** Restores network interfaces to their original MAC addresses stored in a `default_macs.txt` file.
- **Developer Information:** Displays details about the developer, including name, roll number, degree, and course subject.

## Prerequisites
- **Operating System:** Linux or macOS (requires `ifconfig` and `arp` commands; Windows is not supported).
- **Python Version:** Python 3.x.
- **Permissions:** Root/administrator privileges are required to modify network interface settings.
- **Dependencies:** No external Python libraries are required; uses standard libraries (`subprocess`, `random`, `os`, `datetime`).

## Installation
```sh
# Clone the repository
git clone https://github.com/<your-username>/mac-address-spoofer.git

# Navigate to the project directory
cd mac-address-spoofer
