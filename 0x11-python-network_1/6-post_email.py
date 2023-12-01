#!/usr/bin/python3
"""model n 0"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    values = {"email": "{}".format(argv[2])}
    response = requests.post(url, data=values)
    print("{}".format(response.text))
