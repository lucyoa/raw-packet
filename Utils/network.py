from random import choice, randint
from struct import pack
from binascii import unhexlify
from array import array
from socket import error, inet_aton, inet_pton, htons, IPPROTO_TCP, IPPROTO_UDP, AF_INET6, IPPROTO_ICMPV6
from re import search


class Ethernet_raw:
    # +---------------------------------------------------------------+
    # |       Ethernet destination address (first 32 bits)            |
    # +-------------------------------+-------------------------------+
    # | Ethernet dest (last 16 bits)  |Ethernet source (first 16 bits)|
    # +-------------------------------+-------------------------------+
    # |       Ethernet source address (last 32 bits)                  |
    # +-------------------------------+-------------------------------+
    # |        Type code              |                               |
    # +-------------------------------+-------------------------------+

    macs = []

    def __init__(self):
        self.macs.append("3c:d9:2b")  # Hewlett Packard
        self.macs.append("9c:8e:99")  # Hewlett Packard
        self.macs.append("b4:99:ba")  # Hewlett Packard
        self.macs.append("00:50:ba")  # Hewlett Packard
        self.macs.append("00:11:0a")  # Hewlett Packard
        self.macs.append("00:11:85")  # Hewlett Packard
        self.macs.append("00:12:79")  # Hewlett Packard
        self.macs.append("00:13:21")  # Hewlett Packard
        self.macs.append("00:14:38")  # Hewlett Packard
        self.macs.append("00:14:c2")  # Hewlett Packard
        self.macs.append("00:15:60")  # Hewlett Packard
        self.macs.append("00:16:35")  # Hewlett Packard
        self.macs.append("00:17:08")  # Hewlett Packard
        self.macs.append("00:18:fe")  # Hewlett Packard
        self.macs.append("00:19:bb")  # Hewlett Packard
        self.macs.append("00:1a:4b")  # Hewlett Packard
        self.macs.append("00:1b:78")  # Hewlett Packard
        self.macs.append("00:1c:c4")  # Hewlett Packard
        self.macs.append("00:1e:0b")  # Hewlett Packard
        self.macs.append("00:1f:29")  # Hewlett Packard
        self.macs.append("00:21:5a")  # Hewlett Packard
        self.macs.append("00:22:64")  # Hewlett Packard
        self.macs.append("00:23:7d")  # Hewlett Packard
        self.macs.append("00:24:81")  # Hewlett Packard
        self.macs.append("00:25:b3")  # Hewlett Packard
        self.macs.append("00:26:55")  # Hewlett Packard
        self.macs.append("00:0d:88")  # D-Link Corporation
        self.macs.append("00:0f:3d")  # D-Link Corporation
        self.macs.append("00:13:46")  # D-Link Corporation
        self.macs.append("00:15:e9")  # D-Link Corporation
        self.macs.append("00:17:9a")  # D-Link Corporation
        self.macs.append("00:19:5b")  # D-Link Corporation
        self.macs.append("00:1b:11")  # D-Link Corporation
        self.macs.append("00:1c:f0")  # D-Link Corporation
        self.macs.append("00:1e:58")  # D-Link Corporation
        self.macs.append("00:21:91")  # D-Link Corporation
        self.macs.append("00:22:b0")  # D-Link Corporation
        self.macs.append("00:24:01")  # D-Link Corporation
        self.macs.append("00:26:5a")  # D-Link Corporation
        self.macs.append("00:0d:88")  # D-Link Corporation
        self.macs.append("00:0f:3d")  # D-Link Corporation
        self.macs.append("00:00:0c")  # Cisco Systems, Inc
        self.macs.append("00:01:42")  # Cisco Systems, Inc
        self.macs.append("00:01:43")  # Cisco Systems, Inc
        self.macs.append("00:01:63")  # Cisco Systems, Inc
        self.macs.append("00:01:64")  # Cisco Systems, Inc
        self.macs.append("00:01:96")  # Cisco Systems, Inc
        self.macs.append("00:01:97")  # Cisco Systems, Inc
        self.macs.append("00:01:c7")  # Cisco Systems, Inc
        self.macs.append("00:01:c9")  # Cisco Systems, Inc
        self.macs.append("00:02:16")  # Cisco Systems, Inc
        self.macs.append("00:02:17")  # Cisco Systems, Inc
        self.macs.append("00:02:4a")  # Cisco Systems, Inc
        self.macs.append("00:02:4b")  # Cisco Systems, Inc
        self.macs.append("00:02:7d")  # Cisco Systems, Inc
        self.macs.append("00:02:7e")  # Cisco Systems, Inc
        self.macs.append("d0:d0:fd")  # Cisco Systems, Inc
        self.macs.append("d4:8c:b5")  # Cisco Systems, Inc
        self.macs.append("d4:a0:2a")  # Cisco Systems, Inc
        self.macs.append("d4:d7:48")  # Cisco Systems, Inc
        self.macs.append("d8:24:bd")  # Cisco Systems, Inc
        self.macs.append("08:63:61")  # Huawei Technologies Co., Ltd
        self.macs.append("08:7a:4c")  # Huawei Technologies Co., Ltd
        self.macs.append("0c:37:dc")  # Huawei Technologies Co., Ltd
        self.macs.append("0c:96:bf")  # Huawei Technologies Co., Ltd
        self.macs.append("10:1b:54")  # Huawei Technologies Co., Ltd
        self.macs.append("10:47:80")  # Huawei Technologies Co., Ltd
        self.macs.append("10:c6:1f")  # Huawei Technologies Co., Ltd
        self.macs.append("20:f3:a3")  # Huawei Technologies Co., Ltd
        self.macs.append("24:69:a5")  # Huawei Technologies Co., Ltd
        self.macs.append("28:31:52")  # Huawei Technologies Co., Ltd
        self.macs.append("00:1b:63")  # Apple Inc
        self.macs.append("00:1c:b3")  # Apple Inc
        self.macs.append("00:1d:4f")  # Apple Inc
        self.macs.append("00:1e:52")  # Apple Inc
        self.macs.append("00:1e:c2")  # Apple Inc
        self.macs.append("00:1f:5b")  # Apple Inc
        self.macs.append("00:1f:f3")  # Apple Inc
        self.macs.append("00:21:e9")  # Apple Inc
        self.macs.append("00:22:41")  # Apple Inc
        self.macs.append("00:23:12")  # Apple Inc
        self.macs.append("00:23:32")  # Apple Inc
        self.macs.append("00:23:6c")  # Apple Inc
        self.macs.append("00:23:df")  # Apple Inc
        self.macs.append("00:24:36")  # Apple Inc
        self.macs.append("00:25:00")  # Apple Inc
        self.macs.append("00:25:4b")  # Apple Inc
        self.macs.append("00:25:bc")  # Apple Inc
        self.macs.append("00:26:08")  # Apple Inc
        self.macs.append("00:26:4a")  # Apple Inc
        self.macs.append("00:26:b0")  # Apple Inc
        self.macs.append("00:26:bb")  # Apple Inc
        self.macs.append("00:11:75")  # Intel Corporate
        self.macs.append("00:13:e8")  # Intel Corporate
        self.macs.append("00:13:02")  # Intel Corporate
        self.macs.append("00:02:b3")  # Intel Corporate
        self.macs.append("00:03:47")  # Intel Corporate
        self.macs.append("00:04:23")  # Intel Corporate
        self.macs.append("00:0c:f1")  # Intel Corporate
        self.macs.append("00:0e:0c")  # Intel Corporate
        self.macs.append("00:0e:35")  # Intel Corporate
        self.macs.append("00:12:f0")  # Intel Corporate
        self.macs.append("00:13:02")  # Intel Corporate
        self.macs.append("00:13:20")  # Intel Corporate
        self.macs.append("00:13:ce")  # Intel Corporate
        self.macs.append("00:13:e8")  # Intel Corporate
        self.macs.append("00:15:00")  # Intel Corporate
        self.macs.append("00:15:17")  # Intel Corporate
        self.macs.append("00:16:6f")  # Intel Corporate
        self.macs.append("00:16:76")  # Intel Corporate
        self.macs.append("00:16:ea")  # Intel Corporate
        self.macs.append("00:16:eb")  # Intel Corporate
        self.macs.append("00:18:de")  # Intel Corporate

    def __enter__(self):
        return self

    def get_random_mac(self):
        mac_prefix = choice(self.macs)
        mac_suffix = ':'.join('{0:02x}'.format(randint(0x00, 0xff), 'x') for _ in range(3))
        return mac_prefix + ':' + mac_suffix

    @staticmethod
    def get_mac_for_dhcp_discover():
        return "00:00:0c:d4:e8:17"

    @staticmethod
    def convert_mac(mac_address):
        if len(mac_address) < 17:
            print "Too short mac address: " + mac_address
            exit(1)
        mac_address = mac_address[:17].lower()
        if search("([0-9a-f]{2}[:-]){5}([0-9a-f]{2})", mac_address):
            return unhexlify(mac_address.replace(':', ''))
        else:
            print "Bad mac address: " + mac_address
            exit(1)

    def make_header(self, source_mac, destination_mac, network_type):
        return self.convert_mac(destination_mac) + self.convert_mac(source_mac) + pack("!" "H", network_type)

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.macs[:]


class IP_raw:
    # 0                   1                   2                   3
    # 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    # +-------+-------+---------------+-------------------------------+
    # |Version|  IHL  |Type of Service|          Total Length         |
    # +-------+-------+---------------+-----+-------------------------+
    # |         Identification        |Flags|      Fragment Offset    |
    # +---------------+---------------+-----+-------------------------+
    # |  Time to Live |    Protocol   |         Header Checksum       |
    # +---------------+---------------+-------------------------------+
    # |                       Source Address                          |
    # +---------------------------------------------------------------+
    # |                    Destination Address                        |
    # +-----------------------------------------------+---------------+
    # |                    Options                    |    Padding    |
    # +-----------------------------------------------+---------------+

    def __init__(self):
        pass

    @staticmethod
    def get_random_ip():
        return '.'.join(str(randint(0, 255)) for _ in range(4))

    @staticmethod
    def checksum(packet):
        if len(packet) % 2 == 1:
            packet += "\0"
        s = sum(array("H", packet))
        s = (s >> 16) + (s & 0xffff)
        s += s >> 16
        s = ~s
        return (((s >> 8) & 0xff) | s << 8) & 0xffff

    def make_header(self, source_ip, destination_ip, data_len, transport_protocol_len, transport_protocol, ttl=64):
        srcip = inet_aton(source_ip)       # Source port
        dstip = inet_aton(destination_ip)  # Destination port
        ver = 4       # IP protocol version
        ihl = 5       # Internet Header Length
        dscp_ecn = 0  # Differentiated Services Code Point and Explicit Congestion Notification

        tlen = data_len + transport_protocol_len + 20  # Packet length
        ident = htons(randint(1, 65535))  # Identification
        flg_frgoff = 0  # Flags and fragmentation offset
        ptcl = transport_protocol  # Protocol
        chksm = 0  # Checksum

        ip_header = pack("!" "2B" "3H" "2B" "H" "4s" "4s",
                         (ver << 4) + ihl, dscp_ecn, tlen, ident,
                         flg_frgoff, ttl, ptcl, chksm, srcip, dstip)
        chksm = self.checksum(ip_header)
        return pack("!" "2B" "3H" "2B" "H" "4s" "4s",
                    (ver << 4) + ihl, dscp_ecn, tlen, ident,
                    flg_frgoff, ttl, ptcl, chksm, srcip, dstip)


class IPv6_raw:
    #           0 - 3     4 - 11                     12 - 31
    #         +-------+--------------+----------------------------------------+
    #    0-31 |Version|Traffic Class |              Flow Label                |
    #         +-------+--------------+-------------------+--------------------+
    #   32-63 |Payload Length (32-47)|Next Header (48-55)|  Hop Limit (56-63) |
    #         +----------------------+-------------------+--------------------+
    #  64-191 |                       Source Address                          |
    #         +---------------------------------------------------------------+
    # 192-288 |                    Destination Address                        |
    #         +---------------------------------------------------------------+

    def __init__(self):
        pass

    @staticmethod
    def get_random_ip(octets=1, prefix=""):
        ip = prefix
        for index in range(0, octets):
            ip += str(hex(randint(1, 65535))[2:]) + ":"
        return ip[:-1]

    @staticmethod
    def pack_addr(ipv6_addr):
        if ipv6_addr == "::":
            return ''.join(pack("B", 0) for _ in range(16))
        else:
            return inet_pton(AF_INET6, ipv6_addr)

    def make_header(self, source_ip, destination_ip, flow_label, payload_len, next_header, hop_limit=64):
        srcipv6 = self.pack_addr(source_ip)       # Source IPv6 address
        dstipv6 = self.pack_addr(destination_ip)  # Destination IPv6 address

        ver = 6             # IP protocol version
        traffic_class = 0   # Differentiated Services Code Point and Explicit Congestion Notification

        return pack("!" "2I",
                    (ver << 28) + (traffic_class << 20) + flow_label,
                    (payload_len << 16) + (next_header << 8) + hop_limit) + srcipv6 + dstipv6


class ARP_raw:

    eth = None

    def __init__(self):
        self.eth = Ethernet_raw()

    def make_packet(self, ethernet_src_mac, ethernet_dst_mac, sender_mac, sender_ip, target_mac, target_ip, opcode,
                    hardware_type=1, protocol_type=2048, hardware_size=6, protocol_size=4):
        sender_ip = inet_aton(sender_ip)
        target_ip = inet_aton(target_ip)
        sender_mac = self.eth.convert_mac(sender_mac)
        target_mac = self.eth.convert_mac(target_mac)
        arp_packet = pack("!" "2H" "2B" "H", hardware_type, protocol_type, hardware_size, protocol_size, opcode)
        arp_packet += sender_mac + pack("!" "4s", sender_ip)
        arp_packet += target_mac + pack("!" "4s", target_ip)

        eth_header = self.eth.make_header(ethernet_src_mac, ethernet_dst_mac, 2054)
        return eth_header + arp_packet

    def make_response(self, ethernet_src_mac, ethernet_dst_mac, sender_mac, sender_ip, target_mac, target_ip):
        return self.make_packet(ethernet_src_mac=ethernet_src_mac,
                                ethernet_dst_mac=ethernet_dst_mac,
                                sender_mac=sender_mac,
                                sender_ip=sender_ip,
                                target_mac=target_mac,
                                target_ip=target_ip,
                                opcode=2)

    def make_request(self, ethernet_src_mac, ethernet_dst_mac, sender_mac, sender_ip, target_mac, target_ip):
        return self.make_packet(ethernet_src_mac=ethernet_src_mac,
                                ethernet_dst_mac=ethernet_dst_mac,
                                sender_mac=sender_mac,
                                sender_ip=sender_ip,
                                target_mac=target_mac,
                                target_ip=target_ip,
                                opcode=1)


class UDP_raw:
    #  0                16               31
    #  +-----------------+-----------------+
    #  |     Source      |   Destination   |
    #  |      Port       |      Port       |
    #  +-----------------+-----------------+
    #  |                 |                 |
    #  |     Length      |    Checksum     |
    #  +-----------------+-----------------+
    #  |
    #  |          data octets ...
    #  +---------------- ...

    ipv6 = None

    def __init__(self):
        self.ipv6 = IPv6_raw()

    @staticmethod
    def checksum(pkt):
        if len(pkt) % 2 == 1:
            pkt += "\0"
        s = sum(array("H", pkt))
        s = (s >> 16) + (s & 0xffff)
        s += s >> 16
        s = ~s
        return (((s >> 8) & 0xff) | s << 8) & 0xffff

    @staticmethod
    def make_header(source_port, destination_port, data_length):
        if 0 < source_port < 65536 and 0 < destination_port < 65536:
            return pack("!4H", source_port, destination_port, data_length + 8, 0)
        else:
            return None

    def make_header_with_ipv6_checksum(self, ipv6_src, ipv6_dst, port_src, port_dst, data_len, data):
        udp_header = self.make_header(port_src, port_dst, data_len)
        placeholder = 0
        protocol = IPPROTO_UDP
        udp_length = data_len + 8

        psh = self.ipv6.pack_addr(ipv6_src) + self.ipv6.pack_addr(ipv6_dst)
        psh += pack("!" "2B" "H", placeholder, protocol, udp_length)
        chksum = self.checksum(psh + udp_header + data)

        return pack("!4H", port_src, port_dst, data_len + 8, chksum)


class TCP_raw:
    timestamp_value = 0

    def __init__(self):
        with open('/proc/uptime', 'r') as uptime:
            self.timestamp_value = int(float(uptime.readline().split()[0]))

    def update_timestamp(self):
        with open('/proc/uptime', 'r') as uptime:
            self.timestamp_value = int(float(uptime.readline().split()[0]))

    @staticmethod
    def checksum(msg):
        s = 0
        if len(msg) % 2 == 1:
            msg += "\0"
        for i in range(0, len(msg), 2):
            w = (ord(msg[i]) << 8) + (ord(msg[i + 1]))
            s = s + w
        s = (s >> 16) + (s & 0xffff)
        s = ~s & 0xffff
        return s

    def make_header(self, ip_src, ip_dst, port_src, port_dst, seq, ack, flag, win, opt_exist=False, opt=None, data=""):

        reserved = 0
        window = win
        chksum = 0
        urg = 0

        if opt_exist:
            opt_len = len(opt) / 4
            offset = 5 + opt_len
        else:
            offset = 5

        tcp_header = pack("!" "2H" "2L" "2B" "3H",
                          port_src, port_dst, seq, ack, (offset << 4) + reserved, flag, window, chksum, urg)

        if opt_exist:
            tcp_header += opt

        source_address = inet_aton(ip_src)
        destination_address = inet_aton(ip_dst)
        placeholder = 0
        protocol = IPPROTO_TCP
        tcp_length = len(tcp_header) + len(data)
        psh = pack("!" "4s" "4s" "2B" "H", source_address, destination_address, placeholder, protocol, tcp_length)

        chksum = self.checksum(psh + tcp_header + data)

        tcp_header = pack("!" "2H" "2L" "2B" "3H",
                          port_src, port_dst, seq, ack, (offset << 4) + reserved, flag, window, chksum, urg)

        if opt_exist:
            return tcp_header + opt
        else:
            return tcp_header

    def make_syn_header(self, ip_src, ip_dst, port_src, port_dst, seq):
        option_mss = pack("!2B H", 2, 4, 1460)
        option_sack = pack("!2B", 4, 2)
        self.update_timestamp()
        option_timestamp = pack("! 2B 2L", 8, 10, self.timestamp_value, 0)
        option_nop = pack("!B", 1)
        option_scale = pack("!3B", 3, 3, 7)
        options = option_mss + option_sack + option_timestamp + option_nop + option_scale

        return self.make_header(ip_src, ip_dst, port_src, port_dst, seq, 0, 2, 29200, True, options)

    def make_ack_header(self, ip_src, ip_dst, port_src, port_dst, seq, ack, tsecr=-1):
        option_nop = pack("!B", 1)
        if tsecr != -1:
            self.update_timestamp()
            option_timestamp = pack("! 2B 2L", 8, 10, self.timestamp_value, tsecr)
            options = option_nop + option_nop + option_timestamp
        else:
            options = option_nop + option_nop

        return self.make_header(ip_src, ip_dst, port_src, port_dst, seq, ack, 16, 29200, True, options)

    def make_psh_header(self, ip_src, ip_dst, port_src, port_dst, seq, ack, tsecr=-1, data=""):
        option_nop = pack("!B", 1)
        if tsecr != -1:
            self.update_timestamp()
            option_timestamp = pack("! 2B 2L", 8, 10, self.timestamp_value, tsecr)
            options = option_nop + option_nop + option_timestamp
        else:
            options = option_nop + option_nop

        return self.make_header(ip_src, ip_dst, port_src, port_dst, seq, ack, 24, 29200, False, options, data)

    def make_fin_header(self, ip_src, ip_dst, port_src, port_dst, seq, ack, tsecr=-1):
        option_nop = pack("!B", 1)
        if tsecr != -1:
            self.update_timestamp()
            option_timestamp = pack("! 2B 2L", 8, 10, self.timestamp_value, tsecr)
            options = option_nop + option_nop + option_timestamp
        else:
            options = option_nop + option_nop

        return self.make_header(ip_src, ip_dst, port_src, port_dst, seq, ack, 17, 29200, False, options)


class ICMPv6_raw:
    #  0                   1                   2                   3
    #  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    # +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    # |     Type      |     Code      |          Checksum             |
    # +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    # |                                                               |
    # +                         Message Body                          +
    # |                                                               |

    eth = None
    ipv6 = None
    dns = None

    def __init__(self):
        self.eth = Ethernet_raw()
        self.ipv6 = IPv6_raw()
        self.dns = DNS_raw()

    @staticmethod
    def checksum(pkt):
        if len(pkt) % 2 == 1:
            pkt += "\0"
        s = sum(array("H", pkt))
        s = (s >> 16) + (s & 0xffff)
        s += s >> 16
        s = ~s
        return (((s >> 8) & 0xff) | s << 8) & 0xffff

    @staticmethod
    def make_option(option_type, option_value):
        if (len(option_value) + 2) / 8 > 255:
            print "ICMPv6 option value too big!"
            return ""
        else:
            if (len(option_value) + 2) % 8 != 0:
                option_value = ''.join(pack("B", 0) for _ in range(8 - ((len(option_value) + 2) % 8))) + option_value
            return pack("!2B", option_type, (len(option_value) + 2) / 8) + option_value

    def make_packet(self, ethernet_src_mac, ethernet_dst_mac,
                    ipv6_src, ipv6_dst, ipv6_flow, type, code, body):

        placeholder = 0
        protocol = IPPROTO_ICMPV6
        check_sum = 0
        icmp_packet = pack("!" "2B" "H", type, code, check_sum) + body

        psh = self.ipv6.pack_addr(ipv6_src) + self.ipv6.pack_addr(ipv6_dst)
        psh += pack("!" "2B" "H", placeholder, protocol, len(icmp_packet))
        check_sum = self.checksum(psh + icmp_packet)

        icmp_packet = pack("!" "2B" "H", type, code, check_sum) + body

        eth_header = self.eth.make_header(ethernet_src_mac, ethernet_dst_mac, 34525)  # 34525 = 0x86dd (IPv6)
        ipv6_header = self.ipv6.make_header(ipv6_src, ipv6_dst, ipv6_flow, len(icmp_packet), 58, 255)  # 58 = 0x3a (ICMPv6)

        return eth_header + ipv6_header + icmp_packet

    def make_router_solicit_packet(self, ethernet_src_mac, ipv6_src,
                                   need_source_link_layer_address=False, source_link_layer_address=""):

        body = pack("I", 0)             # 4 reserved bytes
        if need_source_link_layer_address:
            body += pack("!" "2B", 1, 1)    # 1 - Type: source link address, 1 - Length = 1 (8 bytes)

            if source_link_layer_address == "":
                body += self.eth.convert_mac(ethernet_src_mac)
            else:
                body += self.eth.convert_mac(source_link_layer_address)

        return self.make_packet(ethernet_src_mac, "33:33:00:00:00:02", ipv6_src, "ff02::2", 0x835d1, 133, 0, body)

    def make_router_advertisement_packet(self, ethernet_src_mac, ethernet_dst_mac, ipv6_src, ipv6_dst,
                                         dns_address, domain_search, prefix=None, ipv6_addr=None, mtu=1500,
                                         advertisement_interval=60000, src_link_layer_address=None,
                                         router_lifetime=1800):
        cur_hop_limit = 64  # Cur hop limit
        flags = 0xc0        # Managed address configuration, other configuration, PRF: Medium
        reachable_time = 0  # Reachable time
        retrans_timer = 0   # Retrans timer

        body = pack("!" "2B" "H" "2I", cur_hop_limit, flags, router_lifetime, reachable_time, retrans_timer)

        if src_link_layer_address is None:
            src_link_layer_address = ethernet_src_mac

        if prefix is not None:
            prefix_value = self.ipv6.pack_addr(str(prefix.split("/")[0]))
            prefix_len = int(prefix.split("/")[1])
            body += self.make_option(3, pack("!" "2B" "3I", prefix_len, 0xc0, 0xffffffff, 0xffffffff, 0) + prefix_value)
            if ipv6_addr is not None:
                body += self.make_option(17, pack("!" "2B" "I", 3, prefix_len, 0) + self.ipv6.pack_addr(ipv6_addr))

        body += self.make_option(1, self.eth.convert_mac(src_link_layer_address))
        body += self.make_option(5, pack("!H", mtu))
        body += self.make_option(25, pack("!H", 6000) + self.ipv6.pack_addr(dns_address))

        if len(domain_search) > 22:
            print "Too big domain search value!"
        else:
            domain_search = self.dns.make_dns_name(domain_search)
            padding = 24 - len(domain_search)
            domain_search += ''.join(pack("B", 0) for _ in range(padding))
            body += self.make_option(31, pack("!I", 6000) + domain_search)

        body += self.make_option(7, pack("!H", advertisement_interval))

        return self.make_packet(ethernet_src_mac, ethernet_dst_mac, ipv6_src, ipv6_dst, 0xb4755, 134, 0, body)

    def make_neighbor_solicitation_packet(self, ethernet_src_mac, ipv6_src, target_ipv6_address=None,
                                          target_mac_address=None, ethernet_dst_mac=None, ipv6_dst=None):
        body = pack("!I", 0x00000000)  # Reserved

        if target_ipv6_address is not None:
            body += self.ipv6.pack_addr(target_ipv6_address)

        if target_mac_address is not None:
            body += self.make_option(2, self.eth.convert_mac(target_mac_address))  # Target link-layer address

        if ethernet_dst_mac is None:
            ethernet_dst_mac = "33:33:00:00:00:01"

        if ipv6_dst is None:
            ipv6_dst = "ff02::1"

        return self.make_packet(ethernet_src_mac, ethernet_dst_mac, ipv6_src, ipv6_dst, 0, 135, 0, body)

    def make_neighbor_advertisement_packet(self, ethernet_src_mac, ipv6_src, target_ipv6_address,
                                           ethernet_dst_mac=None, ipv6_dst=None):
        body = pack("!I", 0x20000000)   # Flags: 0x20000000, Override
        body += self.ipv6.pack_addr(target_ipv6_address)
        body += self.make_option(2, self.eth.convert_mac(ethernet_src_mac))  # Target link-layer address

        if ethernet_dst_mac is None:
            ethernet_dst_mac = "33:33:00:00:00:01"

        if ipv6_dst is None:
            ipv6_dst = "ff02::1"

        return self.make_packet(ethernet_src_mac, ethernet_dst_mac, ipv6_src, ipv6_dst, 0, 136, 0, body)

    # def make_dad_packet(self, ethernet_src_mac, target_ipv6_address):
    #     body = pack("I", 0)             # 4 reserved bytes
    #     body += self.ipv6.pack_addr(target_ipv6_address)
    #     body += self.make_option(14, pack("!IH", 0x1f06928c, 0x6f45))
    #
    #     return self.make_packet(ethernet_src_mac, "33:33:ff:00:03:2e",
    #                             "::", "ff02::1:ff00:32e", 0, 135, 0, body)


class DHCP_raw:
    # 0                   1                   2                   3
    # 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    # +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    # |     op (1)    |   htype (1)   |   hlen (1)    |   hops (1)    |
    # +---------------+---------------+---------------+---------------+
    # |                            xid (4)                            |
    # +-------------------------------+-------------------------------+
    # |           secs (2)            |           flags (2)           |
    # +-------------------------------+-------------------------------+
    # |                          ciaddr  (4)                          |
    # +---------------------------------------------------------------+
    # |                          yiaddr  (4)                          |
    # +---------------------------------------------------------------+
    # |                          siaddr  (4)                          |
    # +---------------------------------------------------------------+
    # |                          giaddr  (4)                          |
    # +---------------------------------------------------------------+
    # |                                                               |
    # |                          chaddr  (16)                         |
    # |                                                               |
    # |                                                               |
    # +---------------------------------------------------------------+
    # |                                                               |
    # |                          sname   (64)                         |
    # +---------------------------------------------------------------+
    # |                                                               |
    # |                          file    (128)                        |
    # +---------------------------------------------------------------+
    # |                                                               |
    # |                          options (variable)                   |
    # +---------------------------------------------------------------+

    # FIELD      OCTETS       DESCRIPTION
    # -----      ------       -----------
    #
    # op            1  Message op code / message type.
    #                  1 = BOOTREQUEST, 2 = BOOTREPLY
    # htype         1  Hardware address type, see ARP section in "Assigned
    #                  Numbers" RFC; e.g., '1' = 10mb ethernet.
    # hlen          1  Hardware address length (e.g.  '6' for 10mb
    #                  ethernet).
    # hops          1  Client sets to zero, optionally used by relay agents
    #                  when booting via a relay agent.
    # xid           4  Transaction ID, a random number chosen by the
    #                  client, used by the client and server to associate
    #                  messages and responses between a client and a
    #                  server.
    # secs          2  Filled in by client, seconds elapsed since client
    #                  began address acquisition or renewal process.
    # flags         2  Flags (see figure 2).
    # ciaddr        4  Client IP address; only filled in if client is in
    #                  BOUND, RENEW or REBINDING state and can respond
    #                  to ARP requests.
    # yiaddr        4  'your' (client) IP address.
    # siaddr        4  IP address of next server to use in bootstrap;
    #                  returned in DHCPOFFER, DHCPACK by server.
    # giaddr        4  Relay agent IP address, used in booting via a
    #                  relay agent.
    # chaddr       16  Client hardware address.
    # sname        64  Optional server host name, null terminated string.
    # file        128  Boot file name, null terminated string; "generic"
    #                  name or null in DHCPDISCOVER, fully qualified
    #                  directory-path name in DHCPOFFER.
    # options     var  Optional parameters field.  See the options
    #                  documents for a list of defined options.

    eth = None
    ip = None
    udp = None

    def __init__(self):
        self.eth = Ethernet_raw()
        self.ip = IP_raw()
        self.udp = UDP_raw()

    def make_packet(self, ethernet_src_mac, ethernet_dst_mac,
                    ip_src, ip_dst, udp_src_port, udp_dst_port,
                    bootp_message_type, bootp_transaction_id, bootp_flags,
                    bootp_client_ip, bootp_your_client_ip, bootp_next_server_ip,
                    bootp_relay_agent_ip, bootp_client_hw_address, dhcp_options, padding=0):

        try:
            message_type = bootp_message_type  # Boot protocol message type
            hardware_type = 1  # Ethernet
            hardware_address_len = 6  # Ethernet address len
            hops = 0  # Number of hops
            transaction_id = bootp_transaction_id  # Transaction id
            seconds_elapsed = 0  # Seconds elapsed
            flags = bootp_flags  # Flags

            CIADDR = inet_aton(bootp_client_ip)  # Client IP address
            YIADDR = inet_aton(bootp_your_client_ip)  # Your client IP address
            SIADDR = inet_aton(bootp_next_server_ip)  # Next server IP address
            GIADDR = inet_aton(bootp_relay_agent_ip)  # Relay agent IP address
            CHADDR = self.eth.convert_mac(bootp_client_hw_address)  # Client hardware address

            # Test case
            # test_command = bytes("() { :; }; echo test > /tmp/test ")
            # test_command = pack("!%ds" % (len(test_command)), test_command)

            client_hw_padding = ''.join(pack("B", 0) for _ in range(10))  # Client hardware address padding
            server_host_name = ''.join(pack("B", 0) for _ in range(64))  # Server host name
            boot_file_name = ''.join(pack("B", 0) for _ in range(128))  # Boot file name
            magic_cookie = pack("!4B", 99, 130, 83, 99)  # Magic cookie: DHCP

            dhcp_packet = pack("!" "4B" "L" "2H",
                               message_type, hardware_type, hardware_address_len, hops, transaction_id,
                               seconds_elapsed, flags)

            dhcp_packet += pack("!" "4s" "4s" "4s" "4s",
                                CIADDR, YIADDR, SIADDR, GIADDR) + CHADDR

            dhcp_packet += client_hw_padding + server_host_name + boot_file_name + magic_cookie

            if padding != 0:
                dhcp_packet += dhcp_options + ''.join(pack("B", 0) for _ in range(int(padding)))
            else:
                dhcp_packet += dhcp_options + ''.join(pack("B", 0) for _ in range(24))

            eth_header = self.eth.make_header(ethernet_src_mac, ethernet_dst_mac, 2048)
            ip_header = self.ip.make_header(ip_src, ip_dst, len(dhcp_packet), 8, 17)
            udp_header = self.udp.make_header(udp_src_port, udp_dst_port, len(dhcp_packet))

            return eth_header + ip_header + udp_header + dhcp_packet
        except error:
            return None

    def make_discover_packet(self, source_mac, client_mac, host_name=None):
        option_discover = pack("!3B", 53, 1, 1)
        options = option_discover

        if host_name is not None:
            host_name = bytes(host_name)
            if len(host_name) < 255:
                host_name = pack("!%ds" % (len(host_name)), host_name)
                option_host_name = pack("!2B", 12, len(host_name)) + host_name
                options += option_host_name

        option_param_req_list = pack("!2B", 55, 254)
        for param in range(1, 255):
            option_param_req_list += pack("B", param)

        option_end = pack("B", 255)

        options += option_param_req_list + option_end

        return self.make_packet(ethernet_src_mac=source_mac,
                                ethernet_dst_mac="ff:ff:ff:ff:ff:ff",
                                ip_src="0.0.0.0", ip_dst="255.255.255.255",
                                udp_src_port=68, udp_dst_port=67,
                                bootp_message_type=1,
                                bootp_transaction_id=randint(1, 4294967295),
                                bootp_flags=0,
                                bootp_client_ip="0.0.0.0",
                                bootp_your_client_ip="0.0.0.0",
                                bootp_next_server_ip="0.0.0.0",
                                bootp_relay_agent_ip="0.0.0.0",
                                bootp_client_hw_address=client_mac,
                                dhcp_options=options)

    def make_request_packet(self, source_mac, client_mac, transaction_id, dhcp_message_type=1, host_name=None,
                            requested_ip=None, option_value=None, option_code=12,
                            client_ip="0.0.0.0", your_client_ip="0.0.0.0", relay_agent_ip="0.0.0.0"):
        option_message_type = pack("!3B", 53, 1, dhcp_message_type)
        options = option_message_type

        if requested_ip is not None:
            option_requested_ip = pack("!" "2B" "4s", 50, 4, inet_aton(requested_ip))
            options += option_requested_ip

        if host_name is not None:
            host_name = bytes(host_name)
            if len(host_name) < 255:
                host_name = pack("!%ds" % (len(host_name)), host_name)
                option_host_name = pack("!2B", 12, len(host_name)) + host_name
                options += option_host_name

        if option_value is not None:
            if len(option_value) < 255:
                if 0 < option_code < 256:
                    option_payload = pack("!" "2B", option_code, len(option_value)) + option_value
                    options += option_payload

        option_param_req_list = pack("!2B", 55, 7)
        for param in [1, 2, 3, 6, 28, 15, 26]:
            option_param_req_list += pack("B", param)

        option_end = pack("B", 255)

        options += option_param_req_list + option_end

        return self.make_packet(ethernet_src_mac=source_mac,
                                ethernet_dst_mac="ff:ff:ff:ff:ff:ff",
                                ip_src="0.0.0.0", ip_dst="255.255.255.255",
                                udp_src_port=68, udp_dst_port=67,
                                bootp_message_type=1,
                                bootp_transaction_id=transaction_id,
                                bootp_flags=0,
                                bootp_client_ip=client_ip,
                                bootp_your_client_ip=your_client_ip,
                                bootp_next_server_ip="0.0.0.0",
                                bootp_relay_agent_ip=relay_agent_ip,
                                bootp_client_hw_address=client_mac,
                                dhcp_options=options)

    def make_release_packet(self, client_mac, server_mac, client_ip, server_ip):
        option_message_type = pack("!3B", 53, 1, 7)
        option_server_id = pack("!" "2B" "4s", 54, 4, inet_aton(server_ip))
        option_end = pack("B", 255)

        options = option_message_type + option_server_id + option_end

        return self.make_packet(ethernet_src_mac=client_mac,
                                ethernet_dst_mac=server_mac,
                                ip_src=client_ip, ip_dst=server_ip,
                                udp_src_port=68, udp_dst_port=67,
                                bootp_message_type=1,
                                bootp_transaction_id=randint(1, 4294967295),
                                bootp_flags=0,
                                bootp_client_ip="0.0.0.0",
                                bootp_your_client_ip="0.0.0.0",
                                bootp_next_server_ip="0.0.0.0",
                                bootp_relay_agent_ip="0.0.0.0",
                                bootp_client_hw_address=client_mac,
                                dhcp_options=options)

    def make_decline_packet(self, relay_mac, relay_ip, server_mac, server_ip, client_mac, requested_ip, transaction_id):
        option_message_type = pack("!3B", 53, 1, 4)
        option_requested_ip = pack("!" "2B" "4s", 50, 4, inet_aton(requested_ip))
        option_server_id = pack("!" "2B" "4s", 54, 4, inet_aton(server_ip))
        option_end = pack("B", 255)

        options = option_message_type + option_requested_ip + option_server_id + option_end

        return self.make_packet(ethernet_src_mac=relay_mac,
                                ethernet_dst_mac=server_mac,
                                ip_src=relay_ip, ip_dst=server_ip,
                                udp_src_port=68, udp_dst_port=67,
                                bootp_message_type=1,
                                bootp_transaction_id=transaction_id,
                                bootp_flags=0,
                                bootp_client_ip=requested_ip,
                                bootp_your_client_ip="0.0.0.0",
                                bootp_next_server_ip="0.0.0.0",
                                bootp_relay_agent_ip=relay_ip,
                                bootp_client_hw_address=client_mac,
                                dhcp_options=options)

    def make_response_packet(self, source_mac, destination_mac, source_ip, destination_ip, transaction_id, your_ip,
                             client_mac, dhcp_server_id, lease_time, netmask, router, dns, dhcp_operation=2,
                             payload=None, proxy=None, domain=None, tftp=None, payload_option_code=114):
        option_operation = pack("!3B", 53, 1, dhcp_operation)
        option_server_id = pack("!" "2B" "4s", 54, 4, inet_aton(dhcp_server_id))
        option_lease_time = pack("!" "2B" "L", 51, 4, lease_time)
        option_netmask = pack("!" "2B" "4s", 1, 4, inet_aton(netmask))
        option_router = pack("!" "2B" "4s", 3, 4, inet_aton(router))
        option_dns = pack("!" "2B" "4s", 6, 4, inet_aton(dns))
        option_end = pack("B", 255)

        options = option_operation + option_server_id + option_lease_time + option_netmask + \
                  option_router + option_dns

        if domain is not None:
            if len(domain) < 255:
                option_domain = pack("!" "2B", 15, len(domain)) + domain
                options += option_domain

        if proxy is not None:
            if len(proxy) < 255:
                option_proxy = pack("!" "2B", 252, len(proxy)) + proxy
                options += option_proxy

        if payload is not None:
            if len(payload) < 255:
                if 0 < payload_option_code < 256:
                    option_payload = pack("!" "2B", payload_option_code, len(payload)) + payload
                    options += option_payload

        if tftp is not None:
            if len(tftp) < 255:
                option_tftp = pack("!" "2B" "4s", 150, 4, inet_aton(tftp))
                options += option_tftp

        options += option_end

        return self.make_packet(ethernet_src_mac=source_mac,
                                ethernet_dst_mac=destination_mac,
                                ip_src=source_ip, ip_dst=destination_ip,
                                udp_src_port=67, udp_dst_port=68,
                                bootp_message_type=2,
                                bootp_transaction_id=transaction_id,
                                bootp_flags=0,
                                bootp_client_ip="0.0.0.0",
                                bootp_your_client_ip=your_ip,
                                bootp_next_server_ip="0.0.0.0",
                                bootp_relay_agent_ip="0.0.0.0",
                                bootp_client_hw_address=client_mac,
                                dhcp_options=options)

    def make_nak_packet(self, source_mac, destination_mac, source_ip, destination_ip, transaction_id, your_ip,
                        client_mac, dhcp_server_id):
        option_operation = pack("!3B", 53, 1, 6)
        option_server_id = pack("!" "2B" "4s", 54, 4, inet_aton(dhcp_server_id))
        option_end = pack("B", 255)
        options = option_operation + option_server_id + option_end

        return self.make_packet(ethernet_src_mac=source_mac,
                                ethernet_dst_mac=destination_mac,
                                ip_src=source_ip, ip_dst=destination_ip,
                                udp_src_port=67, udp_dst_port=68,
                                bootp_message_type=2,
                                bootp_transaction_id=transaction_id,
                                bootp_flags=0,
                                bootp_client_ip="0.0.0.0",
                                bootp_your_client_ip=your_ip,
                                bootp_next_server_ip="0.0.0.0",
                                bootp_relay_agent_ip="0.0.0.0",
                                bootp_client_hw_address=client_mac,
                                dhcp_options=options)


class DNS_raw:
    eth = Ethernet_raw()
    ip = IP_raw()
    udp = UDP_raw()

    def __init__(self):
        pass

    @staticmethod
    def make_dns_name(name):
        name_list = name.split(".")
        result_name = ""
        for part_of_name in name_list:
            if len(part_of_name) > 256:
                return ""
            else:
                result_name += pack("!" "B" "%ds" % (len(part_of_name)), len(part_of_name), part_of_name)
        result_name += "\x00"
        return result_name

    @staticmethod
    def make_dns_ptr(ip_address):
        pass

    def make_response_packet(self, src_mac, dst_mac, src_ip, dst_ip, src_port, dst_port, tid, flags,
                             queries=[], answers_address=[], name_servers={}):
        transaction_id = tid
        dns_flags = flags
        questions = len(queries)
        answer_rrs = len(answers_address)
        authority_rrs = len(name_servers.keys())
        additional_rrs = len(name_servers.keys())

        dns_packet = pack("!6H", transaction_id, dns_flags, questions, answer_rrs, authority_rrs, additional_rrs)

        query_type = 1

        for query in queries:
            query_name = query["name"]
            query_type = query["type"]
            query_class = query["class"]

            if query_name.endswith("."):
                query_name = query_name[:-1]

            dns_packet += self.make_dns_name(query_name)
            dns_packet += pack("!2H", query_type, query_class)

        if query_type == 1:
            for address in answers_address:
                if "name" in address.keys():
                    dns_packet += self.make_dns_name(address["name"])
                else:
                    dns_packet += pack("!H", 0xc00c)

                dns_packet += pack("!" "2H" "I" "H" "4s", address["type"], address["class"], address["ttl"],
                                   4, inet_aton(address["address"]))

        if query_type == 12:
            for address in answers_address:
                domain = self.make_dns_name(address["address"])
                if "name" in address.keys():
                    dns_packet += self.make_dns_name(address["name"])
                else:
                    dns_packet += pack("!H", 0xc00c)

                dns_packet += pack("!" "2H" "I" "H", address["type"], address["class"], address["ttl"],
                                   len(domain))
                dns_packet += domain

        eth_header = self.eth.make_header(src_mac, dst_mac, 2048)
        ip_header = self.ip.make_header(src_ip, dst_ip, len(dns_packet), 8, 17)
        udp_header = self.udp.make_header(src_port, dst_port, len(dns_packet))

        return eth_header + ip_header + udp_header + dns_packet

    def make_request_packet(self, src_mac, dst_mac, src_ip, dst_ip, src_port, dst_port, tid, queries=[], flags=0):
        transaction_id = tid
        dns_flags = flags
        questions = len(queries)
        answer_rrs = 0
        authority_rrs = 0
        additional_rrs = 0

        dns_packet = pack("!6H", transaction_id, dns_flags, questions, answer_rrs, authority_rrs, additional_rrs)
        for query in queries:
            dns_packet += self.make_dns_name(query["name"])
            dns_packet += pack("!2H", query["type"], query["class"])

        eth_header = self.eth.make_header(src_mac, dst_mac, 2048)
        ip_header = self.ip.make_header(src_ip, dst_ip, len(dns_packet), 8, 17)
        udp_header = self.udp.make_header(src_port, dst_port, len(dns_packet))

        return eth_header + ip_header + udp_header + dns_packet

    def make_a_query(self, src_mac, dst_mac, src_ip, dst_ip, src_port, dst_port, tid, names=[], flags=0):
        queries = []

        for name in names:
            queries.append({"type": 1, "class": 1, "name": name})

        return self.make_request_packet(src_mac=src_mac, dst_mac=dst_mac,
                                        src_ip=src_ip, dst_ip=dst_ip,
                                        src_port=src_port, dst_port=dst_port,
                                        tid=tid,
                                        flags=flags,
                                        queries=queries)

    def make_any_query(self, src_mac, dst_mac, src_ip, dst_ip, src_port, dst_port, tid, names=[], flags=0):
        queries = []

        for name in names:
            queries.append({"type": 255, "class": 1, "name": name})

        return self.make_request_packet(src_mac=src_mac, dst_mac=dst_mac,
                                        src_ip=src_ip, dst_ip=dst_ip,
                                        src_port=src_port, dst_port=dst_port,
                                        tid=tid,
                                        flags=flags,
                                        queries=queries)


class DHCPv6_raw:
    # 0                   1                   2                   3
    # 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    # +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    # |   Message   |                   Data :::                      |
    # +-------------+-------------------------------------------------+

    # DHCPv6 Message Types
    # 0	    Reserved
    # 1	    SOLICIT	            [RFC3315]
    # 2	    ADVERTISE	        [RFC3315]
    # 3	    REQUEST	            [RFC3315]
    # 4	    CONFIRM	            [RFC3315]
    # 5	    RENEW	            [RFC3315]
    # 6	    REBIND	            [RFC3315]
    # 7	    REPLY	            [RFC3315]
    # 8	    RELEASE	            [RFC3315]
    # 9	    DECLINE	            [RFC3315]
    # 10	RECONFIGURE	        [RFC3315]
    # 11	INFORMATION-REQUEST	[RFC3315]
    # 12	RELAY-FORW	        [RFC3315]
    # 13	RELAY-REPL	        [RFC3315]
    # 14	LEASEQUERY	        [RFC5007]
    # 15	LEASEQUERY-REPLY	[RFC5007]
    # 16	LEASEQUERY-DONE	    [RFC5460]
    # 17	LEASEQUERY-DATA	    [RFC5460]
    # 18	RECONFIGURE-REQUEST [RFC6977]
    # 19	RECONFIGURE-REPLY	[RFC6977]
    # 20	DHCPV4-QUERY	    [RFC7341]
    # 21	DHCPV4-RESPONSE	    [RFC7341]
    # 22	ACTIVELEASEQUERY	[RFC7653]
    # 23	STARTTLS	        [RFC7653]
    # 24	BNDUPD	            [RFC8156]
    # 25	BNDREPLY	        [RFC8156]
    # 26	POOLREQ	            [RFC8156]
    # 27	POOLRESP	        [RFC8156]
    # 28	UPDREQ	            [RFC8156]
    # 29	UPDREQALL	        [RFC8156]
    # 30	UPDDONE	            [RFC8156]
    # 31	CONNECT	            [RFC8156]
    # 32	CONNECTREPLY	    [RFC8156]
    # 33	DISCONNECT	        [RFC8156]
    # 34	STATE	            [RFC8156]
    # 35	CONTACT	            [RFC8156]
    # 36-255	Unassigned

    eth = None
    ipv6 = None
    udp = None
    dns = None

    def __init__(self):
        self.eth = Ethernet_raw()
        self.ipv6 = IPv6_raw()
        self.udp = UDP_raw()
        self.dns = DNS_raw()

    def get_duid(self, mac_address, timeval=None):
        Hardware_type = 1   # Ethernet
        if timeval is None:
            DUID_type = 3   # Link-Layer address
            return pack("!" "2H", DUID_type, Hardware_type) + self.eth.convert_mac(mac_address)
        else:
            DUID_type = 1   # Link-Layer address plus time
            return pack("!" "2H" "I", DUID_type, Hardware_type, timeval) + self.eth.convert_mac(mac_address)

    def make_packet(self, ethernet_src_mac, ethernet_dst_mac,
                    ipv6_src, ipv6_dst, ipv6_flow, udp_src_port, udp_dst_port,
                    dhcp_message_type, packet_body, options, options_raw=""):
        dhcp_packet = pack("!B", dhcp_message_type)
        dhcp_packet += packet_body

        if options_raw == "":
            for option_code in options.keys():
                dhcp_packet += pack("!" "2H", int(option_code), len(options[option_code]))
                dhcp_packet += options[option_code]
        else:
            dhcp_packet += options_raw

        eth_header = self.eth.make_header(ethernet_src_mac, ethernet_dst_mac, 34525)  # 34525 = 0x86dd (IPv6)
        ipv6_header = self.ipv6.make_header(ipv6_src, ipv6_dst, ipv6_flow, len(dhcp_packet) + 8, 17)  # 17 = 0x11 (UDP)
        udp_header = self.udp.make_header_with_ipv6_checksum(ipv6_src, ipv6_dst, udp_src_port, udp_dst_port,
                                                             len(dhcp_packet), dhcp_packet)

        return eth_header + ipv6_header + udp_header + dhcp_packet

    def make_solicit_packet(self, ethernet_src_mac, ipv6_src, transaction_id, client_identifier, option_request_list):

        if 16777215 < transaction_id < 0:
            return None

        packet_body = pack("!L", transaction_id)[1:]
        options = {}

        options[3] = pack("!" "3Q", 0, 0, 0)  # Identity Association for Non-temporary Address
        options[14] = ""                      # Rapid commit
        options[8] = pack("!H", 0)            # Elapsed time
        options[1] = client_identifier        # Client identifier

        option_request_string = ""
        for option_request in option_request_list:
            option_request_string += pack("!H", option_request)

        options[6] = option_request_string  # Options request

        return self.make_packet(ethernet_src_mac, "33:33:00:01:00:02",
                                ipv6_src, "ff02::1:2", 0, 546, 547,
                                1, packet_body, options)

    def make_relay_forw_packet(self, ethernet_src_mac, ethernet_dst_mac,
                               ipv6_src, ipv6_dst, ipv6_flow,
                               hop_count, link_addr, peer_addr, options, options_raw=""):
        packet_body = pack("!B", hop_count) + self.ipv6.pack_addr(link_addr) + self.ipv6.pack_addr(peer_addr)
        return self.make_packet(ethernet_src_mac, ethernet_dst_mac,
                                ipv6_src, ipv6_dst, ipv6_flow, 546, 547,
                                12, packet_body, options, options_raw)

    def make_advertise_packet(self, ethernet_src_mac, ethernet_dst_mac,
                              ipv6_src, ipv6_dst, transaction_id, dns_address,
                              domain_search, ipv6_address, client_duid_timeval=None, server_duid_mac=None):

        if 16777215 < transaction_id < 0:
            return None

        packet_body = pack("!L", transaction_id)[1:]
        options = {}

        if client_duid_timeval is None:
            options[1] = self.get_duid(ethernet_dst_mac)                       # Client Identifier
        else:
            options[1] = self.get_duid(ethernet_dst_mac, client_duid_timeval)  # Client Identifier

        if server_duid_mac is None:
            options[2] = self.get_duid(ethernet_src_mac)  # Server Identifier
        else:
            options[2] = self.get_duid(server_duid_mac)        # Server Identifier

        options[20] = ""                                     # Reconfigure Accept
        options[23] = self.ipv6.pack_addr(dns_address)       # DNS recursive name server
        options[24] = self.dns.make_dns_name(domain_search)  # Domain search list
        options[82] = pack("!I", 0x3c)                       # SOL_MAX_RT

        options[3] = pack("!" "3I" "2H", 1, 21600, 34560, 5, 24) + self.ipv6.pack_addr(ipv6_address) + \
                     pack("!2I", 0xffffffff, 0xffffffff)     # Identity Association for Non-temporary address

        return self.make_packet(ethernet_src_mac, ethernet_dst_mac,
                                ipv6_src, ipv6_dst,
                                0xa1b82, 547, 546, 2,
                                packet_body, options)

    def make_reply_packet(self, ethernet_src_mac, ethernet_dst_mac,
                              ipv6_src, ipv6_dst, transaction_id, dns_address,
                              domain_search, ipv6_address, client_duid_timeval=None, server_duid_mac=None):

        if 16777215 < transaction_id < 0:
            return None

        packet_body = pack("!L", transaction_id)[1:]
        options = {}

        if client_duid_timeval is None:
            options[1] = self.get_duid(ethernet_dst_mac)                       # Client Identifier
        else:
            options[1] = self.get_duid(ethernet_dst_mac, client_duid_timeval)  # Client Identifier

        if server_duid_mac is None:
            options[2] = self.get_duid(ethernet_src_mac)  # Server Identifier
        else:
            options[2] = self.get_duid(server_duid_mac)   # Server Identifier

        options[20] = ""                                     # Reconfigure Accept
        options[23] = self.ipv6.pack_addr(dns_address)       # DNS recursive name server
        options[24] = self.dns.make_dns_name(domain_search)  # Domain search list
        options[82] = pack("!I", 0x3c)                       # SOL_MAX_RT

        options[3] = pack("!" "3I" "2H", 1, 21600, 34560, 5, 24) + self.ipv6.pack_addr(ipv6_address) + \
                     pack("!2I", 0xffffffff, 0xffffffff)     # Identity Association for Non-temporary address

        return self.make_packet(ethernet_src_mac, ethernet_dst_mac,
                                ipv6_src, ipv6_dst,
                                0xa1b82, 547, 546, 7,
                                packet_body, options)

    # def make_reconfigure_packet(self, ethernet_src_mac, ethernet_dst_mac,
    #                             ipv6_src, ipv6_dst, transaction_id, dns_address,
    #                             domain_search, ipv6_address):
    #     if 16777215 < transaction_id < 0:
    #         return None
    #
    #     packet_body = pack("!L", transaction_id)[1:]
    #     options = {}
    #
    #     options[1] = self.get_duid(ethernet_dst_mac)                       # Client Identifier
    #     options[2] = self.get_duid(ethernet_src_mac)  # Server Identifier
    #
    #     options[20] = ""                                     # Reconfigure Accept
    #     options[23] = self.ipv6.pack_addr(dns_address)       # DNS recursive name server
    #     options[24] = self.dns.make_dns_name(domain_search)  # Domain search list
    #     options[82] = pack("!I", 0x3c)                       # SOL_MAX_RT
    #
    #     options[3] = pack("!" "3I" "2H", 1, 21600, 34560, 5, 24) + self.ipv6.pack_addr(ipv6_address) + \
    #                  pack("!2I", 0xffffffff, 0xffffffff)     # Identity Association for Non-temporary address
    #
    #     return self.make_packet(ethernet_src_mac, ethernet_dst_mac,
    #                             ipv6_src, ipv6_dst,
    #                             0xa1b82, 547, 546, 10,
    #                             packet_body, options)