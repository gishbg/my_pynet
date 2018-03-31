#!/usr/bin/env 
"""
7. Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty prints the data structure that is returned.

"""

from __future__ import print_function, unicode_literals
import yaml
import json
from pprint import pp

with open("my_first.yaml") as f:
	yaml_file = yaml.load(f)

with open("my_first.json") as f:
	json_file = jason.load(f)

pp("="*30)
pp("YAML FILE")
pp("="*30)
pp(yaml_file)
pp("="*30)
pp()
pp()

pp("="*30)
pp("JASON FILE")
pp("="*30)
pp(json_file)
pp("="*30)
pp()
