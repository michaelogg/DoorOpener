#! /usr/bin/python

import zwaving
import door

CONFIG ='CONFIG'
conf = door.readConfig(CONFIG)
door.DEBUG = True	# override DEBUG flag

if door.DEBUG: print conf

doorLock = zwaving.zwave(conf['vera'][0])
doorId = int(conf['doorId'][0])

doorLock.toggleLock(doorId)
