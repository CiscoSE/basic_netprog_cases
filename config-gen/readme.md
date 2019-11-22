# Using Python and Jinja2 to Generate Standardized Configurations

### Author: Russell Johnston

The included scripts and templates are to provide a demonstration of being able to generate network configurations by inputting specific details and outputting the configuration.

A few scripts are included to provide learning and demonstration of how the scripts build out.
* config-gen-01.py - Is foundational using static content to create a config displayed to the terminal after execution.
* config-gen-02.py - Builds on the first script adding interaction with the user when executed to output a configuration to the terminal
* config-gen-03.py - Builds on the second script by outputing the configuration to a *bgp.txt* file in an output directory.
* config-gen-04.py - Illustrates using a CSV file stored in the input directory named *bgp.csv* to create multiple configurations and outputing the content to multiple text files based on the IP address of the MPLS interface and stored in the output directory.

Thank you to Stuart Clark, the foundation of the Jinja2 content comes from his blog post on cisco.com.

[Render your first network configuration template using Python and Jinja2](https://blogs.cisco.com/developer/network-configuration-template)
