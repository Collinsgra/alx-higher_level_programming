#!/usr/bin/python3
"""takes credentials (username and password)
and uses the API to display your id """

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':

    username = sys.argv[1]
    passwd = sys.argv[2]
    response = requests.get('https://api.github.com/user\
', auth=HTTPBasicAuth(username, passwd))
    print(response.json().get('id'))
