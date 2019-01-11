#!/usr/bin/python
#
# Control a z-wave device.
#
# Author: Michael Ogg (c) 2016
#

import subprocess
import json
import sys
import getopt
import os.path
import wget

DEBUG=False

HOST="192.168.1.13"
PORT="3480"
#OUT="-O -"
#LOG="-o /dev/null"
#DATA_REQUEST_URL="http://"+HOST+":"+PORT+"/data_request?id=sdata&output_format=json"
#WGET_DEVICES="wget"+" "+OUT+" "+LOG+" "+DATA_REQUEST_URL

#URL="http://"+HOST+":"+PORT+"/"
#WGET="wget"+" "+OUT+" "+LOG+" "+URL

REQUEST={ 0 : 'data_request?id=sdata&output_format=json',\
          2 : {'request':'data_request?id=action&output_format=json&DeviceNum=',
               'DeviceNum':0,
               'serviceId':'&serviceId=urn:upnp-org:serviceId:Dimming1&action=SetLoadLevelTarget&newLoadlevelTarget=',
               'target':0},
          3 : {'request':'data_request?id=action&output_format=json&DeviceNum=',
               'DeviceNum':0,
               'serviceId':'&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=',
               'target':0},
           7:{ 'request':'data_request?id=action&output_format=json&DeviceNum=',
               'DeviceNum':0,
               'serviceId':'&serviceId=urn:micasaverde-com:serviceId:DoorLock1&action=SetTarget&newTargetValue=',
               'target':0},
  }

#print REQUEST

def wgetjson(url):
        f = wget.download(url)
        o = json.load(open(f))
        if os.path.isfile(f):
                os.remove(f)
        return o

"""
def wget(url):
        c="wget"+" "+OUT+" "+LOG+" "+url
        if DEBUG: print c
        o=dict()
	try:
		p=subprocess.Popen(c,stdout=subprocess.PIPE,shell=True)
		if DEBUG: print "Popen"
		out,err=p.communicate()
		if DEBUG: print "comm"
		o=json.loads(out)
		if DEBUG: print "loads"
	except ValueError:
		if DEBUG: print "json exception"
		return dict()
	return o
"""

def toggleLock(id):
        url='http://'+HOST+':'+PORT+'/'
        o = wgetjson(url+REQUEST[0])
        for d in o['devices']:
                if DEBUG: 
                        print 'id=', d['id'], 'category=', d['category'], 'status=', d.get('status'), 'locked=', d.get('locked'), 'level=', d.get('level'), d['name']
                if id == d['id']:
                        locked = int(d['locked'])
                        print 'locked=', locked
                        if locked:
                                locked=0
                        else:
                                locked=1
                        print 'locked=', locked
                        i = REQUEST[d['category']]
                        url += i['request']+str(id)+i['serviceId']+str(locked)
                        wgetjson(url)


def usage():
        print 'Control Z-wave devices.'
        print 'Usage: python', os.path.basename(sys.argv[0]),\
                '[-hd][-i Id][-c Category][-t TargetValue]'
        print '  -h, --help   Print this help message then exit'
        print '  -d, --debug  Turn on debug flag'
        print '  -i Id        Use the device with device number Id'
        print '  -c Category  Use the device(s) with category number Category'
        print '  -t TargetValue Set the target value to TargetValue'

def main(argv):
        global DEBUG
        try:
                opts, args = getopt.getopt(argv[1:], "hdi:c:t:", ["help","debug"])
        except getopt.GetoptError:
                usage()
                sys.exit(2)

        id=0
        cat=0
        tv=0
        for opt, arg in opts:
                if opt in ("-h", "--help"):
                        usage()
                        sys.exit()
                elif opt in ("-d", "--debug"): DEBUG=True
                elif opt == "-i": id=int(arg)
                elif opt == "-c": cat=int(arg)
                elif opt == "-t": tv=int(arg)

        url='http://'+HOST+':'+PORT+'/'
        o = wgetjson(url+REQUEST[0])
        for d in o['devices']:
                if DEBUG: 
                        print 'id=', d['id'], 'category=', d['category'], 'status=', d.get('status'), 'locked=', d.get('locked'), 'level=', d.get('level'), d['name']
                if id == d['id']:
                        i = REQUEST[d['category']]
                        url += i['request']+str(id)+i['serviceId']+str(tv)
                        wgetjson(url)


###------------------------------------------------------------###

"""
id=16
toggleLock(id)
sys.exit()
"""

if __name__ == '__main__':
        main(sys.argv)
