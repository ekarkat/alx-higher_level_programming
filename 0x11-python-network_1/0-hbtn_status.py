#!/usr/bin/python3
"""model n 0"""
from urllib import request, error, response, parse, robotparser

req = request.Request("https://alx-intranet.hbtn.io/status")
with request.urlopen(req) as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format((html)))
    print("\t- utf8 content: {}".format((html.decode("UTF-8"))))
