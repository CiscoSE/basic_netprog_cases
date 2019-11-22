# Initialize a Basic 2 Tier Data Center

### Author: Russell Johnston

Using Ansible to base line a 2 tier data center network, with basic connectivity. The network is based on the VIRL topology file located in the projects root directory. Once VIRL topology is strated and nodes are reachable using ansible the network can be initialized using the following.

    ansible-playbook init-dc.yaml

This will set up a pair of Nexus9000v to simulate a core pair with VPC configured. Two additional pairs for Nexus9000v are configured to operate as distribution/access layer in a data center. Basic features are enabled.

Once the topology is initialized use the other examples that are included in this project to configure different use cases.

Monitor nodes in VM Maestro, if any nodes fail to start after a prolonged period stop the node and restart.

Live Visualization - http://10.10.20.160:19402

All nodes are accessible via SSH using the following details:

* **Username:** admin
* **Password:** cisco

* **Core:**
    * n9k-core-1: 172.16.30.101
    * n9k-core-2: 172.16.30.102

* **Distribution/Access:**
    * n9k-dist-1a: 172.16.30.111
    * n9k-dist-1b: 172.16.30.112
    * n9k-dist-2a: 172.16.30.121
    * n9k-dist-2b: 172.16.30.122

This topology is built using Cisco DevNet Sandbox Multi-IOS, if deploying outside that environment IP addresses may need to be updated.
