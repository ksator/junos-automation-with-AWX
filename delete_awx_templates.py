'''
Description: use this script to make a REST call to AWX in order to delete all AWX templates (i.e to remove all Ansible playbooks from AWX)
'''
'''
Usage: 
$ python AWX/delete_awx_templates.py 
'''

import requests
from requests.auth import HTTPBasicAuth

authuser = 'admin'
authpwd = 'password'
url = 'http://192.168.233.136/api/v2/job_templates'
my_headers = { 'Accept': 'application/json' }
rest_call_to_get_all_templates = requests.get(url, auth=HTTPBasicAuth(authuser, authpwd), headers=my_headers)

for item in rest_call_to_get_all_templates.json()['results']:
    url = 'http://192.168.233.136/api/v2/job_templates/' + str(item["id"])
    rest_call_to_delete_a_template = requests.delete(url, auth=HTTPBasicAuth(authuser, authpwd))
