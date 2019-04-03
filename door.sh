#! /bin/sh 
#
### BEGIN INIT INFO
# Provides:          door.sh
# Required-Start:    $local_fs syslog
# Required-Stop:     $local_fs syslog
# Should-Start: 
# Should-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: start the DoorOpener daemon
# Description:
### END INIT INFO

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
