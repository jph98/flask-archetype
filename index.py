#!/usr/bin/env python

import yaml

from flask import Flask
from flask import Flask, render_template
from flask import request, session
from flask import make_response

app = Flask(__name__)
app.debug = True

configurationfile = 'app.yaml'
config = {}

# Init
def init():
	"""Init configuration"""
	configfile = open(configurationfile, 'r')
	global config
	try:
		config = yaml.load(configfile)
		if config is not None:
			for item in config:
				print item + ": " + str(config[item])
	finally:		
		configfile.close()

@app.route("/")
def hello():

	session['appname'] = config['appname']
	return render_template('index.html')

if __name__ == "__main__":
	init()
	app.debug = True
	app.secret_key = 'A0Zr97sfas8j/asdkj R~XHH!jkjaLWX/,?RT'
	app.run(host='0.0.0.0')