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
import csv

# Set the current directory for source of environment
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

# Define source jinja2 template 
template = env.get_template('bgp_config.j2')

# import the csv file with the configuration needed in to a list
bgp_configs = []
with open('input/bgp.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=',')
    for line in reader:
        bgp_configs.append(line)
    f.close()

for config in bgp_configs:
    # Compute the IP network for the interface use of strict set to false allows
    # for a host address to be used to determine its network address
    intf_ip = config['mpls_addr'] + '/' + config['mpls_mask']
    intf_net = ipaddress.ip_network(intf_ip, strict=False)
    # Confirm Entered peer address exists in provided subnet
    if ipaddress.IPv4Address(config['mpls_peer']) not in intf_net.hosts():
        print('Error with MPLS Information')
    else:
        # Write configuration to file with name of mple interface as part of filename
        filename = 'output/' + config['mpls_addr'] + '_bgp.txt'
        output = template.render(mpls_address=config['mpls_addr'],
                                 mpls_mask=config['mpls_mask'],
                                 mpls_peer=config['mpls_peer'],
                                 mpls_net=str(intf_net.network_address),
                                 local_asn='65000',
                                 remote_asn='64000',
                                 red_address='2.2.2.1',
                                 red_peer='2.2.2.2',
                                 red_net='2.2.2.0')
        with open(filename, 'w') as f:
            f.write(output)
            f.close()
