#!/usr/bin/python3
"""back-end test"""
from sys import argv
import requests

if __name__ == "__main__":
    pass
    rp_nme = argv[2]
    ow_nme = argv[1]

    url = "https://api.github.com/repos/{}/{}/commits".format(ow_nme, rp_nme)
    head = {"Authorization": "token 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"}

    response = requests.get(url, headers=head)
    data = response.json()
    for i in range(10):
        print("{} {}".format(data[i].get("sha"),
                             data[i].get("commit").get("author").get("name")))
