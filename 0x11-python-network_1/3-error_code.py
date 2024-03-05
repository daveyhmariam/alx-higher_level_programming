#!/usr/bin/python3
"""takes in a URL, sends a request to the URL 
displays the body of the response
"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    try:
        with request.urlopen(argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
