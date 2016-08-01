from flask import Flask
app = Flask(__name__)
app.config.from_object('florm.dfconfig')
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
import florm.views
