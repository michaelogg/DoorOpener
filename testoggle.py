#! /usr/bin/python

import zwaving

url='http://192.168.1.13:3480'
id=16
zwaving.zwave(url).toggleLock(id)
