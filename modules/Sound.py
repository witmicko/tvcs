#!/usr/bin/python

import DynamicObjectV2
Obj = DynamicObjectV2.Class

import time

# import from parent directory
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

def run (self):
  self.registerOutput("audio", Obj("playing", False))
  while 1:
    time.sleep(0.5)
    servo = self.getInputs().servo
    if (servo.moving): self.output("audio", Obj("playing", True))
    else: self.output("audio", Obj("playing", False))