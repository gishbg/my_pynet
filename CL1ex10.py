#!/usr/bin/env python

"""

10. Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name). Print these entries and their corresponding transform set name.

"""
from __future__ import print_function, unicode_literals
from ciscoconfparse import CiscoConfParse

cisco_conf = CiscoConfParse("cisco_ipsec.txt")

tscrypto_map = cisco_conf.find_objects_wo_child(parentspec=r"^crypto map", childspec=r"AES")

for ts_map in tscrypto_map:
	print(ts_map.text)
	for tr_set in ts_map.all_children:
		if "transform-set" in tr_set.text:
			print(tr_set.text)


