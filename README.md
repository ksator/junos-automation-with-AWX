# About AWX

[**About AWX**](https://www.ansible.com/products/awx-project/faq)  
[**AWX REST API guide**](http://docs.ansible.com/ansible-tower/2.3.0/html/towerapi/index.html)  
AWX GUI: http://localhost/  
You can visit the AWX REST API in a web browser at http://localhost/api/v2/  

# About this repo  

This repo is used to configure AWX and to consume it with its REST API.  

# How to use this repo 

```
vi variable.yml
```
```
# python configure_awx_from_variables.py 
Juniper organization successfully created
automation team successfully created and added to the Juniper organization
ksator user successfully created and added to the automation team
Junos automation project successfully created and added to the Juniper organization
junos credentials successfully created and added to the Juniper organization
junos_lab inventory successfully created and added to the Juniper organ
hosts file successfully added as a source to junos_lab inventory
wait 20 seconds before to resume
pb.check.lldp.yml template successfully created
pb.check.bgp.yml template successfully created
pb.check.interfaces.yml template successfully created
pb.check.vlans.yml template successfully created
pb.check.lldp.json.yml template successfully created
pb.configure.golden.yml template successfully created
pb.configure.telemetry.yml template successfully created
pb.rollback.yml template successfully created
pb.print.facts.yml template successfully created
pb.check.all.yml template successfully created
pb.check.ports.availability.yml template successfully created
```
# Looking for more Junos automation solutions

https://github.com/ksator?tab=repositories  
https://gitlab.com/users/ksator/projects  
https://gist.github.com/ksator/  

