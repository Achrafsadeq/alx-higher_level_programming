#!/usr/bin/python3
"""
This script sends a GET request to the specified URL,
retrieves the response body, and prints:
- The type of the response body.
- The raw content of the response body.
- The UTF-8 decoded content of the response body.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
