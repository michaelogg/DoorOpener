#! /usr/bin/python

import contact
import door

CONFIG ='CONFIG'
conf = door.readConfig(CONFIG)
door.DEBUG = True	# override DEBUG flag

if door.DEBUG: print conf

class action:
    def do(self):
        print 'action.do()'

contact.readContact(conf['contactSensor'], action()).start()
