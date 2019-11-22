# Basic NetProg Cases

*Repository of basic introductory network programmability use cases*

---

## Motivation

This project was created to help customers that are not sure where to start with network programmability. The goal was to highlight some small Python scripts as well as a brief introduction to Ansible and Genie.

## Demos / Use Cases

This project is based on 3 use cases to show where automation can be used.

- Generate Configuration files from templates
- Configure switch ports using ansible project and netmiko
- Provision a new VLAN across a data center from core to ToR switching using ansible project


## Technologies & Frameworks Used

The scripts provided use the following tools or modules to complete the tasks.

**Cisco Products & Services:**

- pyATS Genie

**Tools & Frameworks:**

- Ansible Project

**Python Modules:**

- netmiko
- csv
- Jinja2
- ipaddress
- getpass

## Usage

The scripts provided are designed to be used to provide a demonstation of some simple use cases in network automation and to be presented in a demonstation setting using the Cisco DevNet Sandbox Multi-IOS sandbox.

Refer to the demo-script.md for steps to execute the demo scenarios.

## Installation

To start using these demo use cases and scripts complete the following steps. The steps have been validated on macOS and linux subsystem for windows, use on windows may require additional steps that are not documented here. 

*Prerequisites*
- Python3.7 installed
- pip (included in Python3)
- A active reservation for Cisco DevNet  Multi-IOS sandbox
  - A free DevNet account is required
- Assumed previous experience starting a Virl topology using VMMaestro

*Installation Steps*
1. Clone down repository to your local workstation
        
        git clone https://github.com/CiscoSE/basic_netprog_cases.git
2. Move to the cloned directory root

        cd basic_netprog_cases
3. Prepare virtual environment

        make prepenv
4. See demo-script.md for steps to complete demonstrations.

It is estimated that about 15 minutes is required to start to topology, the topology is requried for use cases 2 and 3 only.

## Authors & Maintainers

Smart people responsible for the creation and maintenance of this project:

- Russell Johnston <rujohns2@cisco.com>

## Credits

Much of the learnings are inspired by the content created by @hpreston especially his [NetDevOps Live](https://developer.cisco.com/netdevops/live/) series on Cisco DevNet. 

A thank you to @bigevilbeard, the foundation of the Jinja2 content comes from his blog post on cisco.com. 

> [Render your first network configuration template using Python and Jinja2](https://blogs.cisco.com/developer/network-configuration-template)

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
