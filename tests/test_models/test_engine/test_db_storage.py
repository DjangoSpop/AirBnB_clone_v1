import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import MySQLdb
import pep8
import os

class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.user = User()
        cls.user.first_name = "Betty"
        cls.user.last_name = "Holberton"
        cls.user.email = ""
        cls.user.password = "pwd"
        cls.storage = DBStorage()
        cls.storage.reload()
        
    def test_pep8_DBStorage(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")
        
    def test_all(self):
        """Test all method"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._DBStorage__objects)
        
    def test_new(self):
        """Test new method"""
        obj = self.storage.all()
        state = State(name="California")
        state.save()
        key = state.__class__.__name__ + "." + state.id
        self.assertIsNotNone(obj[key])
        
    def test_reload(self):
        """Test reload method"""
        obj = self.storage.all()
        state = State(name="California")
        state.save()
        self.storage.reload()
        key = state.__class__.__name__ + "." + state.id
        self.assertIsNotNone(obj[key])
        
    def test_delete(self):
        """Test delete method"""
        obj = self.storage.all()
        state = State(name="California")
        state.save()
        self.storage.delete(state)
        key = state.__class__.__name__ + "." + state.id
        self.assertIsNone(obj[key])
        
    def test_get(self):
        """Test get method"""
        obj = self.storage.all()
        state = State(name="California")
        state.save()
        key = state.__class__.__name__ + "." + state.id
        self.assertEqual(obj[key], self.storage.get(State, state.id))
        
    def test_count(self):
        """Test count method"""
        obj = self.storage.all()
        state = State(name="California")
        state.save()
        self.assertEqual(self.storage.count(State), len(obj))
        
    def test_create_state(self):
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")

        # Get the number of current records in the "states" table
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = cursor.fetchone()[0]

        # Execute the console command to create a new state
        # ...

        # Get the number of current records in the "states" table again
        cursor.execute("SELECT COUNT(*) FROM states")
        final_count = cursor.fetchone()[0]

        # Compare the difference between the two counts
        difference = final_count - initial_count

        # Assert that the difference is equal to 1
        assert difference == 1

        # Close the database connection
        db.close()
