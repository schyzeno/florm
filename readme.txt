samples for the Manual Object Relational Mapping form of SQLAlchemy with Flask

To create the database you can use the init_db function:

>>> from yourapplication.database import init_db
>>> init_db()
You can insert entries into the database like this:

>>> from yourapplication.database import db_session
>>> from yourapplication.models import User
>>> u = User('admin', 'admin@localhost')
>>> db_session.add(u)
>>> db_session.commit()
Querying is simple as well:

>>> User.query.all()
[<User u'admin'>]
>>> User.query.filter(User.name == 'admin').first()
<User u'admin'>

