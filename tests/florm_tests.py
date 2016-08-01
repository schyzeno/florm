import os
import pytest
import tempfile

from context import florm
from florm.database import init_db
#prefix ='sqlite:///',
@pytest.fixture
def client(request):
    db_fd, florm.app.config['DATABASE'] = tempfile.mkstemp()
    florm.app.config['DBECHO'] = False
    florm.app.config['TESTING'] = True
    print(db_fd)
    client = florm.app.test_client()
    with florm.app.app_context():
        init_db()

    def teardown():
        os.close(db_fd)
        os.unlink(florm.app.config['DATABASE'])
    request.addfinalizer(teardown)

    return client


def test_empty_db(client):
    rv = client.get('/')
    assert b'No Posts.' in rv.data

#if __name__ == '__main__':
#    unittest.main()
