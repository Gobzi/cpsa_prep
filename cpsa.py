import random

questions = {
    "What's the default port for FTP Control?": [
        "A) 20",
        "B) 21",
        "C) 22",
        "D) 23",
        "B"
    ],
    "What's the default port for SSH (Secure Shell)?": [
        "A) 21",
        "B) 22",
        "C) 23",
        "D) 80",
        "B"
    ],
    "What's the default port for Telnet?": [
        "A) 21",
        "B) 23",
        "C) 25",
        "D) 80",
        "B"
    ],
    "What's the default port for IMAP (Internet Message Access Protocol)?": [
        "A) 110",
        "B) 143",
        "C) 22",
        "D) 80",
        "B"
    ],
    "What's the default port for SMB (Server Message Block)?": [
        "A) 22",
        "B) 80",
        "C) 445",
        "D) 25",
        "C"
    ],
    "What's the default UDP port for DHCP Server?": [
        "A) 67",
        "B) 68",
        "C) 53",
        "D) 123",
        "B"
    ],
    "What's the default UDP port for NetBIOS Datagram Service?": [
        "A) 137",
        "B) 138",
        "C) 161",
        "D) 162",
        "B"
    ],
    "What's the default UDP port for SNMPTRAP (SNMP Trap)?": [
        "A) 161",
        "B) 162",
        "C) 53",
        "D) 22",
        "B"
    ],
    "What's the default UDP port for RADIUS Accounting?": [
        "A) 1812",
        "B) 1813",
        "C) 514",
        "D) 68",
        "B"
    ],
    "What is the primary risk of XSS?": [
        "A) Data leakage",
        "B) Session hijacking",
        "C) Server overload",
        "B"
    ],
    "What is the main purpose of CSRF attacks?": [
        "A) To steal data",
        "B) To perform unauthorized actions on behalf of the user",
        "C) To crash the server",
        "B"
    ],
    "What is the typical response to an SSRF attack?": [
        "A) Ignoring it",
        "B) Limiting outbound requests",
        "C) Increasing server capacity",
        "B"
    ],
    "What type of attack involves injecting malicious scripts into webpages?": [
        "A) SQLi",
        "B) XSS",
        "C) CSRF",
        "B"
    ],
    "What is the primary objective of using prepared statements?": [
        "A) To improve performance",
        "B) To prevent SQL injection",
        "C) To allow dynamic queries",
        "B"
    ],
    "What is the primary purpose of Class E IP addresses?": [
        "A) To allocate addresses for special use",
        "B) For private networks",
        "C) Reserved for experimental purposes",
        "D) To support multicast groups",
        "C"
    ],
    "What does the IP address 0.0.0.0 represent?": [
        "A) A loopback address",
        "B) A private address",
        "C) An invalid, unknown, or non-applicable target",
        "D) A multicast address",
        "C"
    ],
    "What is the purpose of the IP address range 169.254.0.0/16?": [
        "A) To provide public addresses",
        "B) For link-local addresses when a device cannot obtain an IP address from a DHCP server",
        "C) To support multicast groups",
        "D) For private networks",
        "B"
    ],
    "What type of IP addresses are included in the 192.168.0.0/16 range?": [
        "A) Public IP addresses",
        "B) Reserved IP addresses",
        "C) Private IP addresses used within local networks",
        "D) Loopback addresses",
        "C"
    ],
    "What type of IP addresses are included in the 10.0.0.0/8 range?": [
        "A) Public IP addresses",
        "B) Reserved IP addresses",
        "C) Private IP addresses used within local networks",
        "D) Loopback addresses",
        "C"
    ],
    "What type of IP addresses are included in the 172.16.0.0/12 range?": [
        "A) Public IP addresses",
        "B) Reserved IP addresses",
        "C) Private IP addresses used within local networks",
        "D) Loopback addresses",
        "C"
    ],
    "What is the default port number for PostgreSQL?": [
        "A) 3306",
        "B) 5432",
        "C) 1433",
        "D) 8080",
        "B"
    ],
    "What is the default port number for POP3S?": [
        "A) 110",
        "B) 993",
        "C) 995",
        "D) 8080",
        "C"
    ],
    "What is the default port number for IMAPS?": [
        "A) 143",
        "B) 993",
        "C) 995",
        "D) 587",
        "B"
    ],
    "What is the default port number for RDP?": [
        "A) 22",
        "B) 3389",
        "C) 80",
        "D) 443",
        "B"
    ],
    "What is the default port number for SMB?": [
        "A) 21",
        "B) 23",
        "C) 445",
        "D) 25",
        "C"
    ],
    "How many rounds are required for a 192-bit AES key?": [
        "A) 10",
        "B) 12",
        "C) 14",
        "D) 16",
        "B"
    ],
    "Which version of IIS is installed with Windows Server 2008?": [
        "A) IIS 6.0",
        "B) IIS 7.0",
        "C) IIS 8.0",
        "D) IIS 10.0",
        "B"
    ],
    "Which version of IIS is installed with Windows Server 2012?": [
        "A) IIS 7.5",
        "B) IIS 8.0",
        "C) IIS 8.5",
        "D) IIS 10.0",
        "B"
    ],
    "Which version of IIS is installed with Windows 10?": [
        "A) IIS 8.0",
        "B) IIS 8.5",
        "C) IIS 10.0",
        "D) IIS 7.5",
        "C"
    ],
    "What do the permission bits 'rwxr-xr-x' represent?": [
        "A) Owner has read, write, execute; group has read, execute; others have none",
        "B) Owner has read, write; group has read; others have none",
        "C) Owner has read, write, execute; group has read, execute; others have read, execute",
        "D) Owner has read, write, execute; group has read, execute; others have read, execute",
        "D"
    ],
    "What command is used to query DNS information?": [
        "A) dnsquery",
        "B) nslookup",
        "C) dig",
        "D) All of the above",
        "D"
    ],
    "What is the default port number for MSSQL?": [
        "A) 3306",
        "B) 5432",
        "C) 1433",
        "D) 8080",
        "C"
    ],
    "What's the default port for FTP Data?": [
        "A) 23",
        "B) 20",
        "C) 21",
        "D) 25",
        "B"
    ],
    "What's the default port for SMTP (Simple Mail Transfer Protocol)?": [
        "A) 110",
        "B) 80",
        "C) 25",
        "D) 443",
        "C"
    ],
    "What's the default port for DNS (Domain Name System) over TCP?": [
        "A) 80",
        "B) 22",
        "C) 25",
        "D) 53",
        "D"
    ],
    "What's the default port for HTTP (Hypertext Transfer Protocol)?": [
        "A) 443",
        "B) 21",
        "C) 80",
        "D) 22",
        "C"
    ],
    "What's the default port for POP3 (Post Office Protocol v3)?": [
        "A) 21",
        "B) 143",
        "C) 110",
        "D) 80",
        "C"
    ],
    "What's the default port for HTTPS (HTTP Secure)?": [
        "A) 80",
        "B) 22",
        "C) 443",
        "D) 21",
        "C"
    ],
    "What's the default port for IMAPS (IMAP Secure)?": [
        "A) 443",
        "B) 21",
        "C) 993",
        "D) 80",
        "C"
    ],
    "What's the default port for POP3S (POP3 Secure)?": [
        "A) 443",
        "B) 80",
        "C) 995",
        "D) 21",
        "C"
    ],
    "What's the default port for Microsoft SQL Server?": [
        "A) 3306",
        "B) 1433",
        "C) 1521",
        "D) 5432",
        "B"
    ],
    "What's the default port for Oracle Database?": [
        "A) 1433",
        "B) 1521",
        "C) 3306",
        "D) 5432",
        "B"
    ],
    "What's the default port for MySQL?": [
        "A) 5432",
        "B) 1521",
        "C) 3306",
        "D) 1433",
        "C"
    ],
    "What's the default port for RDP (Remote Desktop Protocol)?": [
        "A) 22",
        "B) 80",
        "C) 3389",
        "D) 23",
        "C"
    ],
    "What's the default port for PostgreSQL?": [
        "A) 3306",
        "B) 1521",
        "C) 5432",
        "D) 1433",
        "C"
    ],
    "What's the default port for VNC (Virtual Network Computing)?": [
        "A) 443",
        "B) 5900",
        "C) 3389",
        "D) 80",
        "B"
    ],
    "What's the alternative HTTP port?": [
        "A) 443",
        "B) 8080",
        "C) 80",
        "D) 22",
        "B"
    ],
    "What's the default port for NTP (Network Time Protocol)?": [
        "A) 80",
        "B) 123",
        "C) 22",
        "D) 53",
        "B"
    ],
    "What's the default port for LDAP (Lightweight Directory Access Protocol)?": [
        "A) 636",
        "B) 80",
        "C) 389",
        "D) 22",
        "C"
    ],
    "What's the default port for LDAPS (LDAP Secure)?": [
        "A) 80",
        "B) 636",
        "C) 389",
        "D) 22",
        "B"
    ],
    "What's the default UDP port for DNS (Domain Name System)?": [
        "A) 80",
        "B) 53",
        "C) 25",
        "D) 22",
        "B"
    ],
    "What's the default UDP port for DHCP Client?": [
        "A) 68",
        "B) 67",
        "C) 53",
        "D) 123",
        "A"
    ],
    "What's the default UDP port for NTP (Network Time Protocol)?": [
        "A) 80",
        "B) 123",
        "C) 53",
        "D) 22",
        "B"
    ],
    "What's the default UDP port for NetBIOS Name Service?": [
        "A) 138",
        "B) 137",
        "C) 53",
        "D) 123",
        "B"
    ],
    "What's the default UDP port for SNMP (Simple Network Management Protocol)?": [
        "A) 162",
        "B) 161",
        "C) 53",
        "D) 22",
        "B"
    ],
    "What's the default UDP port for IKE (Internet Key Exchange)?": [
        "A) 514",
        "B) 500",
        "C) 123",
        "D) 68",
        "B"
    ],
    "What's the default UDP port for Syslog?": [
        "A) 123",
        "B) 514",
        "C) 68",
        "D) 53",
        "B"
    ],
    "What's the default UDP port for RIP (Routing Information Protocol)?": [
        "A) 123",
        "B) 520",
        "C) 68",
        "D) 68",
        "B"
    ],
    "What's the default UDP port for L2TP (Layer 2 Tunneling Protocol)?": [
        "A) 123",
        "B) 1701",
        "C) 68",
        "D) 53",
        "B"
    ],
    "What's the default UDP port for RADIUS Authentication?": [
        "A) 1813",
        "B) 1812",
        "C) 514",
        "D) 68",
        "B"
    ],
    "What's the default UDP port for NFS (Network File System)?": [
        "A) 1812",
        "B) 2049",
        "C) 514",
        "D) 68",
        "B"
    ],
    "What's the default UDP port for IPSec NAT Traversal?": [
        "A) 123",
        "B) 4500",
        "C) 514",
        "D) 68",
        "B"
    ],
    "What's the default UDP port for mDNS (Multicast DNS)?": [
        "A) 123",
        "B) 5353",
        "C) 514",
        "D) 68",
        "B"
    ],
    "What's the default UDP port for X11?": [
        "A) 123",
        "B) 6000",
        "C) 514",
        "D) 68",
        "B"
    ],
    "What's the default UDP port for OpenFlow?": [
        "A) 123",
        "B) 6789",
        "C) 514",
        "D) 68",
        "B"
    ],
    "What does TCP stand for?": [
        "A) Transport Control Protocol",
        "B) Transfer Control Protocol",
        "C) Transmission Command Protocol",
        "D) Transmission Control Protocol",
        "D"
    ],
    "What does UDP stand for?": [
        "A) Universal Datagram Protocol",
        "B) User Data Protocol",
        "C) Unsecured Datagram Protocol",
        "D) User Datagram Protocol",
        "D"
    ],
    "What does IP stand for?": [
        "A) Internal Protocol",
        "B) Intermediate Protocol",
        "C) Interconnected Protocol",
        "D) Inernet Protocol",
        "D"
    ],
    "What does DNS stand for?": [
        "A) Data Network System",
        "B) Domain Name Service",
        "C) Domain Network Service",
        "D) Domain Name System",
        "D"
    ],
    "What does HTTP stand for?": [
        "A) Hyper Transfer Text Protocol",
        "B) Hypertext Transmission Protocol",
        "C) Hypertext Transport Protocol",
        "D) Hypertext Transfer Protocol",
        "D"
    ],
    "What does HTTPS stand for?": [
        "A) Hypertext Transfer Secure",
        "B) HTTP Secure",
        "C) Hypertext Transport Secure",
        "D) Hypertext Transmission Secure",
        "B"
    ],
    "What does FTP stand for?": [
        "A) Fast Transfer Protocol",
        "B) Flexible Transfer Protocol",
        "C) File Transfer Protocol",
        "D) Folder Transfer Protocol",
        "C"
    ],
    "What does SSH stand for?": [
        "A) Secure Server Host",
        "B) Secure Shell",
        "C) Safe Socket Handler",
        "D) Secure Socket Handler",
        "B"
    ],
    "What does SMTP stand for?": [
        "A) Secure Mail Transfer Protocol",
        "B) Simple Mail Transfer Protocol",
        "C) Standard Mail Transfer Protocol",
        "D) Standard Mail Trasmit Protocol",
        "B"
    ],
    "What does IMAP stand for?": [
        "A) Internal Mail Access Protocol",
        "B) Internet Message Access Protocol",
        "C) Interactive Message Access Protocol",
        "D) Internet Message Arial Protocol",
        "B"
    ],
    "What does POP3 stand for?": [
        "A) Postal Office Protocol v3",
        "B) Post Office Protocol Version 3",
        "C) Post Office Protocol v3",
        "D) Peer-to-Peer Protocol 3",
        "C"
    ],
    "What does RDP stand for?": [
        "A) Remote Device Protocol",
        "B) Remote Data Protocol",
        "C) Remote Desktop Protocol",
        "D) Resource Distribution Protocol",
        "C"
    ],
    "What does SNMP stand for?": [
        "A) Standard Network Management Protocol",
        "B) Secure Network Management Protocol",
        "C) Simple Network Management Protocol",
        "D) Synchronized Network Monitoring Protocol",
        "C"
    ],
    "What does DHCP stand for?": [
        "A) Dynamic Host Control Protocol",
        "B) Dynamic Host Configuration Protocol",
        "C) Direct Host Configuration Protocol",
        "D) Domain Host Connection Protocol",
        "B"
    ],
    "What does NTP stand for?": [
        "A) Network Transmission Protocol",
        "B) Network Time Protocol",
        "C) Network Transfer Protocol",
        "D) Network Timing Protocol",
        "B"
    ],
    "What does SMB stand for?": [
        "A) Secure Message Block",
        "B) Server Message Block",
        "C) Standard Message Block",
        "D) Shared Memory Block",
        "B"
    ],
    "What does LDAP stand for?": [
        "A) Lightweight Data Access Protocol",
        "B) Low-level Directory Access Protocol",
        "C) Lightweight Directory Access Protocol",
        "D) Local Directory Authentication Protocol",
        "C"
    ],
    "What does VNC stand for?": [
        "A) Virtual Network Control",
        "B) Virtual Node Computing",
        "C) Virtual Network Computing",
        "D) Virtual Namespace Communication",
        "C"
    ],
    "What does RIP stand for?": [
        "A) Routing Interface Protocol",
        "B) Routing Information Protocol",
        "C) Route Information Protocol",
        "D) Real-time Interchange Protocol",
        "B"
    ],
    "What does L2TP stand for?": [
        "A) Layer 2 Transfer Protocol",
        "B) Layer 2 Tunneling Protocol",
        "C) Layer 2 Transport Protocol",
        "D) Layer 2 Termination Protocol",
        "B"
    ],
    "What does RADIUS stand for?": [
        "A) Remote Access Dial-In User Service",
        "B) Remote Authentication Dial-In User Service",
        "C) Remote Authentication Data User Service",
        "D) Remote Access Data Utility Service",
        "B"
    ],
    "What does mDNS stand for?": [
        "A) Multi-Domain DNS",
        "B) Multicast DNS",
        "C) Multi-Node DNS",
        "D) Multi-Direct DNS",
        "B"
    ],
    "What does BGP stand for?": [
        "A) Base Gateway Protocol",
        "B) Border Group Protocol",
        "C) Border Gateway Protocol",
        "D) Backbone Gateway Protocol",
        "C"
    ],
    "What does ARP stand for?": [
        "A) Address Routing Protocol",
        "B) Address Reference Protocol",
        "C) Address Resolution Protocol",
        "D) Address Registration Protocol",
        "C"
    ],
    "What does CIDR stand for?": [
        "A) Class Inter-Domain Routing",
        "B) Classful Inter-Domain Routing",
        "C) Classless Inter-Domain Routing",
        "D) Class Level Domain Routing",
        "C"
    ],
    "What does VLAN stand for?": [
        "A) Very Large Area Network",
        "B) Virtual Link Area Network",
        "C) Virtual Local Area Network",
        "D) Virtual Line Access Network",
        "C"
    ],
    "What does MPLS stand for?": [
        "A) Multi-Protocol Link Switching",
        "B) Multiprotocol Label Switching",
        "C) Multi-Protocol Local Switching",
        "D) Multi-Purpose Label Switching",
        "B"
    ],
    "What does OSPF stand for?": [
        "A) Open Source Path First",
        "B) Open Shortest Path First",
        "C) Open Source Protocol First",
        "D) Optimal Shortest Path Forward",
        "B"
    ],
    "What does EIGRP stand for?": [
        "A) Enhanced Inter-Gateway Routing Protocol",
        "B) Extended Interior Gateway Routing Protocol",
        "C) Enhanced Interior Gateway Routing Protocol",
        "D) Extended Inter-Gateway Routing Protocol",
        "C"
    ],
    "What does NAT stand for?": [
        "A) Network Address Tracker",
        "B) Network Address Translation",
        "C) Network Address Transformation",
        "D) Network Address Transport",
        "B"
    ],
    "What does PAT stand for?": [
        "A) Port Address Tracker",
        "B) Port Address Translation",
        "C) Port Address Transformation",
        "D) Port Address Tunneling",
        "B"
    ],
    "What does SDN stand for?": [
        "A) Software Data Networking",
        "B) Software-Defined Networking",
        "C) Software-Defined Node",
        "D) Software Data Node",
        "B"
    ],
    "What does WAN stand for?": [
        "A) Wide Area Network",
        "B) Wireless Area Network",
        "C) Wide Access Network",
        "D) Web Access Network",
        "A"
    ],
    "What does LAN stand for?": [
        "A) Large Area Network",
        "B) Local Area Network",
        "C) Link Area Network",
        "D) Logical Access Network",
        "B"
    ],
    "What does WLAN stand for?": [
        "A) Wired Local Area Network",
        "B) Wireless Local Area Network",
        "C) Wireless Link Area Network",
        "D) Wireless Local Access Network",
        "B"
    ],
    "What does MAN stand for?": [
        "A) Medium Area Network",
        "B) Metropolitan Area Network",
        "C) Medium Access Network",
        "D) Multi-Access Network",
        "B"
    ],
    "What does CDN stand for?": [
        "A) Content Delivery Network",
        "B) Content Distribution Network",
        "C) Centralized Delivery Network",
        "D) Caching Delivery Network",
        "A"
    ],
    "What does VPN stand for?": [
        "A) Virtual Protected Network",
        "B) Virtual Private Network",
        "C) Verified Private Network",
        "D) Virtual Public Network",
        "B"
    ],
    "What does DMZ stand for?": [
        "A) Digital Management Zone",
        "B) Demilitarized Zone",
        "C) Dynamic Management Zone",
        "D) Data Management Zone",
        "B"
    ],
    "What does IDS stand for?": [
        "A) Internet Detection System",
        "B) Intrusion Defense System",
        "C) Intrusion Detection System",
        "D) Internal Detection System",
        "C"
    ],
    "What does IPS stand for?": [
        "A) Internet Prevention System",
        "B) Intrusion Protection System",
        "C) Intrusion Prevention System",
        "D) Internal Prevention System",
        "C"
    ],
    "What does SIEM stand for?": [
        "A) Security Information and Event Management",
        "B) Secure Information and Event Management",
        "C) Security Incident and Event Management",
        "D) System Incident and Event Management",
        "A"
    ],
    "What does QoS stand for?": [
        "A) Quantity of Service",
        "B) Quality of Service",
        "C) Quality of System",
        "D) Quality of Signal",
        "B"
    ],
    "What does VoIP stand for?": [
        "A) Voice over Integrated Protocol",
        "B) Voice over Internet Protocol",
        "C) Voice over Internal Protocol",
        "D) Voice over Interconnection Protocol",
        "B"
    ],
    "What does ICMP stand for?": [
        "A) Internet Communication Message Protocol",
        "B) Internet Control Message Protocol",
        "C) Internet Control Management Protocol",
        "D) Internet Command Message Protocol",
        "B"
    ],
    "What does GRE stand for?": [
        "A) Generic Routing Encapsulation",
        "B) General Routing Encapsulation",
        "C) Generic Routing Exchange",
        "D) General Routing Encryption",
        "A"
    ],
    "What does PPP stand for?": [
        "A) Point-to-Point Protocol",
        "B) Point Protocol",
        "C) Packet-to-Point Protocol",
        "D) Packet Processing Protocol",
        "A"
    ],
    "What does HSRP stand for?": [
        "A) High-Availability Standby Router Protocol",
        "B) Hot Standby Router Protocol",
        "C) High-Speed Router Protocol",
        "D) Hybrid Standby Router Protocol",
        "B"
    ],
    "What does VRRP stand for?": [
        "A) Virtual Redundant Routing Protocol",
        "B) Virtual Router Redundancy Protocol",
        "C) Variable Redundancy Routing Protocol",
        "D) Virtual Routing Reliability Protocol",
        "B"
    ],
    "What does TFTP stand for?": [
        "A) Trivial File Transfer Protocol",
        "B) Transfer File Transport Protocol",
        "C) Transmission File Transfer Protocol",
        "D) Tiny File Transfer Protocol",
        "A"
    ],
    "What does SFTP stand for?": [
        "A) Secure File Transfer Protocol",
        "B) Simple File Transfer Protocol",
        "C) Standard File Transfer Protocol",
        "D) Serial File Transfer Protocol",
        "A"
    ],
    "What does SSL stand for?": [
        "A) Secure Socket Layer",
        "B) Secure System Layer",
        "C) Safety Socket Layer",
        "D) Secure Synchronization Layer",
        "A"
    ],
    "What does TLS stand for?": [
        "A) Transport Layer Security",
        "B) Transport Layer Service",
        "C) Transmission Layer Security",
        "D) Transfer Link Security",
        "A"
    ],
    "What does CIFS stand for?": [
        "A) Common Internet File System",
        "B) Common Internal File System",
        "C) Common Inter-Files System",
        "D) Centralized Internet File System",
        "A"
    ],
    "What does API stand for?": [
        "A) Application Program Interface",
        "B) Application Process Interface",
        "C) Application Protocol Interface",
        "D) Application Programming Instruction",
        "A"
    ],
    "What does SaaS stand for?": [
        "A) Software as a Service",
        "B) Software and Service",
        "C) Software as a System",
        "D) Software as a Solution",
        "A"
    ],
    "What does PaaS stand for?": [
        "A) Platform as a Service",
        "B) Platform and Service",
        "C) Platform as a System",
        "D) Platform as a Solution",
        "A"
    ],
    "What does IaaS stand for?": [
        "A) Infrastructure as a Service",
        "B) Information as a Service",
        "C) Infrastructure and Service",
        "D) Infrastructure as a Solution",
        "A"
    ],
    "What does GDPR stand for?": [
        "A) General Data Privacy Regulation",
        "B) General Data Protection Regulation",
        "C) General Digital Protection Regulation",
        "D) Global Data Privacy Regulation",
        "B"
    ],
    "What does PCI DSS stand for?": [
        "A) Payment Card Industry Data Security Standard",
        "B) Payment Card Information Data Security Standard",
        "C) Payment Card Industry Data Security System",
        "D) Payment Credential Industry Data Security Standard",
        "A"
    ],
    "What does CISO stand for?": [
        "A) Chief Information Security Officer",
        "B) Chief Information Service Officer",
        "C) Chief Integrated Security Officer",
        "D) Chief Internet Security Officer",
        "A"
    ],
    "What does DDoS stand for?": [
        "A) Distributed Denial of Service",
        "B) Distributed Data Operating Service",
        "C) Distributed Denial of Security",
        "D) Distributed Denial of System",
        "A"
    ],
    "What does APT stand for?": [
        "A) Advanced Persistent Threat",
        "B) Advanced Protected Threat",
        "C) Advanced Persistent Technology",
        "D) Advanced Penetration Threat",
        "A"
    ],
    "What does MFA stand for?": [
        "A) Multi-Factor Authentication",
        "B) Multi-Factor Authorization",
        "C) Multiple Factor Authentication",
        "D) Multi-Function Authentication",
        "A"
    ],
    "What does CVE stand for?": [
        "A) Common Vulnerabilities and Exposures",
        "B) Common Vulnerability Exploit",
        "C) Common Vulnerability and Exposures",
        "D) Critical Vulnerability Exposures",
        "A"
    ],
    "What does ISO stand for?": [
        "A) International Standard Organization",
        "B) International Standards Organization",
        "C) Internal Security Organization",
        "D) International System Organization",
        "B"
    ],
    "What does NIST stand for?": [
        "A) National Institute of Security Technology",
        "B) National Institute of Standards and Technology",
        "C) National Institute of Security Testing",
        "D) National Information Security Technology",
        "B"
    ],
    "What does PCI stand for?": [
        "A) Payment Card Industry",
        "B) Personal Card Information",
        "C) Payment Control Information",
        "D) Payment Credential Industry",
        "A"
    ],
    "What does SOC stand for?": [
        "A) System Operations Center",
        "B) Security Operations Center",
        "C) Secure Operations Center",
        "D) System Oversight Center",
        "B"
    ],
    "What does IR stand for?": [
        "A) Incident Response",
        "B) Internal Review",
        "C) Information Report",
        "D) Incident Resolution",
        "A"
    ],
    "What does RTO stand for?": [
        "A) Recovery Time Objective",
        "B) Recovery Time Operations",
        "C) Recovery Target Objective",
        "D) Recovery Time Optimization",
        "A"
    ],
    "What does RPO stand for?": [
        "A) Recovery Point Objective",
        "B) Recovery Point Operations",
        "C) Recovery Process Objective",
        "D) Recovery Plan Objective",
        "A"
    ],
    "What does DLP stand for?": [
        "A) Data Loss Prevention",
        "B) Data Leak Prevention",
        "C) Data Loss Protection",
        "D) Data Leak Protection",
        "A"
    ],
    "What does BYOD stand for?": [
        "A) Bring Your Own Device",
        "B) Bring Your Own Data",
        "C) Bring Your Own Desktop",
        "D) Bring Your Online Data",
        "A"
    ],
    "What does EDR stand for?": [
        "A) Endpoint Detection Response",
        "B) Endpoint Data Recovery",
        "C) Endpoint Development Response",
        "D) Endpoint Defense Registry",
        "A"
    ],
    "What does SSO stand for?": [
        "A) Single Security Option",
        "B) Single Sign-On",
        "C) Single System Option",
        "D) Single Session Operation",
        "B"
    ],
    "What does ZTA stand for?": [
        "A) Zero Trust Architecture",
        "B) Zero Trust Access",
        "C) Zero Trusted Architecture",
        "D) Zero Tolerance Authentication",
        "A"
    ],
    "What does SAML stand for?": [
        "A) Security Assertion Markup Language",
        "B) Security Authentication Markup Language",
        "C) Security Assertion Management Language",
        "D) Standard Authentication Markup Language",
        "A"
    ],
    "What does SP stand for?": [
        "A) Security Provider",
        "B) Service Provider",
        "C) System Provider",
        "D) Subscription Provider",
        "B"
    ],
    "What does IdP stand for?": [
        "A) Identity Provider",
        "B) Identification Provider",
        "C) Identity Program",
        "D) Identity Processing",
        "A"
    ],
    "What does WAF stand for?": [
        "A) Web Application Firewall",
        "B) Web Access Firewall",
        "C) Web Authentication Firewall",
        "D) Web Analytics Framework",
        "A"
    ],
    "What does CASB stand for?": [
        "A) Cloud Access Security Broker",
        "B) Cloud Application Security Broker",
        "C) Cloud Access Security Base",
        "D) Cloud Access System Broker",
        "A"
    ],
    "What does FIM stand for?": [
        "A) File Integrity Management",
        "B) File Integrity Monitoring",
        "C) File Inspection Management",
        "D) File Interface Monitoring",
        "B"
    ],
    "What does SAM stand for?": [
        "A) Software Asset Management",
        "B) System Asset Management",
        "C) Security Asset Management",
        "D) System Audit Management",
        "A"
    ],
    "What does VDI stand for?": [
        "A) Virtual Data Interface",
        "B) Virtual Desktop Infrastructure",
        "C) Virtual Device Interface",
        "D) Virtual Deployment Infrastructure",
        "B"
    ],
    "What does HIDS stand for?": [
        "A) Host-based Intrusion Detection System",
        "B) Host-based Information Detection System",
        "C) Host Intrusion Detection System",
        "D) Host-based Incident Detection System",
        "A"
    ],
    "What does NIDS stand for?": [
        "A) Network Intrusion Detection System",
        "B) Network Information Detection System",
        "C) Network Incident Detection System",
        "D) Network Intrusion Defense System",
        "A"
    ],
    "What does YARA stand for?": [
        "A) Yet Another Resource Allocator",
        "B) Yet Another Recursive Acronym",
        "C) Yet Another Regex Application",
        "D) Yet Another Redundant Acronym",
        "B"
    ],
    "What does ZBR stand for?": [
        "A) Zero Byte Recovery",
        "B) Zero Base Recovery",
        "C) Zero Backup Ratio",
        "D) Zero Buffer Recovery",
        "A"
    ],
    "What does FUD stand for?": [
        "A) Fear, Uncertainty, and Doubt",
        "B) Fear, Uncertainty, and Data",
        "C) Fear, Uncertainty, and Distrust",
        "D) Fear, Understanding, and Distrust",
        "A"
    ],
    "What does TTP stand for?": [
        "A) Tools, Techniques, and Procedures",
        "B) Tactics, Techniques, and Procedures",
        "C) Technology, Techniques, and Procedures",
        "D) Testing, Techniques, and Processes",
        "B"
    ],
    "What does C2 stand for?": [
        "A) Command and Control",
        "B) Command to Control",
        "C) Command & Control",
        "D) Communication Control",
        "A"
    ],
    "What does MD5 stand for?": [
        "A) Message-Digest Algorithm 5",
        "B) Message Data Algorithm 5",
        "C) Message Digest Application 5",
        "D) Message Distribution Algorithm 5",
        "A"
    ],
    "What does OTP stand for?": [
        "A) One-Time Protocol",
        "B) One-Time Procedure",
        "C) One-Time Password",
        "D) One-Time Passphrase",
        "C"
    ],
    "What does Kerberos stand for?": [
        "A) Kerberos (Key Distribution Protocol)",
        "B) Kerberos Authentication System",
        "C) Kerberos (Authentication Protocol)",
        "D) Kerberos Identity Management",
        "C"
    ],
    "What does WEP stand for?": [
        "A) Wired Encryption Privacy",
        "B) Wireless Encryption Privacy",
        "C) Wired Equivalent Privacy",
        "D) Wired Encryption Protocol",
        "C"
    ],
    "What does WPA stand for?": [
        "A) Wireless Protected Access",
        "B) Wireless Protection Architecture",
        "C) Wi-Fi Protected Access",
        "D) Wireless Privacy Access",
        "C"
    ],
    "What does WPA2 stand for?": [
        "A) Wireless Protected Access 2",
        "B) Wi-Fi Protected Access 2",
        "C) Wireless Protection Architecture 2",
        "D) Wireless Privacy Access 2",
        "B"
    ],
    "What does WPA3 stand for?": [
        "A) Wireless Protection Architecture 3",
        "B) Wi-Fi Protected Access 3",
        "C) Wireless Privacy Access 3",
        "D) Wireless Protected Access 3",
        "B"
    ],
    "What does TKIP stand for?": [
        "A) Temporary Key Integrity Protocol",
        "B) Time Key Integrity Protocol",
        "C) Temporal Key Integrity Protocol",
        "D) Temporal Key Interface Protocol",
        "C"
    ],
    "What does CORS stand for?": [
        "A) Cross-Organizational Resource Sharing",
        "B) Cross-Origin Resource System",
        "C) Cross-Origin Resource Sharing",
        "D) Cross-Operating Resource Sharing",
        "C"
    ],
    "What does XSS stand for?": [
        "A) Cross-Site System",
        "B) Cross-Site Structure",
        "C) Cross-Site Scripting",
        "D) Cross-Site Security",
        "C"
    ],
    "What does SQLi stand for?": [
        "A) SQL Injection",
        "B) Structured Query Injection",
        "C) SQL Interception",
        "D) SQL Insertion",
        "A"
    ],
    "What does XXE stand for?": [
        "A) XML External Entry",
        "B) XML Encapsulation Entry",
        "C) XML External Entity",
        "D) XML Encapsulated Entity",
        "C"
    ],
    "What does CSRF stand for?": [
        "A) Cross-Server Request Forgery",
        "B) Cross-Session Request Forgery",
        "C) Cross-Site Request Forgery",
        "D) Cross-Site Resource Forgery",
        "C"
    ],
    "What does SSRF stand for?": [
        "A) Server-Side Resource Forgery",
        "B) Server-Side Response Forgery",
        "C) Server-Side Request Forgery",
        "D) Server-Side Routing Failure",
        "C"
    ],
    "What is a common defense against SQL injection?": [
        "A) Disabling cookies",
        "B) Using weak passwords",
        "C) Input validation",
        "D) Using plaintext passwords",
        "C"
    ],
    "What does the Same-Origin Policy protect against?": [
        "A) SQL injections",
        "B) Malware downloads",
        "C) Cross-origin attacks",
        "D) Buffer overflows",
        "C"
    ],
    "What is the purpose of a Content Security Policy (CSP)?": [
        "A) To encrypt data",
        "B) To block ads",
        "C) To define which resources can be loaded",
        "D) To compress web pages",
        "C"
    ],
    "What is the primary purpose of Class D IP addresses?": [
        "A) To allocate addresses for special use",
        "B) To support VPNs",
        "C) To support multicast groups",
        "D) For private networks",
        "C"
    ],
    "What is the purpose of the IP address 127.0.0.1?": [
        "A) It is a public address for the internet",
        "B) It is used for subnetting",
        "C) It is used for loopback and testing within the local machine",
        "D) It represents an invalid target",
        "C"
    ],
    "What does NFS stand for?": [
        "A) Network Folder Sharing",
        "B) Network Folder System",
        "C) Network File System",
        "D) Network File Storage",
        "C"
    ],
    "What does CBC stand for in cryptography?": [
        "A) Code Block Chaining",
        "B) Cryptographic Block Creation",
        "C) Cipher Block Chaining",
        "D) Cipher Base Chaining",
        "C"
    ],
    "What is a salted SHA-1 hash?": [
        "A) A hash with no value added",
        "B) A hash with a fixed length",
        "C) A hash with a random value added",
        "D) A hash that is encrypted",
        "C"
    ],
    "What type of hash is MD5?": [
        "A) A 32-bit hash function",
        "B) A 256-bit hash function",
        "C) A 128-bit hash function",
        "D) A 512-bit hash function",
        "C"
    ],
    "What is the key size for DES?": [
        "A) 32 bits",
        "B) 64 bits",
        "C) 56 bits",
        "D) 128 bits",
        "C"
    ],
    "What is the umask value used for if the default permission is 755?": [
        "A) 002",
        "B) 044",
        "C) 022",
        "D) 027",
        "C"
    ],
    "What does rwho command do?": [
        "A) None of the above",
        "B) Kills user sessions",
        "C) Displays users logged into the system",
        "D) Logs out users",
        "C"
    ],
    "What is the purpose of rsh?": [
        "A) Secure file transfer",
        "B) Remote file transfer",
        "C) Allows users to execute shell commands on remote machines",
        "D) Secure remote login",
        "C"
    ],
    "What does RTP stand for in VoIP?": [
        "A) Real-time Processing",
        "B) Real-time Transfer Protocol",
        "C) Real-time Transport Protocol",
        "D) Real-time Transmission Protocol",
        "C"
    ],
    "What is the main purpose of STP?": [
        "A) Supports spanning networks",
        "B) Provides encryption",
        "C) Prevents loops in network topologies",
        "D) Routes traffic",
        "C"
    ],
    "What does PPTP stand for?": [
        "A) Private Point Tunneling Protocol",
        "B) Protocol for Point-to-Point",
        "C) Point-to-Point Tunneling Protocol",
        "D) Point-to-Point Transfer Protocol",
        "C"
    ],
    "What is IKE in VPNs?": [
        "A) Internet Knowledge Exchange",
        "B) Internet Keying Encryption",
        "C) Internet Key Exchange",
        "D) Internet Key Encryption",
        "C"
    ],
    "What does IPsec stand for?": [
        "A) Internet Packet Security",
        "B) Internet Protocol Security",
        "C) Internet Protocol Segmentation",
        "D) Internet Payload Security",
        "B"
    ],
    "What does RPC stand for?": [
        "A) Remote Program Call",
        "B) Remote Processing Component",
        "C) Remote Procedure Call",
        "D) Remote Process Call",
        "C"
    ],
    "What is a null session in networking?": [
        "A) A secure connection",
        "B) A failed connection",
        "C) An unauthenticated connection to a Windows machine",
        "D) A logged-in user session",
        "C"
    ],
    "What does the rwho command do?": [
        "A) Kills user sessions",
        "B) Monitors system logs",
        "C) Displays users logged into the system",
        "D) Logs out users",
        "C"
    ]
}
def flashcard_game():
    question_list = list(questions.items())
    random.shuffle(question_list)
    print("Type your answer, hit Enter to skip, or type 'exit' to quit\n")

    for question, answer in question_list:
        print(question, "\n")
        if isinstance(answer, list):
            for option in answer[:-1]:
                print(option)
            user_answer = input("\nYour answer: ")
            if user_answer.lower() == 'exit':
                print("\nExiting the game.")
                break
            correct_answer_letter = answer[-1]
            correct_answer_value = answer[ord(correct_answer_letter) - ord('A')]

            if user_answer.upper() == correct_answer_letter:
                print("\nCorrect! The answer is:", correct_answer_value, "\n")
            else:
                print("\nIncorrect! The correct answer is:", correct_answer_value, "\n")
flashcard_game()
