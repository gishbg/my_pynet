#!/usr/bin/env python

"""
9. Find all of the crypto map entries that are using PFS group2
"""
from __future__ import print_function, unicode_literals
from ciscoconfparse import CiscoConfParse

def main():
    """
    9. Use ciscoconfparse to find all of the crypto map entries that are
    using PFS group2
    """
    cisco_conf = CiscoConfParse("cisco_ipsec.txt")

    crypto_map = cisco_conf.find_objects_w_child(parentspec=r"^crypto map CRYPTO",
                                                 childspec=r"pfs group2")

    for pfs_map in crypto_map:
        print(pfs_map.text)

if __name__ == "__main__":
    main()

