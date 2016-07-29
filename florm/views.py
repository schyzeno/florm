from florm import app
from flask import render_template, g,request,url_for, redirect, flash 
from florm.database import db_session,init_db
from florm.models import User, Post


@app.teardown_appcontext
def shotdown_session(exception=None):
    db_session.remove()

@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized the database')

@app.route('/')
def index():
    posts = db_session.query(Post).all()
    return render_template('layout.html',pagename="Nam's Home Page", message='Hello World!',posts=posts)

@app.route('/users')
def userlist():
    users = db_session.query(User).all()
    posts = db_session.query(Post).all()
    return render_template('userlist.html',pagename='User List Page', message='See my child',users=users,posts=posts)

@app.route('/post/<postid>')
def view_post(postid):
    posts = db_session.query(Post).all()
    post = db_session.query(Post).filter_by(id=postid).first()
    return render_template('view_post.html', pagename='View Post Page', post=post, posts=posts)

@app.route('/form')
def input_form():
    posts = db_session.query(Post).all()
    return render_template('form.html',message='Enter Users or Posts', pagename='Data Entry Page',posts=posts)

@app.route('/add', methods=['POST'])
def add_user():
    print("entered body")
    db_session.add(User(name=request.form['Name'],email=request.form['email']))
    db_session.commit()
    print("attempt to redirect to:")
    print(url_for('userlist'))
    return redirect(url_for('userlist'))

@app.route('/add_post', methods=['POST'])
def add_post():
    post = Post(title=request.form['title'],body=request.form['body'])
    db_session.add(post)
    db_session.commit()
    return redirect(url_for('view_post',postid=post.id))
