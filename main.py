#!/usr/bin/python

# import from modules directory
import sys
import os.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "/modules")

import threading
import time
import copy

import DynamicObjectV2
Obj = DynamicObjectV2.Class

MsgLock = threading.RLock()
IOLock = threading.RLock()

# enable / disable messages

flags = Obj()

for arg in sys.argv:
    if (arg[:1] == "-"):
        flags[arg[1:]] = True

threads = {}
comms = Obj()

import IPCThread
IPCThread = IPCThread.Class

def registerOutput (owner, tag, default):
    with MsgLock:
        if (comms[tag] and comms[tag].owner != owner):
            return printSync("WARNING: Cannot register tag '{}'. Already registered by thread '{}'.".format(tag, comms[tag].owner.name))
        
        default = Obj(default)
        print("Registered '{}' tag with owner thread '{}' and default output {}.".format(tag, owner.name, default))
        default.owner = owner
        comms[tag] = default

def output (thread, tag, value):
    with MsgLock:
        if (comms[tag].owner != thread):
            return printSync("WARNING: '{}' cannot output with '{}' tag. ACCESS DENIED. Thread '{}' has tag ownership.".format(thread.name, tag, comms[tag].owner.name))
        comms[tag].extend(value)
        info = Obj(copy.copy(comms[tag]))
        del info['owner']
        if (flags.debug): print(" OUTPUT by {}: [{} tag] {}".format(thread.name, tag, info))

def getInputs ():
    with MsgLock:
        return Obj(copy.copy(comms))

def printSync (msg):
    with IOLock:
        print(msg)

def message (thread, msg):
    printSync("MESSAGE by {}: {}".format(thread.name, msg))

# constant
API = {
    "registerOutput": registerOutput,
    "getInputs": getInputs,
    "output": output,
    "message": message
}

# legacy
def addThreadFromClass (Class, name):
    threads[name] = Class(name, API)

def addThreadFromSource (source, name):

    class C (IPCThread):
        def __init__(self, name, API):
            IPCThread.__init__(self, name, API)
            source.init(self)

        def run(self):
            source.run(self)

    threads[name] = C(name, API)

printSync("\n\t\t\tTVCS v0.1.0\n")

# Create threads
import ModuleList

for moduleName in ModuleList.fromSource:
    try:
        moduleSource = __import__(moduleName)
        getattr(moduleSource, "init")
        getattr(moduleSource, "run")
        addThreadFromSource(moduleSource, moduleName)
    except ImportError:
        raise Exception("ERROR: Could not load module '{}' - module does not exist!".format(moduleName))
    except AttributeError:
        raise Exception("ERROR: Could not load module '{}' - module does not have 'init' or 'run' function!".format(moduleName))

for moduleName in ModuleList.fromClass:
    try:
        moduleClass = __import__(moduleName)
        getattr(moduleClass, "Class")
        addThreadFromClass(moduleClass.Class, moduleName)
    except ImportError:
        raise Exception("ERROR: Could not load module '{}' - module does not exist!".format(moduleName))
    except AttributeError:
        raise Exception("ERROR: Could not load module '{}' - module does not have a 'Class'!".format(moduleName))


# Start threads
for t in threads:
    threads[t].daemon = True # make sure threads close with main thread
    threads[t].start()

# make sure main thread dies only on ctrl-c 
while 1:
    pass
