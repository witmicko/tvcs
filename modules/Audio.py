#!/usr/bin/python

import time

# import from parent directory
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import IPCThread
IPCThread = IPCThread.Class

import DynamicObjectV2
Obj = DynamicObjectV2.Class

class Class (IPCThread):

    def __init__(self, name, API):
        IPCThread.__init__(self, name, API)

    def run(self):
        self.registerOutput("audio", Obj("playing", False))
        self.output("audio", Obj("playing", True))
