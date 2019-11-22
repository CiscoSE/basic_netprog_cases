# Demo Steps
## Enable virtual environment and topology
Once the DevNet virl topology is reachable and all nodes are active complete the following:

1. Enable python virtual environment from root of project directory

        source .venv/bin/activate

2. Issue the following make command to configure the topology.

        make topology

Once the ansible playbook is complete you should have 12 changes and the demonstration topology should be ready for use cases 2 and 3.

## Config Generation Demonstration
    cd config-gen

### Demo 1 Review basic configuration script 
    code config-gen-01.py

Review the Jinja2 template
    code bgp-config.j2

Execute script and review output
    
    python config-gen-01.py

### Demo 2 Review evolution of script by making script interactive
    python config-gen-02.py

### Demo 3 Review evolution of script by outputing config to folder
    python config-gen-03.py
    
### Demo 4 Review evolution of script using CSV for input file and output to folder
    python config-gen-04.py

## Configure ports based on port templates
    cd ../server-access/

Complete a learn of interfaces on **n9k-dist-1a** and **n9k-dist-1b** to illustrate genie, Discuss Genie learn capabilities for use during changes 
    
    cd genie

    genie learn interface --testbed-file devices.yaml --devices n9k-dist-1a --output learn1a

    genie learn interface --testbed-file devices.yaml --devices n9k-dist-1b --output learn1b

### Demo 1 Implement a change to a port on n9k-dist-1a using netmiko on port eth1/10
    cd ../netmiko-based

Review the inventory file and the script
- inventory.yaml
- config-port.py

Execute script and configure eth1/10 on either switch.

    python config-port.py

### Demo 2 Implement a change to a port on n9k-dist-1b using ansible
    cd ../ansible-based

Review the Inventory file and the playbook
  
- inventory.yaml
- config-server-port.yaml

Execute the ansible playbook and demostrate running a second time showing that changes are only made if required.

    ansible-playbook config-server-port.yaml

### Demo 3 Genie Verification

Return to genie folder and learn interfaces again and complete diff showing the actual change expected has been completed
    cd ../genie

    genie learn interface --testbed-file devices.yaml --devices n9k-dist-1a --output change1a

    genie learn interface --testbed-file devices.yaml --devices n9k-dist-1b --output change1b

show diff of the configuration
    
    genie diff learn1a change1a

    cat diff_interface_nxos_n9k-dist-1a_ops.txt

Bring up the learn module and call out the number of options so if a change to an interface is complete learning bgp could be done before and after and confirmation the route table changed as expected could be done easily with out relying on a visual human review

## Configure Vlans across Data Center from core to distribution Demonstration
    cd ../../dc-vlan/ansible-based

    ansible-playbook config-vlan.yaml

Complete Demo and deactivate virtual environment
    
    deactivate

## Clean up Demo Artificates
These are for linux and macOS leveraging Make to clean up after the demo. By using this any SSH keys added or output files are removed without manually searching for them.

    cd ../..
    
    make cleanup

