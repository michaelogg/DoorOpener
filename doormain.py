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

import rfid
import relay
import zwaving
import contact
import door

# main program for door opener
# note that locking/unlocking the door and opening/closing the door
# are logically completely separate operations with no (software) dependence
# see the README file for more details

CONFIG ='CONFIG'

# first read the config file
conf = door.readConfig(CONFIG)
print conf

# then load the database of authorized RFID tags
tagsDB = rfid.tagsDB(conf['rfidDB'][0])

# then instantiate the relays
strikeRelay = relay.relay(conf['strikeRelay'])
doorRelay = relay.relay(conf['doorRelay'])

# then the door lock
doorLock = zwaving.zwave(conf['vera'][0])
doorId = int(conf['doorId'][0])

# then start threads for each RFID reader
for dev in conf['rfidReader']:
    rfid.readRFID(dev, tagsDB, doorLock, doorId).start()

# instantiate object to perform open action
delay = float(conf['openDelay'][0])
action = door.opendoor(strikeRelay, doorRelay, delay)

# and finally start the contact sensor thread
contact.readContact(conf['contactSensor'], action).start()
