**Copyright (c) 2016, Michael Ogg**
# DoorOpener
## Table of Contents
* [Abstract](#Abstract)
* [Basic Methodology](#Basic-Methodology)
* [Components](#Components)
* [Installation](#Installation)
* [Usage](#Usage)
* [Hardware Choices](#Hardware-Choices)
* [License](#License)

## Abstract

DoorOpener was designed by Dr. Michael Ogg with the intention of creating a hands-free method of entering or exiting one’s house. It was documented and is being managed by the Ryerson Chapter of Tetra. DoorOpener assumes the user has limited or no limb mobility but has wheelchair access. It is based around the use of a Raspberry Pi, an Internet of Things (Z-wave) Controller, RFID tags and pressure plates. The objective of having the code, as well as additional information, on Github is to allow users to copy and modify Dr. Ogg’s solution for their own purposes.

This project assumes you have a basic understanding of the following concepts: electrical work, Raspberry Pi , Z-wave controllers, and Python. The files are designed so that you can copy and paste this solution almost directly with only minor changes to the config file, given that the hardware is laid out in the same manner. 

We hope that for whatever reason, whether it be as an electronic hobbyist or as someone working in accessibility services, you can make use of Dr. Ogg’s solution. If you’d like to see a video of the DoorOpener, please click here: https://www.youtube.com/watch?v=-B-Js19Npv0


## Basic Methodology
DoorOpener relies on two main controllers: the Raspberry Pi, which controls the majority of the project, and the Vera MiCasaVerde controller, which controls the door lock and the Z-wave relay. 

The RFID tag readers control if the door is locked or unlocked (based on commands sent from the Pi to the Vera). Since there exists a reader on both the inside and outside of the house, it is possible to change the state of the lock from either side of the door. 

The pushplates activate the door opening (by activating the latch strike and then door operator relay, which in turn acticates the actual door operator).The door closes automatically after a set period of time (declared in the CONFIG file). In addition to the pushplates, there is a Z-wave relay (commonly refferred to as a "Compatabile Contact Closure") which can open the door through a Z-wave app (controlled by a device such as an iPhone or Android). The pushplates and the Z-wave relay are all wired in parallel to the Pi via a 3.5 mono jack and a Swifty USB.

The Pi communicates with the Vera via URL commands (based on API given from Vera) sent via WiFi. This allows the Pi to control the door locker and is the middleman between the Z-wave relay and the Vera itself.

The Pi itself is controlled through threaded python files, which means all the sensors are running at once.


## Components
* `Raspberry Pi` : Main controller that connects to Vera and all other components via USB.
* `RFID Reader` x2 : Device used to read RFID tags
* `Latch Strike Relay` : Remote switch used to open or close the door latch. (Contained in relay box)
* `Door Operator Relay` : Same device as the strike relay but used to turn the door lock on or off. (Contained in relay box). 
* `Vera MiCasaVerde` : Z-Wave hub that connects the contact closures and switches.
* `Z-Wave Compatible Contact Closure` : a relay that allows the door to be opened and close via Z-wave.
* `PushPlates` x4 : In this project, four pushplates are used as switches to actuate the door open relay. One is installed at an average height and the other is installed at foot level height both inside and outside the house.
* `Swifty USB Contact Sensor` : a USB switch interface that can take a 3.5 mono jack.

More information on the components can be found under the [Hardware Choices](#Hardware-Choices) section.


### Hardware Schematic
![tetra - hw schematc -final v2](https://user-images.githubusercontent.com/20260964/51509250-5cd98480-1dc6-11e9-8bd3-5004610687bb.png)

* 'PP' refers to pushplate.
* The black icon Z icon implies the devices is Z-wave controlled.



## Installation

DoorOpener is intended to perform on any Raspberry PI (with a minimum of 4 USB ports or with the use of a USB hub) and be used with any Vera and Alexa devices. Although the source code can be implemented on other devices, the following installation guide only applies to the aforementioned devices:

1. Go to https://home.getvera.com/users/login and register your Vera controller (your home router must be enabled for port forwarding).

1. Pair your z-wave door contact sensor to your vera hub using the following link: https://support.getvera.com/customer/en/portal/articles/2949040-how-to-pair-z-wave-devices?b_id=712. Connect the sensor terminals to a usb connector and plug it into port ttyUSB3 of your Pi device.

1. Add your Alexa device of choice to the ecosystem by following the guide in the link: https://support.getvera.com/customer/portal/articles/2648086.

1. Connect the two RFID readers to ports ttyUSB0 and ttyUSB1 on your Pi device.

1. Add the relay device to port ttyUSB2 on your Pi device and wire those relays accordingly to your pre-existing door automation system.

1. Turn on your Raspberry Pi device then download the Door Opener source code and save it into your home directory.

1. To initiate the Door Opener software one must run doormain.py and this can be done by opening a terminal windown on your Raspberry Pi and typing in the following commands:

```
cd /home/DoorOpener
python doormain.py
```

These commands will run the code once. If you would like to run the code continuously without having to retype these commands after each reboot, use the follwing commands instead:

```
cd /home/DoorOpener
python doormain.py
```

followed by:

```
sudo reboot
```

to reboot the device.

## Usage
The Door Opener software is self contained and complete, thus it doesn't require additional scripts or libraries to function. Depending on your hardware configuration, you may need to adjust several parts of the CONFIG file. As well, you must include your own RFID tag keys in the rfid.db.

   #### Device Port
 
 Please consult Pi documentation online for specific port names. Change the /dev/ section of code (e.g. /dev/ttyUSB0) as required.

  #### Relay triggers / door timings
  

In the case where the timing of relay triggers and open delays are not optimal or do not function as desired, the following lines of the CONFIG file can be edited:

```
strikeRelay /dev/ttyUSB2 1 4    # relay 1, hold 4 sec
doorRelay   /dev/ttyUSB2 2 4    # relay 1, hold 1 sec
openDelay   1.5         # time delay for door to open
```
  #### Vera address
  
 Please consult your Vera documentation for obtaining the URL of your device. 
  
  #### doorID
 You'll have to access the Vera homepage via a browesr. Consult your Vera documentation to find the appropriate address / URL, and there will be a list of devices that can be connected or are already connected. The doorLock will be listed there with a number.
 
 #### RFID tags
  
All valid RFID key tags are stored in the rfid.db file and it can be opened in any plain text editior to add or remove key tags.

## Hardware Choices
The intention of this section is to explain why the specific pieces of hardware were used, as well as to explain in further depth the particular components.

* `Raspberry Pi 2` 
A Pi 2 was used with a Wi-Fi dongle, although a Pi 3 was used with built in wi-fi compatability later by Dr. Ogg.


* `RFID Reader`
* `Latch Strike Relay`
* `Door Operator Relay`
* `Vera MiCasaVerde`
* `Z-Wave Compatible Contact Closure`
* `PushPlates` 
* `Swifty USB Contact Sensor` 


## License
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

ogg.michael@gmail.com

http://michaelogg.com
