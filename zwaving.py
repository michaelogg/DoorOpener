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

# Control a z-wave device.

import json
import sys
import getopt
import os.path
import wget
import door

# dictionary of zwave request templates indexed by device category
REQUEST={ 0 : 'data_request?id=sdata&output_format=json',
          2 : {'request':'data_request?id=action&output_format=json&DeviceNum=',
               'DeviceNum':0,
               'serviceId':'&serviceId=urn:upnp-org:serviceId:Dimming1&action=SetLoadLevelTarget&newLoadlevelTarget=',
               'target':0},
          3 : {'request':'data_request?id=action&output_format=json&DeviceNum=',
               'DeviceNum':0,
               'serviceId':'&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=',
               'target':0},
         7 : { 'request':'data_request?id=action&output_format=json&DeviceNum=',
               'DeviceNum':0,
               'serviceId':'&serviceId=urn:micasaverde-com:serviceId:DoorLock1&action=SetTarget&newTargetValue=',
               'target':0},
  }

# encapsulate a wget returning the result as a json encoded object
def wgetjson(url):
        if door.DEBUG: print url
        f = wget.download(url)
        o = json.load(open(f))
        if os.path.isfile(f):
                os.remove(f)
        return o

# class to represent zwave devices
# server	the vera server and port, e.g. http://192.168.1.13:3480
class zwave:
        def __init__(self, server):
                l = len(server)           # server variable is a URL from CONFIG
                if server[l-1] != '/':    # append '/' char to end of URL if not already there
                        server+='/'
                print server
                self.server = server

# toggle lock's state
# id the lock id
        def toggleLock(self, id):
                url = self.server
                o = wgetjson(url+REQUEST[0])	# find all devices
                for d in o['devices']:
                        if id == d['id']:
                                locked = int(d['locked'])	# get lock state
                                if locked:
                                        locked=0
                                else:
                                        locked=1
                                i = REQUEST[d['category']]
                                url += i['request']+str(id)+i['serviceId']+str(locked)
                                wgetjson(url)	# change lock state

# set lock's state
# id the lock id
# state The state to which lock should be set, 0=unlocked, 1=locked
        def setLockState(self, id, state):
                url = self.server
                o = wgetjson(url+REQUEST[0])	# find all devices
                for d in o['devices']:
                        if id == d['id']:
                                i = REQUEST[d['category']]
                                url += i['request']+str(id)+i['serviceId']+str(state)
                                wgetjson(url)	# change lock state

# get lock's state
# id the lock id
        def getLockState(self, id):
                url = self.server
                o = wgetjson(url+REQUEST[0])	# find all devices
                for d in o['devices']:
                        if id == d['id']:
                                locked = int(d['locked'])	# get lock state
                                return locked
