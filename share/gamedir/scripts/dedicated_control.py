#!/usr/bin/python -u

# Dedicated Control handler script for OpenLieroX
# (http://openlierox.sourceforge.net)

# We're expecting this file to be run from "scripts" dir - that's from rev. 3260 or so
# TODO: NO, we are not expecting this!
# It was only done because this script is buggy and does not work otherwise.

# TODO: what is the difference from this file to dedicated_control?

import os, sys, time

# Add current dir to module search path
sys.path.append( os.getcwd() )
sys.path.append( os.path.dirname(sys.argv[0]) )

# Add dir with config file to module search path
try:
	os.listdir(os.getenv("HOME")+"/.OpenLieroX/cfg")
	sys.path.append(os.getenv("HOME")+"/.OpenLieroX/cfg")
except:
	pass

# Add dir with config file to module search path
try:
	os.listdir(os.getenv("HOME")+"/Library/Application Support/OpenLieroX/cfg")
	sys.path.append(os.getenv("HOME")+"/Library/Application Support/OpenLieroX/cfg")
except:
	pass

try:
	os.listdir(os.getenv("USERPROFILE")+"/My Documents/OpenLieroX/cfg") # TODO: lame, use Win32 API
	sys.path.append(os.getenv("USERPROFILE")+"/My Documents/OpenLieroX/cfg")
except:
	pass

try:
	os.listdir(os.path.dirname(sys.argv[0])+"/../cfg")
	sys.path.append(os.path.dirname(sys.argv[0])+"/../cfg")
except:
	pass

try:
	os.listdir("/etc/OpenLieroX/cfg")
	sys.path.append("/etc/OpenLieroX/cfg")
except:
	pass

import dedicated_config as cfg # Per-host config like admin password
import dedicated_control_handler as hnd # control handler
import dedicated_control_io as io # control handler

## The game loop ##

hnd.init()

io.messageLog("Dedicated_control started",io.LOG_INFO)

def MainLoop():
	hnd.signalHandler(io.getSignal()):


if not io.OlxImported:
	while hnd.gameState != hnd.GAME_QUIT:

		MainLoop()
