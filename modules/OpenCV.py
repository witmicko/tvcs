#!/usr/bin/python

import time
import random

# import from parent directory
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import DynamicObjectV2
Obj = DynamicObjectV2.Class

def run (self):
  toggle = False

  self.registerOutput("facePos", Obj("x", 0, "y", 0))
  while 1:
    if (toggle): minValue = 0
    else: minValue = -90

    if (toggle): maxValue = 90
    else: maxValue = 0
    
    toggle = not toggle

    self.output("facePos", Obj("x", random.randint(minValue, maxValue), "y", random.randint(-90, 90)))
    time.sleep(3)