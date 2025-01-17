#!/usr/bin/python3
"""
Python script to send a POST request with an email parameter to a specified URL
and display the response body.
The script uses the `requests` library to handle the HTTP POST request
and prints the server's response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    # Prepare the email data for the POST request
    data = {"email": email}
    response = requests.post(url, data=data)
    print(response.text)
