#!/usr/bin/python

import DynamicObjectV2
Obj = DynamicObjectV2.Class

# import from parent directory
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

def run (self):
  self.registerOutput("audio", Obj("x", 0, "a", 0, "y", 0))