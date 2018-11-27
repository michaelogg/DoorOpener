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
import zwaving
import door

# class to manipulate RFID tags database
# dbfile	name of file containing tags database

class tagsDB:
    def __init__(self, dbfile): 
        self.f = open(dbfile)       # tag database
        self.db = set()             # set([a,b,...]) gets rid of duplicates AB: order doesn't matter in  set()
        for line in self.f:
		if door.DEBUG: print line   # print line in tag db if DEBUG mode is True in CONFIG
		l = line.split()            
		if len(l) > 0:               # if at least one element in line
	                self.db.add(l.pop(0))          #??? add first (pop(0)?) element of line to db
									
# add a tag to the database
    def updateDB(self, id):									#??? WHERE IS THIS USED
	l = id.split()
        if len(l) > 0:
		tag = l.pop(0)[1:13]
		if tag in self.db:
			if door.DEBUG: print 'tag OK'
        	self.db.add(tag)

    def writeDB(self):
        print self.db

# check if tag is valid
    def isValid(self, tag):
        if len(tag) == 0:
            return False
        return tag[1:13] in self.db

# class to read RFID tags
# dev		device name of RFID reader, e.g. /dev/ttyUSB0
# tagsDB	tags database
# lock		door lock
# doorId	ID of door lock
class readRFID (threading.Thread):
    def __init__(self, dev, tagsDB, lock, doorId):
        threading.Thread.__init__(self) #for running this in conjunction with other things in the pi
        self.dev = dev
        self.tagsDB = tagsDB
        self.lock = lock
        self.doorId = doorId

# sit in a loop reading tags
    def run(self):
        print "Starting " + self.dev
        f = open(self.dev)
        while True:
            tag = f.readline()
            if len(tag) > 1:
		if door.DEBUG: print "%s: %s %s" % (self.dev, time.ctime(time.time()), tag)
            if self.tagsDB.isValid(tag):
                if door.DEBUG: print 'toggling door lock', self.doorId
                self.lock.toggleLock(self.doorId)
