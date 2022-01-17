#! /usr/bin/env python3

from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])

from app.main import routes
