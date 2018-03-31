#!/usr/bin/env 
"""
7. Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty prints the data structure that is returned.

"""

from __future__ import print_function, unicode_literals
import yaml
import json
from pprint import pprint

with open("my_first.yaml") as f1:
	yaml_file = yaml.load(f1)

with open("my_first.json") as f2:
	json_file = json.load(f2)

pprint("="*30)
pprint("YAML FILE")
pprint("="*30)
pprint(yaml_file)
pprint("="*30)
pprint("")
pprint("")

pprint("="*30)
pprint("JASON FILE")
pprint("="*30)
pprint(json_file)
pprint("="*30)
pprint("")
