# this script makes a rest call to create an AWX user
# usage: python create_user.py

import requests
from requests.auth import HTTPBasicAuth
import json

# this is the default AWX user
authuser = 'admin'
authpwd = 'password'
headers = { 'content-type' : 'application/json' }
payload = {
    "username": "ksator",
    "first_name": "khelil",
    "last_name": "sator",
    "is_superuser": True,
    "password": "AWXpassword"
}
url = 'http://192.168.233.136/api/v2/users/'

rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))

if rest_call.status_code == 201:
     print 'user ksator successfully created'
else: 
     print 'failed to create the user ksator'





