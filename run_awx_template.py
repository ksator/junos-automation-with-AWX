'''
Description: use this script to make a REST call to AWX in order to run an existing AWX template (i.e an Ansible playbook)
'''
'''
usage: $ python run_awx_templates.py <template_name>
'''
'''
bad example:  python run_awx_templates.py wrong_awx_template_name
there is a problem with that template
'''
'''
good example: $ python run_awx_templates.py valid_awx_template_name
waiting for the job to complete ... 
still waiting for the job to complete ...
still waiting for the job to complete ...
status is successful
'''
'''
$ python run_awx_template.py run_pb.check.bgp.yml
waiting for the job to complete ... 
still waiting for the job to complete ...
still waiting for the job to complete ...
still waiting for the job to complete ...
status is successful
'''
###################################################
# This block indicates the various imports
###################################################
import requests
from requests.auth import HTTPBasicAuth
# from pprint import pprint
import time
import sys
import json
import yaml


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



######################################################
# this block is the AWX configuration using REST calls
######################################################

my_variables_in_yaml=import_variables_from_file()

authuser = my_variables_in_yaml['user']['username']
authpwd = my_variables_in_yaml['user']['password']

'''
authuser = 'admin'
authpwd = 'password'
'''

payload = {
    "limit": "",
    "verbosity": 0
}
'''
payload = {}
'''
'''
payload = {
   "limit": "QFX10K2-174",
   "verbosity": 3,
   "extra_vars": {
      "rbid": 1
   }
}
'''
template_name = sys.argv[1]
headers = { 'content-type' : 'application/json' }
url = 'http://' + my_variables_in_yaml['awx']['ip'] + '/api/v2/job_templates/' + template_name + '/launch/'
rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))

# print 'rest call http response code is ' + str(rest_call.status_code)
# expected value for rest_call.status_code is 201
if rest_call.status_code !=201: 
  print "there is a problem with that template"
  sys.exit()

print "waiting for the job to complete ... "
time.sleep(15)

# print 'job that have the details for the previous rest call is ' + str(rest_call.json()['job'])
# rest call to get the status of the previous template execution
url='http://' + my_variables_in_yaml['awx']['ip'] + '/api/v2/jobs/' + str(rest_call.json()["job"])
headers = { 'Accept' : 'application/json' }
status=requests.get(url, auth=(authuser, authpwd), headers=headers)

# waiting for the job to complete, and then print the job status
while status.json()["status"] not in ["successful","failed"]:
  print "still waiting for the job to complete ..."
  time.sleep(15)
  status=requests.get(url, auth=(authuser, authpwd), headers=headers)
print "status is " + status.json()["status"]

