import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models import User, BaseModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from datetime import datetime


# https://docs.sqlalchemy.org/en/20/orm/session_transaction.html#joining-a-session-into-an-external-transaction-such-as-for-test-suites
# https://docs.sqlalchemy.org/en/20/orm/session_basics.html

class UserModelTest(unittest.TestCase):
    def setUp(self):
        # Isolate connections to have fresh DBs and tables
        self.engine = create_engine('sqlite:///:memory:')
        BaseModel.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
    
    def tearDown(self):
        self.session.close()
        BaseModel.metadata.drop_all(self.engine)

    def test_create_1_user(self):
        user = User(username="test_user", password="password", first_name="test", last_name="user")
        self.session.add(user)
        statement = select(User)
        self.session.commit()
        result = self.session.scalars(statement).all()
        self.assertEqual(len(result), 1)
        
        result = result[0]
        self.assertEqual(result.id, 1)
        self.assertEqual(result.username, "test_user")
        self.assertEqual(result.first_name, "test")
        self.assertEqual(result.last_name, "user")
        self.assertEqual(result.password, "password")
        self.assertIsInstance(result.creation_time, datetime)

if __name__ == "__main__":
    unittest.main()
