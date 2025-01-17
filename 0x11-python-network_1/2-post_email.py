#!/usr/bin/python3
"""
Python script that sends a POST request to a URL with an email
as a parameter and displays
the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    # Send the request and read the response
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        # Print the response body
        print(response_body)
