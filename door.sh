#! /bin/sh 

case "$1" in 
      start) 
            cd /home/pi/DoorOpener
            /usr/bin/python doormain.py & 
            ;; 
      stop) 
            killall -v python 
            ;; 
esac 
exit 0 
