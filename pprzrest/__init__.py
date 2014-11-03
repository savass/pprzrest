# -*- coding: utf8 -*-

from flask import Flask
from flask.ext.socketio import SocketIO
import logging as mLog
from mSimProcMon import SimProcMon
import mConfig as AppConfig

LOG_FILENAME = 'pprz_wep.log'
mLog.basicConfig(filename=LOG_FILENAME,level=mLog.DEBUG, format='%(asctime)s %(levelname)s \t %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
#app = Flask(__name__)
app = Flask(__name__, static_url_path = "")

#Debug flag makes the app loading twice - which causes services to star two times.  
app.debug = False
socketio = SocketIO(app)

#create process monitor
SPM = SimProcMon(mLog,socketio)

mLog.info("init PAPARAZZI_PATH : %s", AppConfig.PAPARAZZI_PATH)
mLog.info("init PAPARAZZI_SRC : %s", AppConfig.PAPARAZZI_SRC)
#run process monitor (if required) 
if AppConfig.RUN_PROCESS_MONITOR:
    SPM.run_process_mon_deamon()
#run agents (if required)
if AppConfig.RUN_AGENTS:
    #run link
    RunStr = AppConfig.PAPARAZZI_PATH + AppConfig.LINK_PATH + AppConfig.DEF_LINK_PARAM
    SPM.start_process("link", RunStr)
    #run server
    RunStr = AppConfig.PAPARAZZI_PATH + AppConfig.SERVER_PATH + AppConfig.DEF_SERVER_PARAM
    SPM.start_process("server", RunStr)
    #run app_server
    RunStr = AppConfig.PAPARAZZI_PATH + AppConfig.APP_SERVER_PATH + AppConfig.DEF_APP_SERVER_PARAM
    SPM.start_process("app_server", RunStr)

from pprzrest import views

mLog.info("pprzRest server initiated..")

