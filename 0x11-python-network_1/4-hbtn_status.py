#!/usr/bin/python3
"""requests to the URL and displays the body of the response"""
import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception

    # response body
    print("Body response:")
    print(f"    - type: {type(response.text)}")
    print(f"    - content: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
