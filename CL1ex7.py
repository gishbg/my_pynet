#!/usr/bin/env 
"""
7. Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty prints the data structure that is returned.

"""

from __future__ import print_function, unicode_literals
import yaml
import json
from pprint import pprint

def output_format(my_list, file_type):	
	pprint("")
	pprint("#"*30)
	pprint(file_type)
	pprint("#"*30)
	pprint(my_list)
	pprint("#"*30)
	pprint("")


def main():
	"""
	7. Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty prints the data structure that is returned.
	"""
	with open("yaml_file.yaml") as f1:
		yaml_list = yaml.load(f1)

	with open("json_file.json") as f2:
		json_list = json.load(f2)

	output_format(yaml_list, "YAML FILE")
	output_format(json_list, "JSON FILE")

if __name__ == "__main__":
	main()
