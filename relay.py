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

import threading
import time

# encapsulate a relay
# r is the relay, r[0] is the device e.g. /dev/ttyUSB0, r[1] is the relay number A: Found in config file. Used for the relay box.
# to write to the device, the program might have to be run with sudo

class relay:
    def __init__(self, r): #__init__ is a class constructor.
        print r
        self.stream = open(r[0], "w", 0)        # r is the line in CONFIG starting with 'strikeRelay' or 'doorRelay' -> r[0] refers to device in CONFIG
        self.buff = bytearray(3)    # byte array of size 3            
        self.buff[0] = '\xff'		# first byte is wake up
        self.buff[1] = int(r[1])	# second byte is relay number
        self.hold = float(r[2])		# relay hold time

# get hold time
    def getHoldTime(self):
        return self.hold

# close the relay
    def close(self):
        self.buff[2] = '\x01'
        self.stream.write(self.buff)

# open the relay
    def open(self):
        self.buff[2] = '\x00'
        self.stream.write(self.buff)

# class to do a momentary on. since the hold time is arbitrary, the action
# has to be in its own thread.
# relay	the relay AB: what does this mean?

class momentaryon(threading.Thread):
    def __init__(self, r):
        threading.Thread.__init__(self)
        self.r = r
        self.hold = r.getHoldTime()

    def run(self):
        self.r.close()
        time.sleep(self.hold)
        self.r.open()
