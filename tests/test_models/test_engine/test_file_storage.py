#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        try:
            os.remove('file.json')
        except Exception:
            pass
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_new(self):
        """ New object is correctly added to __objects """
        temp = BaseModel()
        for obj in storage.all().values():
            temp = obj
            self.assertTrue(temp is obj)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            self.assertEqual(new.to_dict()['id'], obj.to_dict()['id'])

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'Another storage')
    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
    def test_create_state():
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")

        # Get the number of current records in the "states" table
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = cursor.fetchone()[0]

        # Create a new instance of State and save it to the MySQL database
        state = State(name="California")
        state.save()

        # Get the number of current records in the "states" table
        cursor.execute("SELECT COUNT(*) FROM states")
        final_count = cursor.fetchone()[0]

        # Compare the initial count to the final count to make sure the new
        # record was successfully added to the database
        assert final_count == initial_count + 1

        # Delete the new instance of State from the MySQL database
        state.delete()

        # Get the number of current records in the "states" table
        cursor.execute("SELECT COUNT(*) FROM states")
        final_count = cursor.fetchone()[0]

        # Compare the initial count to the final count to make sure the new
        # record was successfully deleted from the database
        assert final_count == initial_count
        db.close()# ... existing code ...

class TestFileStorage(unittest.TestCase):
    """ Class to test the FileStorage class """

    def test_new_object_added(self):
        """ Test that a new object is correctly added to __objects """
        storage = FileStorage()
        new = BaseModel()
        storage.new(new)
        self.assertIn('BaseModel.' + new.id, storage.all())

    def test_save_file_created(self):
        """ Test that the save method creates the storage file """
        storage = FileStorage()
        new = BaseModel()
        storage.new(new)
        storage.save()
        self.assertTrue(os.path.exists(FileStorage.__file_path))

    def test_reload_file_loaded(self):
        """ Test that the reload method successfully loads the storage file """
        storage = FileStorage()
        new = BaseModel()
        storage.new(new)
        storage.save()
        storage.reload()
        self.assertIn('BaseModel.' + new.id, storage.all())

    def test_reload_empty_file(self):
        """ Test that the reload method handles an empty file """
        storage = FileStorage()
        with open(FileStorage.__file_path, 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_nonexistent_file(self):
        """ Test that the reload method handles a nonexistent file """
        storage = FileStorage()
        os.remove(FileStorage.__file_path)
        self.assertIsNone(storage.reload())

    def test_create_state(self):
        """ Test creating and deleting a State object in the database """
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")

        # Get the number of current records in the "states" table
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = cursor.fetchone()[0]

        # Create a new instance of State and save it to the MySQL database
        state = State(name="California")
        state.save()

        # Get the number of current records in the "states" table
        cursor.execute("SELECT COUNT(*) FROM states")
        final_count = cursor.fetchone()[0]

        # Compare the initial count to the final count to make sure the new
        # record was successfully added to the database
        self.assertEqual(final_count, initial_count + 1)

        # Delete the new instance of State from the MySQL database
        state.delete()

        # Get the number of current records in the "states" table
        cursor.execute("SELECT COUNT(*) FROM states")
        final_count = cursor.fetchone()[0]

        # Compare the initial count to the final count to make sure the new
        # record was successfully deleted from the database
        self.assertEqual(final_count, initial_count)

        # Close the database connection
        db.close()

# ... remaining code ...