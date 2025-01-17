#!/usr/bin/python3
"""
This Python script retrieves the status
from the URL `https://alx-intranet.hbtn.io/status`
using the `urllib` library.
It then formats and displays the response body,
including the type of the response,
the raw content,
and the UTF-8 decoded content.
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
