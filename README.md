# Repository documentation structure

- [**What to find in this repository**](README.md#what-to-find-in-this-repository)
- [**About REST API**](README.md#about-rest-api)
- [**REST calls with Python**](README.md#rest-calls-with-python)
- [**REST calls with Ansible**](README.md#rest-calls-with-ansible)
- [**How to get locally the content of the remote repository**](README.md#how-to-get-locally-the-content-of-the-remote-repository)
- [**JUNOS REST API**](README.md#junos-rest-api)
    - [**junos REST API guide**](README.md#junos-rest-api-guide)
    - [**how to get the equivalent RPC of a junos show command**](README.md#how-to-get-the-equivalent-rpc-of-a-junos-show-command)
    - [**how to enable REST API on Junos**](README.md#how-to-enable-rest-api-on-junos)
    - [**how to use Junos REST API explorer**](README.md#how-to-use-the-junos-rest-api-explorer)
    - [**how to make REST calls with curl**](README.md#how-to-make-rest-calls-with-curl)
    - [**how to make REST calls with python**](README.md#how-to-make-rest-calls-with-python)
    - [**how to make REST calls with ansible**](README.md#how-to-make-rest-calls-with-ansible)
- [**AWX REST API**](README.md#awx-rest-api)
- [**Looking for more Junos automation solutions**](README.md#looking-for-more-junos-automation-solutions)

# What to find in this repository

This repository has basic REST calls examples for Junos. 

# About REST API

Junos, Junos space, Contrail, Northstar, ... have REST API.  
You first need to get the REST API documentation for your system.   
Then you can use a graphical REST Client (REST Easy, RESTClient, Postman, ...) to start playing with REST APIs and learn more about REST APIs.  

Graphical REST clients are for humans, so if you need automation and programmatic access, you have to use other sorts of REST clients. You can then use Python as a REST Client to handle REST Calls.  

# REST calls with Python

We can use Python librairies to make REST calls. I am using the library requests.  

Example: google map has a public API (read only). The python script [**google_map_api.py**](google_map/google_map_api.py) prompts you for an address, and then uses the google map API to get data with a JSON representation for that address, and then parses the JSON output and prints the address latitude and longitude. Run this command to use it:  
```
$ python google_map_api.py
which address: 41 rue de villiers neuilly sur seine
latitude is 48.8890315
longitude is 2.2806278
```

# REST calls with Ansible 

We can use Ansible to make rest calls. I am using the module [**uri**](http://docs.ansible.com/ansible/latest/uri_module.html). 


# How to get the content of the remote repository locally

```
sudo -s
git clone https://github.com/ksator/rest_calls_to_junos.git
cd rest_calls_to_junos/
ls
```
You can now use the local copy of this remote repository.  

# JUNOS REST API

You can use HTTP get and post methods to submit RPCs to the REST Server.  
You can retrieve data in XML or JSON.  
REST configuration is under “system services” (default port is 3000)  
REST Explorer is an optional tool (GUI) for testing  

### Junos REST API guide
it is located [**here**](https://www.juniper.net/documentation/en_US/junos/information-products/pathway-pages/rest-api/rest-api.pdf) 

### How to get the equivalent RPC of a Junos show command?

Each Junos show command has an equivalent RPC.   
To get the equivalent RPC of a Junos show command, add ```| display xml rpc``` at the end of the show command.  

##### show command/RPC without argument

Run this command to get the equivalent rpc of ```show version``` (which is ```get-software-information```):
```
lab@spine-03> show version | display xml rpc
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/17.3R1/junos">
    <rpc>
        <get-software-information>
        </get-software-information>
    </rpc>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>
```

##### show command/RPC with arguments

Some show commands use arguments, so the equivalent rpc require arguments:  
Run this command to get the equivalent rpc of ```show chassis hardware clei-models | display xml```. There is one argument in the rpc.
```
pytraining@mx80-17> show chassis hardware clei-models | display xml rpc 
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/17.2R1/junos">
    <rpc>
        <get-chassis-inventory>
                <clei-models/>
        </get-chassis-inventory>
    </rpc>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>
```

Run this command to get the equivalent rpc for ```show route receive-protocol bgp 192.168.10.4 active-path hidden | display xml```. There are several arguments in the rpc.
```
pytraining@newhostname> show route receive-protocol bgp 192.168.10.4 active-path hidden | display xml rpc    
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/12.3R11/junos">
    <rpc>
        <get-route-information>
                <active-path/>
                <bgp/>
                <peer>192.168.10.4</peer>
                <hidden/>
        </get-route-information>
         </rpc>
        <cli>
            <banner>{master:0}</banner>
        </cli>
    </rpc-reply>
```

### How to enable REST API on Junos

Run these commands to enable REST API on Junos. The default port is 3000.  
The below commands also enable a graphical REST API Explorer that allows to conveniently experiment with REST APIs.  
```
lab@dc-vmx-3> show configuration system services rest | display set
set system services rest http
set system services rest enable-explorer
```

### How to use the Junos REST API explorer

Junos REST API explorer is an optional graphical tool for testing Junos REST API. It is embeded in Junos, and allows to conveniently experiment with REST APIs.

##### Junos REST API explorer usage: one single RPC, no argument
Here's how to use the Junos REST API explorer to make a REST call to get Junos data in XML. This example uses an HTTP GET. The RPC is ```get-software-information```. There is no argument in the RPC. This is the equivalent of ```show version | display xml```. The default port is 3000, but I am using 8080 in this example.     
![rest call get software information.png](explorer/rest_call_get-software-information.png)  

##### Junos REST API explorer usage: RPC with arguments
Here's how to use the Junos REST API explorer to make a REST call when there are arguments in the RPC. This is the equivalent of ```show version brief | display xml```. The RPC is ```get-software-information``` and the RPC argument is ```<brief/>```.
```
lab@jedi-vmx-2-vcp> show version brief | display xml rpc
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/17.2R1/junos">
    <rpc>
        <get-software-information>
                <brief/>
        </get-software-information>
    </rpc>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>
```
In that case, we use an HTTP POST, despite it only being to read data. The default port is 3000, but I am using 8080 in this example.     
![rest_call_with_arguments.png](explorer/rest_call_with_args.png)

##### Junos REST API explorer usage: several RPC
Here's how to use the Junos REST API explorer to make a REST call with several RPC. In this case, we use an HTTP POST, despite it is only to read data. The default port is 3000, but I am using 8080 in this example.       
![rest_call_with_several rpc.png](explorer/rest_call_with_several_rpc.png)  

##### Junos REST API explorer usage: RPC with filters
Here's how to use the Junos REST API explorer to make a REST call with filters to get Junos data. This example uses an HTTP POST. This is the equivalent of ``` show configuration interfaces ge-0/0/0 | display xml```. The default port is 3000, but I am using 8080 in this example.     
![rest_call_with_filter.png](explorer/rest_call_with_filter.png)


### How to make REST calls with curl

curl is an open source command line tool for transferring data.  

##### curl usage with: one single RPC, no argument

Run this command to retrieve and print the software information in a XML representation from a vMX router with a REST call. It's an HTTP GET. The rpc ```get-software-information``` is the equivalent of ```show version```. 
```
$ curl http://172.30.52.152:8080/rpc/get-software-information -u "lab:m0naco" -H "Content-Type: application/xml" -H "Accept: application/xml"
```

Run this command to retrieve and print the software information in a JSON representation from an vMX router with a REST call. It's an HTTP GET. The rpc ```get-software-information``` is the equivalent of ```show version```
```
$ curl http://172.30.52.152:8080/rpc/get-software-information -u "lab:m0naco" -H "Content-Type: application/xml" -H "Accept: application/json"
```

##### curl usage with: RPC with arguments

Run this command to retrieve and print the software information in a XML representation from an vMX router with a REST call. This is the equivalent of ```show version brief | display xml```. The RPC is ```get-software-information``` and the RPC argument is ```<brief/>```.  It's an HTTP POST. 
```
$ curl http://172.30.52.152:8080/rpc/get-software-information -u "lab:m0naco" -H "Content-Type: application/xml" -H "Accept: application/xml" -d "<brief/>"
```
##### curl usage with: several RPC

Run this command to make a REST call with several RPC. In this case, we use an HTTP POST, despite it only being to read data. The list of RPC is ```get-bgp-neighbor-information``` and ```get-software-information```. The default port is 3000, but I am using 8080 in this example.  
```
$ curl http://172.30.52.152:8080/rpc?stop-on-error=1 -u "lab:m0naco" -H "Content-Type: plain/text" -H "Accept: application/xml" -d "<get-bgp-neighbor-information/> <get-software-information/>"
```

##### curl usage with: RPC with a filter

Run this command to retrieve a subset of the junos configuration in a XML representation from an vMX router with a REST call with a filter. It's the equivalent of ```show configuration interfaces ge-0/0/0 | display xml```.  It's an HTTP POST. 
```
$ curl http://172.30.52.152:8080/rpc/ -u "lab:m0naco" -H "Content-Type: application/xml" -H "Accept: application/xml" -d "<get-config><source><running/></source><filter type="subtree"><configuration><interfaces><interface><name>ge-0/0/0</name></interface></interfaces></configuration></filter></get-config> "
```

### How to make REST calls with Python 

We can use Python librairies to make REST calls. I am using the library requests.  

[**get_software_information_in_xml.py**](junos/get_software_information_in_xml.py) retrieves and prints the software information in a XML representation from an vMX router with a REST call. It uses the HTTP method GET, with the RPC ```get-software-information``` and no argument. 
```
$ python junos/get_software_information_in_xml.py
```

[**get_software_information_in_json.py**](junos/get_software_information_in_json.py) script retrieves in a JSON representation the software information from an MX router with a REST API call. It uses the HTTP method GET with the RPC ```get-software-information``` and no argument. The JSON response is parsed and some details are printed. 
```
$ python junos/get_software_information_in_json.py 
Software version: 17.4R1.16
Host-name: dc-vmx-3
Product name: vmx
```

[**get_configuration_with_filter.py**](junos/get_configuration_with_filter.py) script retrieves and print a subset of the Junos configuration from an MX router with a REST API call. It uses a filter to retrieve only a subset of the Junos configuration. It uses the HTTP method POST. 
```
$ python junos/get_configuration_with_filter.py
```

[**configure.py**](junos/configure.py) script configures a Junos device using a REST API call. It uses the HTTP method POST. It does these operations: lock-configuration, load-configuration, commit and unlock-configuration, and returns an HTTP response code. 

```
$ python junos/configure.py 
200
```
```
lab@dc-vmx-3> show system commit 
0   2018-01-16 10:01:11 UTC by lab via junoscript
```
```                                        
lab@dc-vmx-3> show configuration | compare rollback 1 
[edit system login]
+   message "welcome to REST demo";
```

[**audit_bgp.py**](junos/audit_bgp.py) script audits a list of devices using a REST API call. It uses the HTTP method GET to retrieve some BGP details in JSON. It uses the RPC ```get-bgp-neighbor-information```. It then parses the JSON output and prints the peers state.  
```
$ python junos/audit_bgp.py
**************************************************
auditing bgp peers state for device 172.30.52.152
session state for peer 192.168.1.2+63127 is Established
**************************************************
auditing bgp peers state for device 172.30.52.153
session state for peer 192.168.1.1+179 is Established
```

### How to make REST calls with Ansible

The ansible inventory file is [**hosts**](hosts) at the root of the repository.  
The ansible configuration file is [**ansible.cfg**](ansible.cfg) at the root of the repository.  
Devices credentials are in a yaml file in the [**group_vars**](group_vars) directory  
These playbooks have been tested using Ansible 2.4.2.0  

The playbook [**pb_rest_call.yml**](junos/pb_rest_call.yml) makes rest call to Junos devices and saves the rpc output [**locally**](junos). It also parses the rpc output and prints some details.  


```
$ ansible-playbook junos/pb_rest_call.yml

PLAY [make rest call to Junos devices, save and parse output] *************************************************************************************

TASK [check if some ports are reachable on Junos devices] *************************************************************************************
ok: [dc-vmx-3] => (item=22)
ok: [dc-vmx-4] => (item=22)
ok: [dc-vmx-3] => (item=830)
ok: [dc-vmx-4] => (item=830)
ok: [dc-vmx-4] => (item=8080)
ok: [dc-vmx-3] => (item=8080)

TASK [create device directories] **************************************************************************************************************
changed: [dc-vmx-3 -> localhost]
changed: [dc-vmx-4 -> localhost]

TASK [make rest call to vmx devices] **********************************************************************************************************
changed: [dc-vmx-3 -> localhost]
changed: [dc-vmx-4 -> localhost]

TASK [Print some mx details] ******************************************************************************************************************
ok: [dc-vmx-3] => {
    "msg": "device dc-vmx-3 runs version 17.4R1.16"
}
ok: [dc-vmx-4] => {
    "msg": "device dc-vmx-4 runs version 17.4R1.16"
}

PLAY RECAP ************************************************************************************************************************************
dc-vmx-3                   : ok=4    changed=2    unreachable=0    failed=0
dc-vmx-4                   : ok=4    changed=2    unreachable=0    failed=0
```
```
$  ls junos
dc-vmx-3  dc-vmx-4  pb_rest_call.yml
```
```
$  ls junos/dc-vmx-3/
rpc_output.json

```

The playbook [**pb_rest_calls.yml**](junos/pb_rest_calls.yml) makes several rest calls to several Junos devices and saves the rpc output [**locally**](junos). 
```
$ ansible-playbook junos/pb_rest_calls.yml 

PLAY [make rest calls to junos devices] **********************************************************************************************************************************

TASK [check if some ports are reachable on Junos devices] ****************************************************************************************************************
ok: [dc-vmx-4] => (item=22)
ok: [dc-vmx-3] => (item=22)
ok: [dc-vmx-4] => (item=830)
ok: [dc-vmx-3] => (item=830)
ok: [dc-vmx-4] => (item=8080)
ok: [dc-vmx-3] => (item=8080)

TASK [create device directories] *****************************************************************************************************************************************
ok: [dc-vmx-4 -> localhost]
ok: [dc-vmx-3 -> localhost]

TASK [make rest call to vmx devices] *************************************************************************************************************************************
changed: [dc-vmx-3 -> localhost] => (item=get-software-information)
changed: [dc-vmx-4 -> localhost] => (item=get-software-information)
changed: [dc-vmx-3 -> localhost] => (item=get-bgp-neighbor-information)
changed: [dc-vmx-4 -> localhost] => (item=get-bgp-neighbor-information)

PLAY RECAP ***************************************************************************************************************************************************************
dc-vmx-3                   : ok=3    changed=1    unreachable=0    failed=0   
dc-vmx-4                   : ok=3    changed=1    unreachable=0    failed=0   
```
```
$ ls junos/dc-vmx-3/
get-bgp-neighbor-information_output.json  get-software-information_output.json  rpc_output.json
```


# AWX REST API

[**About AWX**](https://www.ansible.com/products/awx-project/faq)  
[**AWX REST API guide**](http://docs.ansible.com/ansible-tower/2.3.0/html/towerapi/index.html)  

The python scripts [**configure_awx_templates.py**](AWX/configure_awx_templates.py) make a REST call to AWX in order to create AWX templates (i.e to add your Ansible playbooks to AWX)  
Usage: 
```
$ python AWX/configure_awx_templates.py 
run_pb.check.lldp.yml template has been created
run_pb.check.bgp.yml template has been created
run_pb.check.interfaces.yml template has been created
run_pb.check.vlans.yml template has been created
run_pb.check.lldp.json.yml template has been created
```

The python scripts [**run_awx_templates.py**](AWX/run_awx_templates.py) uses the AWX REST API to execute an AWX template (i.e an Ansible playbook) and to print the status.  

Usage:
``` 
$ python AWX/run_awx_templates.py <template_name>
```
Example: 
```
$ python AWX/run_awx_templates.py wrong_name
there is a problem with that template
```
Example: 
```
$ python AWX/run_awx_templates.py valid_name
waiting for the job to complete ... 
still waiting for the job to complete ...
still waiting for the job to complete ...
status is successful
```


The python scripts [**delete_awx_template.py**](AWX/delete_awx_template.py) make a REST call to AWX in order to delete an AWX template (i.e to remove an Ansible playbook from AWX)  
Usage: 
```
$ python AWX/delete_awx_templates.py 
```

The python scripts [**delete_awx_templates.py**](AWX/delete_awx_templates.py) makes REST calls to AWX in order to delete all AWX templates (i.e to remove all Ansible playbook from AWX)  
Usage: 
```
$ python AWX/delete_awx_templates.py 
```


# Looking for more Junos automation solutions

https://github.com/ksator?tab=repositories  
https://gitlab.com/users/ksator/projects  
https://gist.github.com/ksator/  

