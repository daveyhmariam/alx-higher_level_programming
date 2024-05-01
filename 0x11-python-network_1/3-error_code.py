#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
displays the body of the response
"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    url = argv[1]
    try:
        with request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except error.URLError as e:
        if hasattr(e, 'code'):
            print("Error code: {}".format(e.code))
