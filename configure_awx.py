# rest calls to AWX 

import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint

# this is the default AWX user
authuser = 'admin'
authpwd = 'password'

headers = { 'content-type' : 'application/json' }
url_base = 'http://192.168.233.142'

# create the organization Juniper
url=url_base + '/api/v2/organizations/'
payload = {
    "name": "Juniper"
}
rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
# pprint (rest_call.json())
if rest_call.status_code == 201:
     print 'organization Juniper successfully created'
else:
     print 'failed to create the organization Juniper'

# get the id of the organization Juniper
url = url_base + "/api/v2/organizations/"
rest_call = requests.get(url, headers=headers, auth=(authuser, authpwd))
# pprint (rest_call.json())
for item in rest_call.json()['results']:
 if item['name'] == 'Juniper':
#  print "Juniper organization id is " + str(item['id'])
  Juniper_id = str(item['id'])

"""
# add a user ksator to the organization Juniper

url = url_base + '/api/v2/organizations/' + Juniper_id + '/users/'
payload = {
    "username": "ksator",
    "first_name": "khelil",
    "last_name": "sator",
    "is_superuser": False,
    "password": "AWXpassword"
}
rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
pprint (rest_call.json())
if rest_call.status_code == 201:
     print 'user ksator created and added successfully to the organization Juniper'
else:
     print 'failed to create the user ksator in the organization Juniper'
"""

"""
# create the user ksator

payload = {
    "username": "ksator",
    "first_name": "khelil",
    "last_name": "sator",
    "is_superuser": True,
    "password": "AWXpassword"
}
url=url_base + '/api/v2/users/'
rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
# pprint (rest_call.json())
if rest_call.status_code == 201:
     print 'user ksator successfully created'
else:
     print 'failed to create the user ksator'
"""

"""
# get the user id for ksator

url = url_base + "/api/v2/users/"
rest_call = requests.get(url, headers=headers, auth=(authuser, authpwd))
#pprint (rest_call.json())
for item in rest_call.json()['results']:
 if item['username'] == 'ksator':
  print "ksator username id is " + str(item['id'])
"""

# create a team automation
url = url_base + '/api/v2/organizations/' + Juniper_id + '/teams/'
payload = {
    "name": "automation",
    "organization": Juniper_id
}
rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
pprint (rest_call.json())
if rest_call.status_code == 201:
     print 'team automation successfully created and added to the Juniper organization'
else:
     print 'failed to create the team automation'


# add a user ksator to the team automation
#url = url_base + '/api/v2/organizations/' + Juniper_id + '/users/'
url = url_base + '/api/v2/teams/2/users/'
payload = {
    "username": "ksator2",
    "first_name": "khelil2",
    "last_name": "sator2",
    "is_superuser": False,
    "password": "AWXpassword"
}
rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
# pprint (rest_call.json())
if rest_call.status_code == 201:
     print 'user ksator created and added successfully to the team automation'
else:
     print 'failed to create the user ksator in the team automation'

