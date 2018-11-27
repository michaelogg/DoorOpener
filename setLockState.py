#! /usr/bin/python

import zwaving
import argparse

parser = argparse.ArgumentParser(description="Change the state of a lock")
parser.add_argument("-url", help="URL of vera controller", default='http://192.168.1.13:3480')
parser.add_argument("id", help="device number id", type=int)
parser.add_argument("state", help="state value", type=int, choices=[0,1])
args = parser.parse_args()


#id=16
#state=1

zwaving.zwave(args.url).setLockState(args.id, args.state)
