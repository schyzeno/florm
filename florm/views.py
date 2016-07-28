from florm import app
from flask import render_template
from florm.database import db_session

@app.teardown_appcontext
def shotdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    return render_template('layout.html',message='Hello World!')
