#!/usr/bin/python3
"""
Python script that sends a request to a URL
and displays the body of the response.
Handles HTTP errors and prints the error code.
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Send a request to the URL and read the response
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors and print the error code
        print(f"Error code: {e.code}")
