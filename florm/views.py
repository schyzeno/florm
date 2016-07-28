from florm import app
from flask import render_template, g,request,url_for, redirect, flash 
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

@app.route('/form')
def userform():
    return render_template('form.html',message='See user form')

@app.route('/add_user', methods=['POST'])
def add_user():
    db_session.add(User(name=request.form['name'],email=request.form['email']))
    db_session.commit()
    return redirect(url_for('userlist')) 
