#!/usr/bin/python

# import from parent directory
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import time

import IPCThread
IPCThread = IPCThread.Class

import DynamicObject

class Class (IPCThread):

    def __init__(self, name, API):
        IPCThread.__init__(self, name, API)
        self.registerOutput("audio2", {"playing": False})

    def run(self):
        while 1:
            self.output("audio2", {"playing": True})
            time.sleep(0.2)