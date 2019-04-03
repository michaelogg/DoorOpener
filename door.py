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

import time
import relay

# read the config file putting the contents into a dictioary

DEBUG = False

def readConfig(file):
    conf = {}
    f = open(file)
    for line in f:
        e = line.find('#')
        l = line[0:e].split()
        if len(l) == 0:
            continue
        k = l.pop(0)
        conf.update({k : l})

    global DEBUG
    if 'DEBUG' in conf:
        DEBUG = conf['DEBUG'][0] == 'True'	# set global DEBUG flag
    return conf

# class to open the door
# note that in the code, open and close refer to the relay contacts NOT the door
# sr	latch strike relay
# dr	door opener relay
# delay	delay between strike and door opening

class opendoor:
    def __init__(self, sr, dr, delay):
        self.sr = sr
        self.dr = dr
        self.delay = delay

    def do(self):
        if DEBUG: print "opendoor.do() ..."
        relay.momentaryon(self.sr).start()
        time.sleep(self.delay)
        relay.momentaryon(self.dr).start()
