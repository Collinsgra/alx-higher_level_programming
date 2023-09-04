#!/usr/bin/python3
"""Sends a request to a url with response body.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    rg = requests.get(url)
    if rg.status_code >= 400:
        print("Error code: {}".format(rg.status_code))
    else:
        print(rg.text)
