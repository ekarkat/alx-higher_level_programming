#!/usr/bin/python3
"""model n 0"""
from urllib import request, error, response, parse, robotparser
from sys import argv

if __name__ == "__main__":
    req = request.Request(argv[1])

    try:
        with request.urlopen(req) as response:
            html = response.read()
            print(html.decode("UTF-8"))
    except error.URLError as e:
        print("Error code: {}".format(e.code))
