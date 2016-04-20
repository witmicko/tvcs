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
    # s_joint = Servo(channel=0, min=250, max=327, freq=50)
    s_tilt    = Servo(channel=1, min=250, max=327, freq=50)
    s_pan     = Servo(channel=2, min=250, max=410, freq=50)
    # self.registerOutput("sometag", Obj("somefield1", "somevalue", "somefield2", 0))

def run (self):
    # put your init and global variables here

    # main loop
    while 1:
        headPosition = self.getInputs().headPosition
        lampPosition = self.getInputs().lampPosition

        s_tilt.move_to(headPosition.y)
        s_pan.move_to(headPosition.x)
        s_joint.move_to(lampPosition.z)

        time.sleep(0.2)