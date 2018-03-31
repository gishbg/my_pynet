
#!/usr/bin/env python

"""
6. Write a Python program that creates a list. One of the elements of the list should be a dictionary with at least two keys. Write this list out to a file using both YAML and JSON formats. The YAML file should be in the expanded form.
"""

from __future__ import unicode_literals, print_function
import yaml
import json
from pprint import pprint

my_list = range(6)
my_list.append("something")
my_list.append("$55")
my_list.append({"key1": "atr1", "key2" : "atr2"})
my_list[-1]["g_key"] = "g_atr"

with open("my_first.yaml", "w") as f:
	yaml.dump(my_list, f, default_flow_style=False)

with open("my_second.json", "w") as f:
	json.dump(my_list, f)

print("Files my_first.yaml and my_second.json were create.")


