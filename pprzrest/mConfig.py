# -*- coding: utf8 -*-

#Configuration File

import os

SERVER_PATH = "/sw/ground_segment/tmtc/server "
LINK_PATH = "/sw/ground_segment/tmtc/link "
APP_SERVER_PATH = "/sw/ground_segment/tmtc/app_server "

#Get PAPARAZZI_HOME path
PAPARAZZI_PATH = os.getenv('PAPARAZZI_HOME')
if PAPARAZZI_PATH is None:
	#if no environment variable 
	PAPARAZZI_PATH = "/home/pprz/DEV/paparazzi"

#Get PAPARAZZI_SRC path
PAPARAZZI_SRC = os.getenv('PAPARAZZI_SRC')
if PAPARAZZI_SRC is None:
	os.environ["PAPARAZZI_SRC"] = PAPARAZZI_PATH

#Default parameters to run agents
DEF_LINK_PARAM = "-d /dev/paparazzi/xbee -transport xbee -s 57600"

DEF_SERVER_PARAM = ""

DEF_APP_SERVER_PARAM = "-v -utcp"

#Run agents on app start
RUN_AGENTS = True
#Run process monitor on app start
RUN_PROCESS_MONITOR = True



