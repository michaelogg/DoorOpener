#! /usr/bin/python

import relay
import door
import time

# first read the config file
CONFIG ='CONFIG'
conf = door.readConfig(CONFIG)
print conf

# then instantiate the relays
strikeRelay = relay.relay(conf['strikeRelay'])
doorRelay = relay.relay(conf['doorRelay'])

# then hold the relays
delay = float(conf['openDelay'][0])
door.opendoor(strikeRelay, doorRelay, delay).do()
