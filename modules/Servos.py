#!/usr/bin/python

import time

# import from parent directory
import sys
import os.path

from Servo import Servo

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import DynamicObjectV2
Obj = DynamicObjectV2.Class

# put your imports here

def init(self):
    pan_servo = Servo(channel=0, min=115, max=460, freq=50)
    # put your self.registerOutput here
    self.registerOutput("sometag", Obj("somefield1", "somevalue", "somefield2", 0))

def run (self):
    # put your init and global variables here
  
    # main loop
    while 1:
        # put your logic here
        # you can use: output, getInputs, message, flags
        self.message('hello')
        self.getInputs().sometag
        # if you want to limit framerate, put it at the end
        time.sleep(0.2)