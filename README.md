# install docker on a raspberry pi
tested on rpi3b+ on ethernet

will run all the required emoncms components within docker containers
host system reboots trigged by ~/.host-shutdown-interface.sh

## install instructions
from your laptop:
--------------
download the official raspibian buster lite [I'm using 2020-02-13-raspbian-buster-lite.zip](magnet:?xt=urn:btih:2213f24bca4031663b3dfa99fb554dce8cfcb5da&dn=2020-02-13-raspbian-buster-lite.zip&tr=http%3A%2F%2Ftracker.raspberrypi.org%3A6969%2Fannounce)
burn image to micro sd card using Etcher
once completed (7mins for me), remove and re-insert sd card
put empty file onto /boot partition named `ssh` to enable headless remote access
unmount the sd card (eject/sefely remove) and put it into the raspberry pi
turn on the raspberry pi
get the new ip - try the fing app or the nmap command (eg. `nmap -sP 192.168.1.0/24`) to see list of devices
login via ssh `$ ssh pi@192.168.1.[0-254]` into a terminal window

from the pi
-------------
all the commands have been put into a bash script:
$ ./install.sh 

shutdown controller
------------
to enable docker container to reboot host, create volume on container that maps to the file /var/run/shutdown_signal. if the contents of this file is changed to "reboot" then the command `sudo shutdown -r now` is triggerd
@requires inotify-tools

TODO:
install instructions on laptop
 - just git clone the repo and run docker-compose up in the new directory
