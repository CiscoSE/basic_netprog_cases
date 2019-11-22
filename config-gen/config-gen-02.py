#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic NetProg Cases Console Script.

Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Russell Johnston"
__email__ = "rujohns2@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


import ipaddress
from jinja2 import Environment, FileSystemLoader

# Set the current directory for source of environment
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

# Define source jinja2 template 
template = env.get_template('bgp_config.j2')

# Get the interface address and its mask in dot notation
intf_addr = input('Enter MPLS interface IP address:\n')
intf_mask = input('Enter MPLS interface Mask (eg. 255.255.255.252):\n')

intf_ip = intf_addr + '/' + intf_mask
# Compute the IP network for the interface use of strict set to false allows
# for a host address to be used to determine its network address
intf_net = ipaddress.ip_network(intf_ip, strict=False)

if intf_net.prefixlen < 30:
    while True:
        mpls_peer = ipaddress.IPv4Address(input('Enter MPLS Providers IP address:\n'))
        # Confirm Entered peer address exists in provided subnet if not reprompt
        if mpls_peer in intf_net.hosts():
            break
        else:
            print('Entered IP not in provided network ' + str(intf_net))
else:
    # If subnet is a /30 then select the remaining address for the peer address
    for addr in list(intf_net.hosts()):
        if addr != ipaddress.IPv4Address(intf_addr):
            mpls_peer = addr

output = template.render(mpls_address=intf_addr, 
                         mpls_peer=str(mpls_peer),
                         mpls_net=str(intf_net.network_address),
                         mpls_mask=intf_mask,
                         local_asn='65000',
                         remote_asn='64000',
                         red_address='2.2.2.1',
                         red_peer='2.2.2.2',
                         red_net='2.2.2.0',
                         )
print('='*30 + '\n')
print('Generated Configuration\n\n' + '='*30 + '\n\n')
print(output)
