#! /usr/bin/python

import zwaving
import argparse

parser = argparse.ArgumentParser(description="Get the state of a lock")
parser.add_argument("-url", help="URL of vera controller", default='http://192.168.1.13:3480')
parser.add_argument("id", help="device number id", type=int)
args = parser.parse_args()

#id=16

s=zwaving.zwave(args.url).getLockState(args.id)
print "\nid=",args.id, ", state=",s
