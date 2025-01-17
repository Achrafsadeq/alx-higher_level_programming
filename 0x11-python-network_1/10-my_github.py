#!/usr/bin/python3
"""
Python script that uses the GitHub API to display your GitHub user ID.
Uses Basic Authentication with a personal access token.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


def get_github_user_id(username, token):
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, token)

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        user_data = response.json()
        print(user_data.get('id'))
    except requests.exceptions.RequestException as e:
        print(None)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    get_github_user_id(username, token)
