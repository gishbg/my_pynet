#!/usr/bin/env python

"""

ciscoconfparse
8. Write a Python program using ciscoconfparse that parses this config file (cisco_ipsec.txt). Note, this config file is not fully valid (i.e. parts of the configuration are missing). The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO') and for each crypto map entry print out its children.

"""
from __future__ import print_function, unicode_literals
from ciscoconfparse import CiscoConfParse

cisco_conf = CiscoConfParse("cisco_ipsec.txt")

crypto_map = cisco_conf.find_objects(r"^crypto map CRYPTO")

for line in crypto_map:
	print(line.text)
	for child in line.children:
		print(child.text)
