from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from florm import app

#engine = create_engine(app.config['DATABASE'], echo=app.config['DBECHO'],convert_unicode=True)
##engine = create_engine('sqlite:///florm.db', echo=True,convert_unicode=True)
#db_session = scoped_session(sessionmaker(autocommit=False,
#                                         autoflush=True,
#                                         bind=engine))
#Base = declarative_base()
#Base.query = db_session.query_property()

def get_engine():
    engine = create_engine('sqlite://.'+app.config['DATABASE'], echo=app.config['DBECHO'],convert_unicode=True)
    return engine

def connect_db():
    engine = get_engine()
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=True,
                                             bind=engine))
    return db_session

def get_base():
    engine = get_engine()
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=True,
                                             bind=engine))
    Base = declarative_base()
    Base.query = db_session.query_property()  
    return Base

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    engine = get_engine()
    db_session = scoped_session(sessionmaker(autocommit=False,
                                                 autoflush=True,
                                                 bind=engine))
    Base = declarative_base()
    Base.query = db_session.query_property()  
    import florm.models
    Base.metadata.create_all(bind=engine)
