#!/usr/bin/python3
"""
If the HTTP status code of the response is greater than or equal to 400,
the script prints the error code. Otherwise, it prints the response text.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    # Check if the status code indicates an error (>= 400)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
