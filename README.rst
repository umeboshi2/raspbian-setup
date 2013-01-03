raspbian-setup
==============

Introduction
-----------------

The Raspberry Pi is a nifty little machine that can be used for many 
different purposes.

I was given one of these as a Christmas present, and decided to use it 
as a small network appliance.  I have yet to actually use the video interface 
on the machine, and instead, I primarily use ssh over ethernet to control the 
device.  These instructions are written with this in mind, however things 
should work similar using local access to the device.

Initial Stuff
---------------------

- Download raspbian image and write to SD Card.

- Boot raspberrypi and run sudo raspi-config

  + expand rootfs to fill size of card

  + set locales and tzdata

  + I usually drop the memory given to the GPU to 16

  + Fortunately, ssh server is enabled by default

  + I usually disable desktop on boot

- (Optional) Setup new user and add to sudo, adm, staff, etc. groups

- reboot

- ssh <user>@raspberrypi

- sudo apt-get install git

- git clone https://github.com/umeboshi2/raspbian-setup.git

- cd raspbian-setup

- edit the initial-setup script

  + If you don't want to remove desktop environment, comment or cut that part out
    of the script.

- sudo ./initial-setup

- ./site-setup


