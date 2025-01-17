#!/usr/bin/python3
"""
Python script that takes a URL, sends a request,
and displays the value of the X-Request-Id header.

This script sends a GET request to the specified URL and retrieves.
"""
import requests
import sys

if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
