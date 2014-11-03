# -*- coding: utf8 -*-

from gevent import monkey
monkey.patch_all()

from flask import render_template, session, request, redirect, url_for, jsonify, send_file
from flask.ext.socketio import emit


from pprzrest import app,socketio, mLog, SPM, AppConfig


@socketio.on('connect', namespace='/PprzOnWeb')
def test_connect():
    print "client connected"
    mLog.debug("Client connected.")
    if not SPM.ProcessOutput is None:
    	emit('StatusMsg', {'data': SPM.ProcessOutput,
    		'link_sts': SPM.get_status("link"),
    		'server_sts': SPM.get_status("server"),
    		'app_server_sts': SPM.get_status("app_server"),
    		'link_arg': SPM.get_process_arg("link"),
    		'server_arg':SPM.get_process_arg("server"),
    		'app_server_arg': SPM.get_process_arg("app_server")
    		 } )

@socketio.on('disconnect', namespace='/PprzOnWeb')
def test_disconnect():
    print('Client disconnected')
    mLog.debug("Client disconnected.")

type
#Run 
@app.route('/pprzrest/api/v1.0/run', methods = ['POST'])
def run_agent():    
    agent_name = request.form.get('agent', "")
    variable = request.form.get('inputvar', "")
    #print "agent:", agent_name
    #print "variable",variable
    if agent_name == "link":
    	
    	RunStr = AppConfig.PAPARAZZI_PATH + AppConfig.LINK_PATH + variable
    	SPM.start_process("link", RunStr)
   	
    if agent_name == "server":

    	RunStr = AppConfig.PAPARAZZI_PATH + AppConfig.SERVER_PATH + variable 	
    	SPM.start_process("server", RunStr)
    	
    if agent_name == "app_server":
    	
    	RunStr = AppConfig.PAPARAZZI_PATH + AppConfig.APP_SERVER_PATH + variable    	
    	SPM.start_process("app_server", RunStr)

    return jsonify( { 'STATUS': 'OK' } ), 200

#stop
@app.route('/pprzrest/api/v1.0/stop', methods = ['POST'])
def stop_agent():
    agent_name = request.form.get('agent', "")
    if agent_name == "link":
    	SPM.stop_process("link")
    if agent_name == "server":
    	SPM.stop_process("server")
    if agent_name == "app_server":
    	SPM.stop_process("app_server")

    return jsonify( { 'STATUS': 'OK' } ), 200

@app.route('/mfile', methods = ['GET'])
def get_file():
    mFile = request.form.get('file_path', None)
    mLog.debug("Client file request: %s", mFile)
    if mFile is None:
        return jsonify( { 'ERROR': 'No file name in request.' } ), 400
    return send_file(mFile)

@app.route('/')
def index():
    return render_template('index.html')
