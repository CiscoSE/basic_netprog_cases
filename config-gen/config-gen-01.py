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


from jinja2 import Environment, FileSystemLoader

# Set the current directory for source of environment
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

# Define source jinja2 template 
template = env.get_template('bgp_config.j2')

output = template.render(mpls_address='1.1.1.1', 
                         mpls_peer='1.1.1.2',
                         mpls_net='1.1.1.0',
                         mpls_mask='255.255.255.252',
                         local_asn='65000',
                         remote_asn='64000',
                         red_address='2.2.2.1',
                         red_peer='2.2.2.2',
                         red_net='2.2.2.0',
                         )
print('='*30 + '\n')
print('Generated Configuration\n' + '='*30 + '\n\n')
print(output)
