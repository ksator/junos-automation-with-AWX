# AWX REST API

[**About AWX**](https://www.ansible.com/products/awx-project/faq)  
[**AWX REST API guide**](http://docs.ansible.com/ansible-tower/2.3.0/html/towerapi/index.html)  

The python scripts [**configure_awx_templates.py**](AWX/configure_awx_templates.py) make a REST call to AWX in order to create AWX templates (i.e to add your Ansible playbooks to AWX)  
Usage: 
```
$ python configure_awx_templates.py 
run_pb.check.lldp.yml template has been created
run_pb.check.bgp.yml template has been created
run_pb.check.interfaces.yml template has been created
run_pb.check.vlans.yml template has been created
run_pb.check.lldp.json.yml template has been created
```

The python scripts [**run_awx_templates.py**](AWX/run_awx_templates.py) uses the AWX REST API to execute an AWX template (i.e an Ansible playbook) and to print the status.  

Usage:
``` 
$ python run_awx_templates.py <template_name>
```
Example: 
```
$ python AWX/run_awx_templates.py wrong_name
there is a problem with that template
```
Example: 
```
$ python run_awx_templates.py valid_name
waiting for the job to complete ... 
still waiting for the job to complete ...
still waiting for the job to complete ...
status is successful
```


The python scripts [**delete_awx_template.py**](AWX/delete_awx_template.py) make a REST call to AWX in order to delete an AWX template (i.e to remove an Ansible playbook from AWX)  
Usage: 
```
$ python delete_awx_templates.py 
```

The python scripts [**delete_awx_templates.py**](AWX/delete_awx_templates.py) makes REST calls to AWX in order to delete all AWX templates (i.e to remove all Ansible playbook from AWX)  
Usage: 
```
$ python delete_awx_templates.py 
```


# Looking for more Junos automation solutions

https://github.com/ksator?tab=repositories  
https://gitlab.com/users/ksator/projects  
https://gist.github.com/ksator/  

