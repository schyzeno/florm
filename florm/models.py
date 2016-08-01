from sqlalchemy import Column, Integer, String, Text, DateTime
from florm.database import get_base
import datetime

Base = get_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=True)
    timestamp = Column(DateTime)
    
    def __init__(self, title=None, body=None, timestamp=datetime.datetime.now()):  
        self.title = title
        self.body = body
        self.timestamp = timestamp
    
    def __repr__(self):
        return '<Post %r, %r>' % (self.id,self.title)


