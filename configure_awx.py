###################################################
# This script takes the variables defined in the file variables.yml and make rest calls to AWX to configure it.
###################################################
###################################################
# usage: python configure_awx.py
###################################################
###################################################
# This block indicates the various imports
###################################################
import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint
import yaml
import time


##################################################
# This block defines the functions we will use
###################################################
def import_variables_from_file():
 my_variables_file=open('variables.yml', 'r')
 my_variables_in_string=my_variables_file.read()
 # print my_variables_in_string
 my_variables_in_yaml=yaml.load(my_variables_in_string)
 # print my_variables_in_yaml
 # print my_variables_in_yaml['awx']['ip']
 my_variables_file.close()
 return my_variables_in_yaml


def create_the_organization():
 url=url_base + '/api/v2/organizations/'
 payload = {
     "name": my_variables_in_yaml['organization']['name']
 }
 rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
 # pprint (rest_call.json())
 if rest_call.status_code == 201:
      print my_variables_in_yaml['organization']['name'] + ' organization successfully created'
 else:
      print 'failed to create the organization ' + my_variables_in_yaml['organization']['name']


def get_the_id_of_the_organization(): 
 url = url_base + "/api/v2/organizations/"
 rest_call = requests.get(url, headers=headers, auth=(authuser, authpwd))
 # pprint (rest_call.json())
 for item in rest_call.json()['results']:
  if item['name'] == my_variables_in_yaml['organization']['name']:
 #  print my_variables_in_yaml['organization']['name'] + " organization id is " + str(item['id'])
   organization_id = str(item['id'])
   return organization_id


def create_the_team(): 
 url = url_base + '/api/v2/organizations/' + organization_id + '/teams/'
 payload = {
     "name": my_variables_in_yaml['team']['name'],
     "organization": organization_id
 }
 rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
 # pprint (rest_call.json())
 if rest_call.status_code == 201:
      print my_variables_in_yaml['team']['name'] + ' team successfully created and added to the ' + my_variables_in_yaml['organization']['name'] + ' organization' 
 else:
      print 'failed to create the team ' + my_variables_in_yaml['team']['name'] + ' in the organization ' + my_variables_in_yaml['organization']['name']   


def get_the_team_id(): 
 url = url_base + "/api/v2/teams/"
 rest_call = requests.get(url, headers=headers, auth=(authuser, authpwd))
 # pprint (rest_call.json())
 for item in rest_call.json()['results']:
  if item['name'] == my_variables_in_yaml['team']['name']:
 #  print "team id is " + str(item['id'])
   team_id = str(item['id'])
  return team_id


def add_the_user_to_the_team(): 
 url = url_base + '/api/v2/teams/' + team_id + '/users/'
 payload = {
     "username": my_variables_in_yaml['user']['username'],
     "first_name": my_variables_in_yaml['user']['first_name'],
     "last_name": my_variables_in_yaml['user']['last_name'],
     "is_superuser": True,
     "password": my_variables_in_yaml['user']['password']
 }
 rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
 # pprint (rest_call.json())
 if rest_call.status_code == 201:
      print my_variables_in_yaml['user']['username'] + ' user successfully created and added to the ' + my_variables_in_yaml['team']['name'] + ' team'
 else:
      print 'failed to create the user ' + my_variables_in_yaml['user']['username'] + ' in the team ' + my_variables_in_yaml['team']['name']



def add_the_user_to_the_organization():
 url = url_base + '/api/v2/organizations/' + organization_id + '/users/'
 payload = {
     "username": my_variables_in_yaml['user']['username'],
     "first_name": my_variables_in_yaml['user']['first_name'],
     "last_name": my_variables_in_yaml['user']['last_name'],
     "is_superuser": True,
     "password": my_variables_in_yaml['user']['password']
 }
 rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
 # pprint (rest_call.json())
 if rest_call.status_code == 201:
      print my_variables_in_yaml['user']['username'] + ' user successfully created and added to the ' + my_variables_in_yaml['organization']['name'] + ' organization'
 else:
      print 'failed to create the user ' + my_variables_in_yaml['user']['username'] + ' in the organization ' + my_variables_in_yaml['organization']['name']


def add_the_project_to_the_organization(): 
 url = url_base + '/api/v2/projects/'
 payload = {
     "name": my_variables_in_yaml['project']['name'],
     "scm_type": "git",
     "scm_url": my_variables_in_yaml['project']['git_url'],
     "scm_branch": "", 
     "scm_clean": True,
     "scm_delete_on_update": True,
     "organization": int(organization_id),
     "scm_update_on_launch": False
 }
 rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
 # pprint (rest_call.json())
 if rest_call.status_code == 201:
      print my_variables_in_yaml['project']['name'] + ' project successfully created and added to the ' + my_variables_in_yaml['organization']['name'] + ' organization'
 else:
      print 'failed to create the project ' + my_variables_in_yaml['project']['name'] + ' in the organization ' + my_variables_in_yaml['organization']['name']


def get_the_project_id(): 
 url = url_base + "/api/v2/projects/"
 rest_call = requests.get(url, headers=headers, auth=(authuser, authpwd))
 # pprint (rest_call.json())
 for item in rest_call.json()['results']:
  if item['name'] == my_variables_in_yaml['project']['name']:
 #  print "Project id is " + str(item['id'])
   project_id = str(item['id'])
 return project_id


def add_credentials(): 
 url = url_base + '/api/v2/credentials/'
 payload = {
    "name": my_variables_in_yaml['credentials']['name'],
    "organization": organization_id,
    "credential_type": 1,
    "inputs": {
       "username": my_variables_in_yaml['credentials']['username'],
       "password": my_variables_in_yaml['credentials']['password']
    }
 }
 rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
 # pprint (rest_call.json())
 if rest_call.status_code == 201:
      print my_variables_in_yaml['credentials']['name'] + ' credentials successfully created and added to the ' + my_variables_in_yaml['organization']['name'] + ' organization'
 else:
      print 'failed to create the credentials ' + my_variables_in_yaml['credentials']['name'] + ' in the organization ' + my_variables_in_yaml['organization']['name']

def get_the_credential_id(): 
 url = url_base + "/api/v2/credentials/"
 rest_call = requests.get(url, headers=headers, auth=(authuser, authpwd))
 # pprint (rest_call.json())
 for item in rest_call.json()['results']:
  if item['name'] == my_variables_in_yaml['credentials']['name']:
 #  print "inventory id is " + str(item['id'])
   credential_id = str(item['id'])
 return credential_id

def add_inventory():
 url = url_base + '/api/v2/inventories/'
 payload = {
    "name": my_variables_in_yaml['inventory']['name'],
    "organization": organization_id,
     "has_inventory_sources": True
}
 rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
 # pprint (rest_call.json())
 if rest_call.status_code == 201:
      print my_variables_in_yaml['inventory']['name'] + ' inventory successfully created and added to the ' + my_variables_in_yaml['organization']['name'] + ' organization'
 else:
      print 'failed to create the inventory ' + my_variables_in_yaml['credentials']['name'] + ' in the organization ' + my_variables_in_yaml['organization']['name']


def get_the_inventory_id(): 
 url = url_base + "/api/v2/inventories/"
 rest_call = requests.get(url, headers=headers, auth=(authuser, authpwd))
 # pprint (rest_call.json())
 for item in rest_call.json()['results']:
  if item['name'] == my_variables_in_yaml['inventory']['name']:
 #  print "inventory id is " + str(item['id'])
   inventory_id = str(item['id'])
 return inventory_id


def add_inventory_source():
 url = url_base + '/api/v2/inventories/' + inventory_id + '/inventory_sources/'
 payload = {
   "source_path": my_variables_in_yaml['inventory']['file'],
   "source_project": project_id,
   "name": "inventory_source",
   "overwrite_vars": True,
   "update_on_launch": True,
   "source": "scm"
}
 rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
 # pprint (rest_call.json())
 if rest_call.status_code == 201:
      print my_variables_in_yaml['inventory']['file'] + ' file successfully added as a source to ' + my_variables_in_yaml['inventory']['name'] + ' inventory'
 else:
      print 'failed to add the file ' + my_variables_in_yaml['inventory']['name'] + ' as a source of the inventory ' + my_variables_in_yaml['inventory']['name']


def add_templates():
 url = url_base + '/api/v2/job_templates/'
 for item in my_variables_in_yaml['playbooks']:
  time.sleep(1)
  payload = {
   'name': "run_" + item,
   'description': "template to execute " + item + " playbook",
   'job_type': 'run',
   'inventory': inventory_id,
   'project': project_id,
   'playbook': item,
   'credential': credential_id,
   'verbosity': 0,
   "extra_vars": '',
   "skip_tags": '',
   "start_at_task": '',
   "ask_limit_on_launch": True,
   "ask_variables_on_launch": False,
   "ask_verbosity_on_launch": True
 }
  rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
  # pprint (rest_call.json())
  if rest_call.status_code == 201:
    print 'run_' + item + ' template successfully created ' + 'using the playbook ' + item  
  else:
    print 'failed to create the template run_' + item  + ' using the playbook ' + item
 

######################################################
# this block is the AWX configuration using REST calls
######################################################
my_variables_in_yaml=import_variables_from_file()
# this is the default AWX user
authuser = 'admin'
authpwd = 'password'
headers = { 'content-type' : 'application/json' }
url_base = 'http://' + my_variables_in_yaml['awx']['ip']
# print url_base
create_the_organization()
time.sleep(2)
organization_id = get_the_id_of_the_organization()
time.sleep(2)
create_the_team()
time.sleep(2)
team_id = get_the_team_id()
time.sleep(2)
add_the_user_to_the_organization()
# add_the_user_to_the_team()
time.sleep(2)
add_the_project_to_the_organization()
time.sleep(2)
project_id = get_the_project_id()
time.sleep(2)
add_credentials()
time.sleep(2)
credential_id = get_the_credential_id()
time.sleep(2)
add_inventory()
time.sleep(2)
inventory_id = get_the_inventory_id()
time.sleep(2)
add_inventory_source()
print 'wait 30 seconds before to resume'
time.sleep(30)
add_templates()






