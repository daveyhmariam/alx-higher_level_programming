#!/usr/bin/python3
"""takes in a URL, sends a request to the URL 
displays the body of the response
"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    try:
        url = argv[1]
        with request.urlopen(url) as res:
            pass
    except error.URLError as e:
        if hasattr(e, 'code'):
            print("Error code: {}".format(e.code))
