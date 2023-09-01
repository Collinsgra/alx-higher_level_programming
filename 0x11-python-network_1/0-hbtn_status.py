#!/usr/bin/python3
"""Python that fetches https://alx-intranet.hbtn.io/status"""
import urllib
from urllib import request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        status = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(status)))
        print("\t- content: {}".format(status))
        print("\t- utf8 content: {}".format(status.decode('utf-8')))
