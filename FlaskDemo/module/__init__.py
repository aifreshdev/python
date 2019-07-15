import os
import json
import config
from flask import Flask

app = Flask(__name__, template_folder= config.ROOT_DIR + '/template')
app.secret_key = config.SECRET_KEY

def objToDict(object):
    return object.__dict__

def isAllowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

class Result():
	'''This is a docstring. I have created a new class'''
	def __init__(self, name):
		self.filename = name