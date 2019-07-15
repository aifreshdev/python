import os
from flask import Flask

DEBUG = True
ROOT_DIR = os.path.abspath(os.getcwd())
SECRET_KEY = "super_secret_key"
UPLOAD_FOLDER = ROOT_DIR + '/upload'