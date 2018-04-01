#!/usr/bin/env python

"""
6. Write a Python program that creates a list. One of the elements of the list should be a dictionary with at least two keys. Write this list out to a file using both YAML and JSON formats. The YAML file should be in the expanded form.
"""

from __future__ import unicode_literals, print_function
import yaml
import json

def main():
	"""
	6. Write a Python program that creates a list. One of the elements of the list should be a dictionary with at least two keys. Write this list out to a file using both YAML and JSON formats. The YAML file should be in the expanded form.
	"""
	my_dict = {"key1": "atr1", "key2" : "atr2"}

	my_list = range(6)
	my_list.append("something")
	my_list.append("$55")
	my_list.append(my_dict)
	my_list[-1]["g_key"] = "g_atr"

	with open("yaml_file.yaml", "w") as f:
		yaml.dump(my_list, f, default_flow_style=False)

	with open("json_file.json", "w") as f:
		json.dump(my_list, f)

	print("yaml_file.yaml and json_file.json were create.")

if __name__ == "__main__":
	main()

