#!/usr/bin/python3
"""model n 0"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    head = response.headers.get("X-Request-Id")
    print("{}".format(head))
