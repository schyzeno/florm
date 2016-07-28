from florm import app
from flask import render_template
from florm.database import db_session
from florm.models import User

@app.teardown_appcontext
def shotdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    return render_template('layout.html',message='Hello World!')

@app.route('/users')
def userlist():
    result = db_session.query(User).all()
    return render_template('userlist.html',message='See my child',users=result)
