import subprocess
import random
import os
import datetime

DEFAULT_MAC_FILE = "default_macs.txt"

list_of_macs = [
    ("00:00:0C:C2:1B:04", "VMware, Inc. (Virtual Machine)"),
    ("00:14:22:5D:62:10", "Apple, Inc. (iPhone)"),
    ("00:1E:52:6E:7F:A1", "Samsung Electronics Co.,Ltd (Samsung Smart TV)"),
    ("00:1A:11:3F:E1:00", "Sony Corporation (PlayStation)"),
    ("00:16:D3:40:F9:B2", "Cisco Systems, Inc. (Router)"),
    ("00:24:D7:30:5C:20", "Microsoft Corporation (Xbox)"),
    ("00:17:F2:EB:80:00", "Nintendo Co., Ltd. (Wii)"),
    ("00:50:56:C0:00:08", "VMware, Inc. (Virtual Machine)"),
    ("00:0A:95:9D:68:16", "Toshiba Corporation (Laptop)"),
    ("00:23:AB:1B:2E:30", "Dell Inc. (Desktop Computer)"),
    ("00:26:B0:4F:CF:01", "Huawei Technologies Co., Ltd. (Smartphone)"),
    ("00:0D:67:88:12:45", "LG Electronics (Smart TV)"),
    ("00:1C:25:4F:5A:6F", "Intel Corporate (Network Interface Card)"),
    ("00:0C:29:2D:B7:E8", "Cisco Systems, Inc. (Access Point)"),
    ("00:19:7D:0E:46:1A", "Hewlett-Packard Company (Printer)"),
    ("00:15:5D:1B:B9:76", "ASUS TeK Computer Inc. (Wireless Router)"),
    ("00:0F:1F:33:71:1D", "Netgear Inc. (Switch)"),
    ("00:17:A4:20:30:00", "Xiaomi Communications Co., Ltd. (Smart Home Device)"),
    ("00:0D:E9:E3:4B:90", "Fujitsu Limited (Tablet)"),
    ("00:08:74:22:1C:6B", "Hewlett-Packard Company (Scanner)"),
    ("00:13:46:58:AB:CD", "Motorola Mobility LLC (Smartwatch)"),
    ("00:1B:21:34:56:78", "Cisco Systems, Inc. (Firewall)"),
    ("00:1E:65:99:33:99", "TP-Link Technologies Co., Ltd. (Access Point)"),
    ("00:0E:8E:12:34:56", "Google, Inc. (Chromecast)"),
    ("00:0C:42:2E:FA:8A", "Apple, Inc. (iPad)"),
    ("00:1A:2B:3C:4D:5E", "Microsoft Corporation (Surface Tablet)"),
    ("00:21:33:44:55:66", "Amazon Technologies Inc. (Echo Device)"),
    ("00:0F:65:42:AC:1E", "Lenovo Group Limited (Laptop)"),
    ("00:0B:CD:DE:EF:AB", "Sonos, Inc. (Speaker)"),
    ("00:0D:EE:F1:A2:B3", "Roku, Inc. (Streaming Device)")
]


def generate_random_mac():
    return "08:00:00:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def select_mac_from_list(mac_list):
    print("Available MAC Addresses:")
    for n,i in enumerate(mac_list):
        print(f"{n+1}.{i[1]} MAC: {i[0]}")
    choice = int(input("Select a MAC Address (1 - {}): ".format(len(mac_list))))
    if 1 <= choice <= len(mac_list):
        return mac_list[choice - 1][0]
    else:
        print("Invalid choice.")
        return None

def scan_network():
    arp_output = subprocess.run(["arp", "-a"], capture_output=True, text=True)
    output_lines = arp_output.stdout.splitlines()
    print(output_lines)
    mac_interfaces = []
    for line in output_lines:
        mac_address = line.split("at")[1].split("[")[0].strip()
        interface_name = line.split("on")[1].split(r"'")[0].strip()
        mac_interfaces.append((mac_address,interface_name))
    return mac_interfaces

developer_info = {
    "name": "Siyam Haider",
    "roll_number": "21I-1571",
    "section": "T",
    "degree": "Cybersecurity",
    "campus": "FAST NUCES ISB",
    "course_subject": "Ethical Hacking"
}

description = """
A MAC address spoofer is a tool or software application used to alter the Media Access Control (MAC) address of a network interface on a computer or device. 
The MAC address is a unique identifier assigned to network interfaces for communications within a network segment. 
By spoofing the MAC address, users can change their device's identity on a network.
"""

def display_current_macs():
    current_macs = []
    ifconfig_result = subprocess.run(["ifconfig"], capture_output=True, text=True)
    output = ifconfig_result.stdout

    print("Current MAC Addresses:")
    interfaces = output.split('\n\n')
    for interface in interfaces:
        if "flags" in interface:
            lines = interface.split('\n')
            adapter_name = lines[0].split(':')[0]
            mac_address = ""
            for line in lines:
                if "ether" in line:
                    mac_address = line.split()[1]
                    break
            print(f"{adapter_name} : {mac_address}")
            current_macs.append((mac_address,adapter_name))
    return current_macs

def reset_to_default_macs():
    if not os.path.exists(DEFAULT_MAC_FILE):
        print("Default MAC addresses file not found.")
        return
    
    with open(DEFAULT_MAC_FILE, "r") as f:
        default_macs = [line.strip().split(',') for line in f.readlines()]

    for mac_address, interface_name in default_macs:
        spoof_mac(mac_address,interface_name)

def spoof_mac(mac_address,interface):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])
    print("DONE")

def write_current_macs_to_file():
    current_macs = display_current_macs()
    with open(DEFAULT_MAC_FILE, "w+") as f:
        for adapter_name, mac_address in current_macs:
            if(adapter_name!=""):
                f.write(f"{adapter_name},{mac_address}\n")


def main():
    print("Developer Name:", developer_info["name"])
    print("Roll Number:", developer_info["roll_number"])
    print("Section:", developer_info["section"])
    print("Degree:", developer_info["degree"])
    print("Campus:", developer_info["campus"])
    print("Course Subject:", developer_info["course_subject"])
    
    # Display current date and time
    print("Current Date and Time:", datetime.datetime.now())
    print(description)
    print("MAC Address Spoofer")
    print("1. Generate a random MAC address (02:00:00:xx:xx:xx)")
    print("2. Select a MAC address from a list of known MAC addresses")
    print("3. Scan the current network for other devices and select one of their MAC addresses")
    print("4. Display all current MAC addresses")
    print("5. Reset all adapters to their default MAC addresses")
    choice = input("Choose an option (1/2/3/4/5): ")

    if choice == '1':
        interface_name = input("Enter name of interface: ")
        random_mac = generate_random_mac()
        print("Generated random mac: ",random_mac)
        spoof_mac(random_mac,interface_name)
    elif choice == '2':
        interface_name = input("Enter name of interface: ")
        selected_mac = select_mac_from_list(list_of_macs)
        if selected_mac:
            spoof_mac(selected_mac,interface_name)
    elif choice == '3':
        network_macs = scan_network()
        selected_mac = select_mac_from_list(network_macs)
        if selected_mac:
            interface_name = input("Enter name of interface to spoof: ")
            spoof_mac(selected_mac, interface_name)
    elif choice == '4':
        display_current_macs()
    elif choice == '5':
        reset_to_default_macs()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    if not os.path.exists(DEFAULT_MAC_FILE):
        print("Creating default MAC addresses file...")
        # Write default MAC addresses to file
        write_current_macs_to_file()
    main()
