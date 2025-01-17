#!/usr/bin/python3
"""
Python script that lists the 10 most recent commits of a repository
using the GitHub API.
Fetches the 10 most recent commits from the specified repository.
"""
import requests
import sys


def fetch_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {"per_page": 10}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        commits = response.json()

        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./100-github_commits.py <repository> <owner>")
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]
    fetch_commits(repo, owner)
