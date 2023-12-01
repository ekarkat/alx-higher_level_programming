#!/usr/bin/python3
"""model n 0"""
from urllib import request, error, response, parse, robotparser
from sys import argv

if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        print((response.getheader('X-Request-Id')))
