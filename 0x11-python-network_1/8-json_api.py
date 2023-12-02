#!/usr/bin/python3
"""model n 0"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    try:
        values = {'q': "{}".format(argv[1])}
    except IndexError:
        values = {"q": ""}
    response = requests.post(url, data=values)
    content_type = response.headers.get('Content-Type')
    # print(content_type)

    if (content_type is not None
            and 'application/json' in content_type):
        data = response.json()
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data["id"], data["name"]))
    else:
        print("Not a valid JSON")
