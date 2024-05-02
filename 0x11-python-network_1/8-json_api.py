#!/usr/bin/python3
"""A script tha:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    payload = "" if len(sys.argv) == 1 else {"q": sys.argv[1]}
    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url, data=payload)
    try:
        if res.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.json().get("id"),
                                   res.json().get("name")))
    except ValueError:
        print("Not a valid JSON")
