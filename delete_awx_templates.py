'''
Description: use this script to make a REST call to AWX in order to delete all AWX templates (i.e to remove all Ansible playbooks from AWX)
'''
'''
Usage: $ python delete_awx_templates.py 
'''

import requests
from requests.auth import HTTPBasicAuth
import yaml 

def import_variables_from_file():
 my_variables_file=open('variables.yml', 'r')
 my_variables_in_string=my_variables_file.read()
 # print my_variables_in_string
 my_variables_in_yaml=yaml.load(my_variables_in_string)
 # print my_variables_in_yaml
 # print my_variables_in_yaml['awx']['ip']
 my_variables_file.close()
 return my_variables_in_yaml

my_variables_in_yaml=import_variables_from_file()


# authuser = my_variables_in_yaml['user']['username']
# authpwd = my_variables_in_yaml['user']['password']
authuser = 'admin'
authpwd = 'password'

my_headers = { 'Accept': 'application/json' }
url = 'http://' + my_variables_in_yaml['awx']['ip'] + '/api/v2/job_templates'
rest_call_to_get_all_templates = requests.get(url, auth=HTTPBasicAuth(authuser, authpwd), headers=my_headers)
for item in rest_call_to_get_all_templates.json()['results']:
    url = 'http://' + my_variables_in_yaml['awx']['ip'] + '/api/v2/job_templates/' + str(item["id"])
    rest_call_to_delete_a_template = requests.delete(url, auth=HTTPBasicAuth(authuser, authpwd))


