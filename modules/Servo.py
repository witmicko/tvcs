#!/usr/bin/python

import DynamicObjectV2
Obj = DynamicObjectV2.Class

import time

# import from parent directory
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

def run (self):
  self.registerOutput("servo", Obj("moving", False))
  while 1:
    time.sleep(1)
    facePos = self.getInputs().facePos
    if (facePos.x > 0): self.output("servo", Obj("moving", True))
    else: self.output("servo", Obj("moving", False))