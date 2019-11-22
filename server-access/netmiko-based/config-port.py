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


from netmiko import Netmiko
from jinja2 import Environment, FileSystemLoader
import yaml
from getpass import getpass

# Load inventory file and store to dictionary
with open('inventory.yaml', 'r') as yfile:
    data = yaml.load(yfile, Loader=yaml.FullLoader)
    yfile.close()

for device in data:
    print(device)

template_option = [
    {'template':'mgmt_port','j2file':'managementport.j2'},
    {'template':'server_port', 'j2file':'serverport.j2'}
]
sel_device = input('Enter the name of the device to connect to\n')

i = 0
for option in template_option:
    i += 1
    print('%d : %s' %(i, option['template']))

sel_template = int(input('Select Template to Deploy\n'))
sel_template -= 1
port_template = template_option[sel_template]['j2file']

port = input('Enter Port to be configured\n')
description = input('Enter port description\n')

host = {
    "host": data[sel_device]['ip_addr'],
    "username": input("Username: "),
    "password": getpass("Password: "),
    "device_type": data[sel_device]['device_type']
}

# Set the current directory for source of environment
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

# Define source jinja2 template
template = env.get_template(port_template)

if sel_template is 0:
    config_output = template.render(
        intf_name=port,
        vlan=data[sel_device]['mgmt_vlan']
    )
if sel_template is 1:
    config_output = template.render(
        intf_name=port,
        native_vlan=data[sel_device]['native_vlan'],
        vlan_list=data[sel_device]['vlan_list']
    )
print(config_output)

print('\nConnecting to device ' + str(data[sel_device]['ip_addr']))

net_connect = Netmiko(**host)
output = net_connect.send_config_set(config_output)
print(output)

net_connect.save_config()
net_connect.disconnect()
