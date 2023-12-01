#!/usr/bin/python3
"""model n 0"""
from urllib import request, error, response, parse, robotparser
from sys import argv

if __name__ == "__main__":
    values = {"email": "{}".format(argv[2])}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode())
