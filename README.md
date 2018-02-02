## Documentation structure
[**About AWX**](README.md#about-this-project)  
[**About this repo**](README.md#about-this-repo)  
[**How to use this repo**](README.md#how-to-use-this-repo)  


Looking for more Junos automation solutions
## About AWX

AWX is Ansible Tower open sourced.  
You can use it if you want to consume your ansible playbooks with:
- GUI
- REST API
- users authentication and permissions. 

Here's the [**AWX FAQ**](https://www.ansible.com/products/awx-project/faq)  
Here's the [**AWX REST API guide**](http://docs.ansible.com/ansible-tower/2.3.0/html/towerapi/index.html)  

## About this repo  

- This repository has automation content that configures AWX. If you want to consume Ansible playbooks using AWX, you can use this repository to quickly add them to AWX.  
- This repository has automation content that consumes AWX (execute playbooks with REST calls).    
- It uses Python scripts and YAML variables. 

## How to use this repo 

The steps are:  
- install AWX
- install the requirements to use Ansible modules for Junos  
- install the requirements to use the python scripts hosted in this repository  
- clone this repository
- edit the file [**variables.yml**](variables.yml) to indicate your details such as the ip address of your awx, the git repository that has your playbooks, ....
- execute the script [**configure_awx_using_your_variables.py**](configure_awx_using_your_variables.py): It uses the details from the file [**variables.yml**](variables.yml) and configure AWX    
- you can now consume your playbooks with AWX GUI and AWX API!
   - AWX GUI is http://<awx_ip_address>    
   - You can visit the AWX REST API with a web browser: http://<awx_ip_address>/api/v2/ 
   - Execute the file [**run_awx_templates.py**](run_awx_templates.py) to consume your playbooks from AWX REST API. 

## install AWX 

Here's the [install guide](https://github.com/ansible/awx/blob/devel/INSTALL.md)

## install the requirements to use Ansible modules for Junos  

## install the requirements to use the python scripts hosted in this repository  
The python scripts  hosted in this repository use the library **requests** to makes REST calls to AWX.   
```
sudo -s
pip install requests
```

## clone this repository
```
sudo -s
git clone https://github.com/ksator/junos-automation-with-AWX.git
cd junos-automation-with-AWX
```

## edit the file variables.yml

The file [**variable.yml**](variable.yml) defines variables.  
Edit it to indicate details such as: 
- The IP address of your AWX   
- the git repository that has your playbooks
- the list of playbooks from your git repository you want to add to AWX
- and some additionnal details

```
more variable.yml

```

```
vi variable.yml
```


## execute the script configure_awx_using_your_variables.py

The file [**configure_awx_using_your_variables.py**](configure_awx_using_your_variables.py) uses the details in the file [**variables.yml**]variables.yml and creates: 
- An AWX organization
- An AWX team. The team belongs to the organization created above
- An AWX user. The user belongs to the team created above
- Credentials for AWX to connect to junos devices. These credentials belongs to the organization created above
- An AWX project. The project belongs to the organization created above. The project uses playbooks from a git repository.
- An AWX inventory. it belongs to the organization created above
- An equivalent AWX template for each playbook from the git repository

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



## Looking for more Junos automation solutions

https://github.com/ksator?tab=repositories  
https://gitlab.com/users/ksator/projects  
https://gist.github.com/ksator/  

