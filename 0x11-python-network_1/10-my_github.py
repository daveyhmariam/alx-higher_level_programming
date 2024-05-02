#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    ses = requests.Session()

    ses.auth = (sys.argv[1], sys.argv[2])
    res = ses.get("https://api.github.com/user")
    print(res.json().get("id"))
