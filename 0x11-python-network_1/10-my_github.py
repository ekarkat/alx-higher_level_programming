#!/usr/bin/python3
"""model n 0"""
from sys import argv
import requests

if __name__ == "__main__":
    user = argv[1]
    token = argv[2]
    url = "https://api.github.com/users/{}".format(user)
    headers = {"Authorization": "token {}".format(argv[2])}
    try:
        response = requests.get(url, headers=headers)
        user_data = response.json()
        print(user_data.get('id'))
    except requests.RequestException as e:
        print("None")
