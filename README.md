**Copyright (c) 2016, Michael Ogg**
# DoorOpener
## Table of Contents
* [Abstract](#Abstract)
* [Basic Methodology](#Basic-Methodology)
* [Components](#Components)
* [Installation](#Installation)
* [Usage](#Usage)
* [Lisence] (#Lisence)

## Abstract

This Automatic Door Opener was designed by Dr. Michael Ogg with the intention of creating a hands-free method of entering or exiting one’s house. It was documented and is being managed by the Ryerson Chapter of Tetra. This door opener assumes the user has limited or no limb mobility but has wheelchair access. It is based around the use of a Raspberry Pi, an Internet of Things (Z-wave) Controller, RFID tags and pressure plates. The objective of having the code, as well as additional information, on Github is to allow users to copy and modify Dr. Ogg’s solution for their own purposes.

This project assumes you have a basic understanding of the following concepts: electrical work, Raspberry Pi , Internet of Things controllers, and Python. The files are designed so that you can copy and paste this solution almost directly with only minor changes to the config file, providing the hardware is laid out in the same manner. 

We hope that for whatever reason, whether it be as an electronic hobbyist or as someone working in accessibility services, you can make use of Dr. Ogg’s solution. If you’d like to see a video of the Automatic Door Opener, please click here: https://www.youtube.com/watch?v=-B-Js19Npv0


## Basic Methodology
* Brief description of method of operation

## Components
* `Raspberry Pi` : Main controller that connects to Vera and all other components via USB.
* `RFID Reader` x2 : Device used to read RFID tags
* `Door Strike Relay` : Remote switch used to open or close the door latch. (Contained in relay box)
* `Door Open Relay` : Same device as the strike relay but used to turn the door lock on or off. (Contained in relay box)
* `Vera` : Z-Wave hub that connects the contact closures and switches.
* `Z-Wave Compatible Contact Closure` : a relay that allows the door to be opened and close via Z-wave.
* `Push Plates` x4 : In this project, four pushplates are used as switches to actuate the door open relay. One is installed at an average height and the other is installed at foot level height both inside and outside the house.


![tetra - hw schematc final](https://user-images.githubusercontent.com/20260964/50591673-ca952f00-0e5e-11e9-99dc-36fbd32591af.png)



## Installation

***WHAT THE USER NEEDS TO CHANGE WITHIN THE CODE*** 

-> Vera IP / other Z-Wave Hub
-> RFID Keys
-> USB / device labelling (depending on how the user wires it)

The installation process is fairly simple and straight forward:

When Pi boots, push button and system is initialized.

## Usage
* Write walk Michael talked about
* Include snippets of code

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
