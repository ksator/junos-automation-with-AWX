## Documentation structure
[**About AWX**](README.md#about-awx)  
[**About this repo**](README.md#about-this-repo)  
[**How to use this repo**](README.md#how-to-use-this-repo)    
[**install AWX**](README.md#install-awx)  
[**install the requirements to use Ansible modules for Junos**](README.md#install-the-requirements-to-use-ansible-modules-for-junos)  
[**install the requirements to use the python scripts hosted in this repository**](README.md#install-the-requirements-to-use-the-python-scripts-hosted-in-this-repository)   
[**clone this repository**](README.md#clone-this-repository)  
[**edit the file variables.yml**](README.md#edit-the-file-variablesyml)  
[**execute the script configure_awx_using_your_variables.py**](README.md#execute-the-script-configure_awx_using_your_variablespy)  
[**Looking for more Junos automation solutions**](README.md#looking-for-more-junos-automation-solutions)  

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
- This repository has automation content that consumes AWX.  You can use this repository to execute playbooks with REST calls.    
- It uses Python scripts and YAML variables. 

## How to use this repo 

The steps are:  
- install AWX
- install the requirements to use Ansible modules for Junos  
- install the requirements to use the python scripts hosted in this repository  
- clone this repository
- edit the file [**variables.yml**](variables.yml) to indicate your details such as the ip address of your AWX, the git repository that has the playbooks you want to add yo your AWX, ....
- execute the script [**configure_awx.py**](configure_awx.py): It uses the variables you defined in the file [**variables.yml**](variables.yml) to configure AWX    
- you can now consume your playbooks with AWX GUI and AWX API!
   - AWX GUI is ```http://<awx_ip_address>```    
   - You can visit the AWX REST API with a web browser: ```http://<awx_ip_address>/api/v2/``` 
   - Execute the file [**run_awx_template.py**](run_awx_template.py) to consume your playbooks from AWX REST API. 

## install AWX 

Here's the [install guide](https://github.com/ansible/awx/blob/devel/INSTALL.md)  
I am running AWX as a containerized application.  
Issue the ```docker ps``` command to see what containers are running.  
```
# docker ps
CONTAINER ID        IMAGE                     COMMAND                  CREATED             STATUS              PORTS                                NAMES
5f506acf7a9a        ansible/awx_task:latest   "/tini -- /bin/sh -c…"   2 weeks ago         Up About a minute   8052/tcp                             awx_task
89d2b50cd396        ansible/awx_web:latest    "/tini -- /bin/sh -c…"   2 weeks ago         Up About a minute   0.0.0.0:80->8052/tcp                 awx_web
6677b05c3dd8        memcached:alpine          "docker-entrypoint.s…"   2 weeks ago         Up About a minute   11211/tcp                            memcached
702d9538c538        rabbitmq:3                "docker-entrypoint.s…"   2 weeks ago         Up About a minute   4369/tcp, 5671-5672/tcp, 25672/tcp   rabbitmq
7167f4a3748e        postgres:9.6              "docker-entrypoint.s…"   2 weeks ago         Up About a minute   5432/tcp                             postgres
```
The default credentials are admin/password.  

## install the requirements to use Ansible modules for Junos  

We need to install in the awx_task container the Ansible requirements to use the Ansible modules for Junos.  

Connect to the container cli:
```
docker exec -it awx_task bash  
```

Once connected, run these commands from awx_task:
```
yum install -y pip python-devel libxml2-devel libxslt-devel gcc openssl libffi-devel python-pip  
pip install --upgrade pip
pip install junos-eznc jxmlease
ansible-galaxy install Juniper.junos,1.4.3
```

Once complete, exit out of the container.


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

The file [**variables.yml**](variables.yml) defines variables.  
Edit it to indicate details such as: 
- The IP address of your AWX   
- the git repository that has your playbooks
- the list of playbooks from your git repository you want to add to AWX
- and some additionnal details

```
vi variable.yml
```

```
$ more variables.yml 
---

# awx ip @
awx: 
 ip: 192.168.233.142

# awx organization you want to create
organization: 
 name: "Juniper"

# awx team you want to create. The below team belongs to the above organization
team:
 name: "automation"

# awx user you want to create. The below user belongs to the above team
user: 
 username: "ksator"
 first_name: "khelil"
 last_name: "sator"
 password: "AWXpassword"

# awx project you want to create. The below project belongs to the above organiza
tion
project: 
 name: "Junos automation"
 git_url: "https://github.com/ksator/lab_management.git"

# credentials for AWX to connect to junos devices. The below credentials belongs 
to the above organization
credentials: 
 name: "junos"
 username: "lab"
 password: "jnpr123"

# awx inventory you want to create. 
# indicate which file you want to use as source of the AWX inventory. 
# The below inventory belongs to the above organization
inventory: 
 name: "junos_lab"
 file: "hosts"

# awx templates you want to create. 
# indicate the list of playbooks you want to use when creating equivalent awx tem
plates. 
# The below playbook belongs to the above source 
playbooks: 
 - 'pb.check.lldp.yml'
 - 'pb.check.bgp.yml'
 - 'pb.check.interfaces.yml'
 - 'pb.check.vlans.yml'
 - 'pb.check.lldp.json.yml'
 - 'pb.configure.golden.yml'
 - 'pb.configure.telemetry.yml'
 - 'pb.rollback.yml'
 - 'pb.print.facts.yml'
 - 'pb.check.all.yml'
 - 'pb.check.ports.availability.yml'
```


## execute the script configure_awx_using_your_variables.py

The file [**configure_awx_using_your_variables.py**](configure_awx_using_your_variables.py) uses the details in the file [**variables.yml**](variables.yml) and creates: 
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

