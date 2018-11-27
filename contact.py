"""
Copyright (c) 2016, Michael Ogg 

This file is part of DoorOpener. DoorOpener is free software: you can
redistribute it and/or modify it under the terms of the GNU General
Public License as published by the Free Software Foundation, either
version 3 of the License, or (at your option) any later version.

DoorOpener is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with DoorOpener. If not, see <http://www.gnu.org/licenses/>.
"""

import door
import threading

# class to read the USB contact sensor
# dev	array containing:
#	dev[0]	USB device, e.g. /dev/input/mouse0
#	dev[1:]	array containing contact close code
# action	an object with a do() method to perform an action on contact closure

class readContact(threading.Thread):
    def __init__(self, dev, action):
        threading.Thread.__init__(self)
        self.dev = dev[0]
        l = len(dev)-1
        self.cc = bytearray(l)
        for i in range(l):
            self.cc[i] = int(dev[i+1])	# dev is type string
        self.action = action

    def run(self):
        print "Start detecting contact closure on " + self.dev
        f = open(self.dev)
        l = len(self.cc)
        b = bytearray(l)
        while True:	# read codes fom device
		for i in range(l):
       		     b[i] = ord(f.read(1))
                c = True
		for i in range(l):
                    c = c and (b[i] == self.cc[i])
                if door.DEBUG: print "sensor value = ", [b[i] for i in range(l)]
		if c:
                    self.action.do()
