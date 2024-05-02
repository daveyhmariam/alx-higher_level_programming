#!/usr/bin/python3
""" Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don't need to check arguments passed to the script (number or type)

"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    param = {"autor": argv[2], "per_page": 10}
    res = requests.get(url, params=param)
    if res.status_code == 200:
        commits = res.json()
        for commit in commits:
            sha_key = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print("{}: {}".format(sha_key, author_name))
