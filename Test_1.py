# Question: (Answers); Answers are in tuple format, so they can act as a key in a dictionary
# I think I abandoned that idea, though, so they probably don't need to be a tuple. I'm not gonna take the time to
# change that, though.
questions = {'A small business enables multiple devices on its private network to share a single public IP address '
             'when accessing the internet. This setup hides the internal IP addresses of devices from external '
             'networks.'
             '\n\nWhich network technology concept is being utilized in this scenario?\n':
                 ('DNS',
                  'VLAN',
                  'DHCP',
                  'NAT'),

             'A large enterprise uses a network service that automatically assigns IP addresses to client devices, '
             'ensuring each device receives the appropriate network configuration without manual intervention.\n\n'
             'Which network technology concept does this scenario illustrate?\n':
                 ('NAT',
                  'DNS',
                  'FTP',
                  'DHCP'),

             'Which term describes a configuration where multiple networks are connected over a large geographic area, '
             'sharing data and resources efficiently?\n':
                 ('MAN',
                  'WAN',
                  'PAN',
                  'LAN'),

             'Which network topology connects all nodes to a central device, like a switch, to ensure minimal '
             'disruption when a single link fails?\n':
                 ('Bus',
                  'Star',
                  'Ring',
                  'Mesh'),

             'What type of device connects different networks and determines the best path for data transmission?\n':
                 ('Access point',
                  'Router',
                  'Hub',
                  'Switch'),

             'A network administrator on a Windows computer wants to test the connectivity to a remote server and '
             'measure the response time.\n\n'
             'Which network troubleshooting command should the administrator use?\n':
                 ('nslookup',
                  'tracert',
                  'ipconfig',
                  'ping'),

             'A Linux system administrator needs to view a server’s current network configuration details, such as IP '
             'address and subnet mask.\n\n'
             'Which command should they use?\n':
                 ('nslookup',
                  'ping',
                  'traceroute',
                  'ifconfig'),

             'An administrator on a Windows machine wants to check how the local DNS server resolves a particular '
             'domain name to an IP address. \n\n'
             'Which command should the administrator use?\n':
                 ('netstat',
                  'ipconfig',
                  'ping',
                  'nslookup'),

             'When troubleshooting DNS issues on a Linux system, which command should you use to query DNS servers to '
             'resolve domain names?\n':
                 ('traceroute',
                  'ifconfig',
                  'ping',
                  'dig'),

             'Which command on Linux provides detailed information about current network connections?\n\n':
                 ('traceroute',
                  'netstat',
                  'ping',
                  'route'),

             'Which OSI model layer provides end-to-end data transmission services and ensures complete data '
             'transfer?\n':
                 ('Application layer',
                  'Transport layer',
                  'Data link layer',
                  'Network layer'),

             'Which OSI layer is responsible for logical addressing and routing packets between devices across '
             'different networks?\n':
                 ('Physical layer',
                  'Network layer',
                  'Transport layer',
                  'Data link layer'),

             'At which OSI layer should you categorize an Ethernet switch that forwards frames based on MAC '
             'addresses?\n':
                 ('Transport layer',
                  'Data link layer',
                  'Network layer',
                  'Physical layer'),

             'A router determines the best path for data packets to travel across multiple networks.\n\n'
             'At which OSI layer does the router primarily operate?\n':
                 ('Physical layer',
                  'Transport layer',
                  'Network layer',
                  'Data link layer'),

             'When a user accesses a website using HTTPS, at which TCP/IP layer does the HTTPS protocol operate?\n':
                 ('Application layer',
                  'Internet layer',
                  'Network access layer',
                  'Transport layer'),

             'Which type of cloud service allows users to develop and deploy applications on a platform without '
             'managing the underlying infrastructure?\n':
                 ('Virtual desktop infrastructure [VDI]',
                  'Platform as a service [PaaS]',
                  'Software as a service [SaaS]',
                  'Infrastructure as a service [IaaS]'),

             'A company uses an email service that requires no installation or maintenance of the application on local '
             'devices.\n\n'
             'Which cloud model does this describe?\n':
                 ('Virtualization',
                  'Platform as a service [PaaS]',
                  'Infrastructure as a service [IaaS]',
                  'Software as a service [SaaS]'),

             'Which virtualization technology enables multiple operating systems to run on a single physical '
             'machine?\n':
                 ('Platform as a service [PaaS]',
                  'Hypervisors',
                  'Software as a service [SaaS]',
                  'Cloud computing'),

             'A business uses a third-party service to host its virtual desktops and provide secure remote access to '
             'employees.\n\n'
             'Which type of solution is being used?\n':
                 ('Public cloud',
                  'Virtual desktop infrastructure [VDI]',
                  'Software as a service [SaaS]',
                  'Infrastructure as a service [IaaS]'),

             'A company uses its on-premises data center to store sensitive data while running some customer-facing '
             'applications in a public cloud environment. They have integrated both environments, enabling data and '
             'applications to move between them seamlessly.\n\n'
             'Which type of virtual and cloud computing solution does this scenario describe?\n':
                 ('Infrastructure as a service [IaaS]',
                  'Private cloud',
                  'Public cloud',
                  'Hybrid cloud')
             }

# In format of aq'n'_response create full response list in All_Tests module
responses = {
    'aq1_response':
        ['Try again. Domain name system [DNS] resolves domain names to IP addresses. It is not responsible for '
         'allowing multiple devices to share a single public IP address for internet access.',
         'Try again. A virtual local area network [VLAN] divides a physical network into multiple logical segments. '
         'While this improves security and efficiency, it does not enable multiple devices to share a single public IP '
         'address.',
         'Try again. Dynamic host configuration protocol [DHCP] automatically assigns IP addresses to devices on a '
         'network. While DHCP manages IP addresses internally, it does not allow multiple devices to share a single '
         'public IP address externally.',
         'That’s right! Network address translation [NAT] allows multiple devices on a private network to access the '
         'internet using a single public IP address. It translates internal private IP addresses to the public IP '
         'address, enabling all devices to share that public address as described in the scenario.'],

    'aq2_response':
        ['Try again. Network address translation [NAT] translates private IP addresses to a public IP address and '
         'allows devices on a private network to access external networks. It does not automatically assign IP '
         'addresses to network devices.',
         'Try again. The domain name system [DNS] translates domain names into IP addresses and vice versa. Although '
         'important for network connectivity, it does not automatically assign IP addresses to devices.',
         'Try again. File transfer protocol [FTP] is used to transfer files between devices over a network. It does '
         'not assign IP addresses or manage network configurations for client devices.',
         'That’s right! Dynamic host configuration protocol [DHCP] automatically assigns IP addresses and other '
         'network configuration parameters to devices on a network. This process allows each device to connect to the '
         'network with the correct settings without manual configuration, exactly as described in the scenario.'
         ],

    'aq3_response':
        ['Try again. A metropolitan area network (MAN) spans a city or campus, which is larger than a LAN but '
         'typically does not cover a wide region like a WAN.',
         'That’s right! A wide area network [WAN] connects multiple networks over large geographic areas, allowing '
         'them to communicate and share resources.',
         'Try again. A personal area network [PAN] is designed for personal devices within a very short range, '
         'typically a few meters.',
         'Try again. A local area network [LAN] covers a smaller, localized area, such as a home or office, and does '
         'not typically span geographic regions'],

    'aq4_response':
        ['Try again. A bus topology uses a single cable, and any disruption affects the entire network.',
         'That’s right! A star topology connects devices to a central device, ensuring localized failure.',
         'Try again. A ring topology connects devices in a circle, so failure disrupts the entire network.',
         'Try again. A mesh topology connects all devices to each other, which is expensive but redundant.'],

    'aq5_response':
        ['Try again. Access points enable wireless devices to join a network.',
         'That’s right! Routers connect different networks and manage data routing.',
         'Try again. Hubs are basic devices that send data to all connected devices.',
         'Try again. Switches connect devices within the same network, not between networks.'],

    'aq6_response':
        ['Try again. The nslookup command is used to query DNS servers to find the IP address associated with a domain '
         'name or vice versa. While it helps troubleshoot DNS-related issues, it does not test connectivity or measure '
         'response times.',
         'Try again. The tracert command is a Windows command that traces the path the packets take to reach a '
         'destination, showing each hop along the route and the time it takes. Although it provides route information, '
         'it is not solely for checking basic connectivity and round-trip time.',
         'Try again. The ipconfig command in Windows displays the network configuration details of the local machine, '
         'such as the IP address and default gateway. It does not test connectivity to a remote server or measure '
         'response time.',
         'That’s right! The ping command in Windows sends ICMP echo requests to a specified host to check connectivity '
         'and measure the response time (round-trip time). This command is exactly what the administrator needs to '
         'verify the server’s reachability.'],

    'aq7_response':
        ['Try again. The nslookup command queries DNS servers to find domain names corresponding to IP addresses or '
         'vice versa. It does not provide information about the local server’s network configuration.',
         'Try again. The ping command sends ICMP echo requests to test network connectivity and measure response '
         'times. It does not display the local server’s network configuration details.',
         'Try again. The traceroute command traces the path packets take from the source to a destination, showing '
         'each hop. While useful for routing and connectivity issues, it does not display network configuration '
         'details of the local server.',
         'That’s right! The ifconfig command in Linux displays the current network configuration, including IP '
         'addresses, subnet masks, and other interface settings. This command provides exactly the information the '
         'administrator needs about the server’s network settings.'],

    'aq8_response':
        ['Try again. The netstat command displays network connections, routing tables, and other interface statistics. '
         'It does not query DNS for domain name resolution.',
         'Try again. The ipconfig command displays the local network configuration, including the current IP address, '
         'subnet mask, and default gateway. It does not resolve domain names to IP addresses.',
         'Try again. While the ping command can show the IP address associated with a domain name by testing '
         'connectivity, it does not specifically query the DNS server for name resolution details.',
         'That’s right! The nslookup command is used to query DNS servers and check DNS resolution. By entering a '
         'domain name, it returns the corresponding IP address as resolved by the DNS server, matching the scenario’s '
         'requirements.'],

    'aq9_response':
        ['Try again. traceroute traces the path packets take but does not resolve domain names through DNS.',
         'Try again. ifconfig displays network interface information but does not perform DNS queries.',
         'Try again. ping checks network connectivity, not DNS resolution.',
         'That’s right! Dig is a DNS lookup utility that queries DNS servers to resolve domain names to IP addresses.'],

    'aq10_response':
        ['Try again. traceroute identifies the path data takes but does not show connections.',
         'That’s right! netstat provides details on current network connections.',
         'Try again. ping checks connectivity but does not show connection details.',
         'Try again. route manages routing tables but does not show connections.'],

    'aq11_response':
        ['Try again. The application layer interacts with application software but does not handle data transport.',
         'That’s right! The transport layer is responsible for end-to-end communication and error recovery, ensuring '
         'complete data transfer between the source and destination.',
         'Try again. The data link layer provides node-to-node data transfer—a link between two directly connected '
         'nodes.',
         'Try again. The network layer handles packet forwarding, including routing through intermediate routers, not '
         'end-to-end data transmission.'],

    'aq12_response':
        ['Try again. The physical layer deals with the actual transmission of data over the physical medium, not '
         'routing or addressing.',
         'That’s right! The network layer handles logical addressing (IP addresses) and routing packets between '
         'different networks.',
         'Try again. The transport layer manages data transfer between systems but does not handle routing or '
         'addressing.',
         'Try again. The data link layer handles communication within the same network and manages physical addresses '
         'like MAC addresses, not logical addresses.'],

    'aq13_response':
        ['Try again. The transport layer is responsible for error-checking and ensuring the correct delivery of data, '
         'but it does not forward frames.',
         'That’s right! Ethernet switches operate at the data link layer, forwarding frames based on MAC addresses.',
         'Try again. The network layer handles logical addressing and routing, not frame forwarding based on MAC '
         'addresses.',
         'Try again. The physical layer manages the actual transmission of data as electrical signals, not the '
         'forwarding of frames.'],

    'aq14_response':
        ['Try again. The physical layer deals with the actual transmission of signals, not with routing.',
         'Try again. The transport layer ensures reliable communication but does not handle path determination between '
         'networks.',
         'That’s right! Routers operate at the network layer (layer 3), which is responsible for routing data packets '
         'between networks.',
         'Try again. The data link layer handles frame transmission within a single local network, not between '
         'multiple networks.'],

    'aq15_response':
        ['That’s right! HTTPS operates at the application layer, handling secure web communication.',
         'Try again. The internet layer is responsible for routing and IP addressing, not secure web communication.',
         'Try again. The network access layer handles the physical network transmission, but HTTPS operates at a '
         'higher layer.',
         'Try again. The transport layer ensures reliable delivery of data but does not handle application protocols '
         'like HTTPS.'],

    'aq16_response':
        ['Try again. VDI refers to virtual desktop environments, not application platforms.',
         'That’s right! PaaS provides platforms with preinstalled tools for application development.',
         'Try again. SaaS provides access to ready-to-use software, not development platforms.',
         'Try again. IaaS provides basic virtual infrastructure like virtual machines and storage.'],

    'aq17_response':
        ['Try again. Virtualization underpins cloud computing but does not define this service model.',
         'Try again. PaaS supports application development but does not provide ready-to-use software.',
         'Try again. IaaS provides infrastructure resources, not complete software solutions.',
         'That’s right! SaaS allows users to access applications like email without managing installations.'],

    'aq18_response':
        ['Try again. PaaS provides tools for development but does not directly implement hypervisors.',
         'That’s right! Hypervisors allow multiple operating systems to run on one physical machine.',
         'Try again. SaaS provides software applications but does not involve managing operating systems.',
         'Try again. Cloud computing uses virtualization but does not focus on hypervisors.'],

    'aq19_response':
        ['Try again. A public cloud refers to shared resources, not specifically VDI services.',
         'That’s right! VDI enables remote access to virtual desktops hosted by a third-party service.',
         'Try again. SaaS focuses on software applications, not desktop hosting.',
         'Try again. IaaS provides virtual infrastructure but does not focus on desktop environments.'],

    'aq20_response':
        ['Try again. IaaS is a cloud computing model where virtualized resources are provided over the internet for '
         'organizations to manage. While IaaS can be part of a hybrid cloud solution, the scenario describes a '
         'combination of private and public resources.',
         'Try again. A private cloud is dedicated to a single organization and is not shared externally. The scenario '
         'involves using both on-premises (private) infrastructure and public cloud services.',
         'Try again. A public cloud provides services over the internet and is shared among multiple organizations. '
         'This scenario specifically mentions the combination of on-premises infrastructure with a public cloud, '
         'which does not describe a public cloud.',
         'That’s right! A hybrid cloud combines a private cloud (the on-premises data center) with a public cloud '
         'service, allowing seamless data and application movement between both environments. This matches the '
         'scenario where sensitive data stays on-premises, and customer-facing applications run in the public cloud.']
}

quest_key_list = list(questions.keys())
resp_key_list = list(responses.keys())
answer_response = {}

