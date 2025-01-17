#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
using the requests package.
This script sends a GET request to the specified URL
and displays the body of the response.
"""

import requests


if __name__ == "__main__":
    # Send a GET request to the specified URL
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
