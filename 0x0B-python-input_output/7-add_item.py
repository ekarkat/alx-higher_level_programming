#!/usr/bin/python3
'''Module 7'''
import sys

save_jason = __import__('5-save_to_json_file').save_to_json_file
load_jason = __import__('6-load_from_json_file').load_from_json_file

try:
    liste = load_jason("add_item.json")
except FileNotFoundError:
    liste = []
liste = liste + sys.argv[1:]
save_jason(liste, "add_item.json")
