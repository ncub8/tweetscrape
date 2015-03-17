from flask import Flask
import os

app = Flask(__name__, static_url_path='')
app.debug = True
#config_path = os.environ.get("CONFIG_PATH", "blog.config.DevelopmentConfig")
#app.config.from_object(config_path)

import views
#import filter
#from . import login