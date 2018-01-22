'''
Description: use this script to make a REST call to AWX in order to create AWX templates (i.e to add your Ansible playbooks to AWX)
'''
'''
Usage: 
$ python AWX/configure_awx_templates.py 
run_pb.check.lldp.yml template has been created
run_pb.check.bgp.yml template has been created
run_pb.check.interfaces.yml template has been created
run_pb.check.vlans.yml template has been created
run_pb.check.lldp.json.yml template has been created
run_pb.configure.golden.yml template has been created
run_pb.configure.telemetry.yml template has been created
run_pb.rollback.yml template has been created
run_pb.print.facts.yml template has been created
run_pb.check.all.yml template has been created
run_pb.check.ports.availability.yml template has been created
'''

import requests
from requests.auth import HTTPBasicAuth
import time
import sys
import json

authuser = 'admin'
authpwd = 'password'
headers = { 'content-type' : 'application/json' }
url = 'http://192.168.233.136/api/v2/job_templates/'

playbook_list = ['pb.check.lldp.yml', 'pb.check.bgp.yml', 'pb.check.interfaces.yml', 'pb.check.vlans.yml', 'pb.check.lldp.json.yml',  'pb.configure.golden.yml', 'pb.configure.telemetry.yml', 'pb.rollback.yml', 'pb.print.facts.yml', 'pb.check.all.yml', 'pb.check.ports.availability.yml']

for item in playbook_list: 
 payload = {
     'name': "run_" + item, 
     'description': "template to execute " + item + " playbook", 
     'job_type': 'run', 
     'inventory': 2, 
     'project': 6, 
     'playbook': item, 
     'credential': 2, 
     'verbosity': 0, 
     "extra_vars": '', 
     "skip_tags": '', 
     "start_at_task": '',
     "ask_limit_on_launch": True,
     "ask_variables_on_launch": False,
     "ask_verbosity_on_launch": True
 }
 rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
 # print rest_call.status_code
 if rest_call.status_code != 201: 
     print 'something went wrong with template for playbook ' + item
 else: 
     print 'run_' + item + ' template has been created'
 # print rest_call.json()

