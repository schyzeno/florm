import os
import unittest
import tempfile

from context import florm
from florm.database import init_db

class FlormTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, florm.app.config['DATABASE'] = tempfile.mkstemp()
        florm.app.config['ECHODB'] = False
        florm.app.config['TESTING'] = True
        self.app = florm.app.test_client()
        print('====================')
        print(florm.app.config['DATABASE'])
        print('====================')
        with florm.app.app_context():
            init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(florm.app.config['DATABASE'])
    
    def test_empty_db(self):
        rv = self.app.get('/')
        print(rv.data)
        assert b'No Posts.' in rv.data

if __name__ == '__main__':
    unittest.main()
