import unittest
from console import HBNBCommand, storage  # replace 'your_module' with the actual module name

class TestCreate(unittest.TestCase):
    def setUp(self):
        """
        Set up for the tests.
        """
        self.cmd = HBNBCommand()

    def test_create_no_args(self):
        """
        Test creating an object with no arguments.
        """
        with self.assertRaises(SystemExit):
            self.cmd.do_create('')

    def test_create_invalid_class(self):
        """
        Test creating an object with an invalid class name.
        """
        with self.assertRaises(SystemExit):
            self.cmd.do_create('InvalidClassName')

    def test_create_valid_class_no_params(self):
        """
        Test creating an object with a valid class name and no parameters.
        """
        self.cmd.do_create('ValidClassName')
        self.assertTrue('ValidClassName' in storage.all())

    def test_create_valid_class_with_params(self):
        """
        Test creating an object with a valid class name and parameters.
        """
        self.cmd.do_create('ValidClassName name="Test" number=1')
        self.assertTrue('ValidClassName' in storage.all())
        obj = storage.all()['ValidClassName']
        self.assertEqual(obj.name, 'Test')
        self.assertEqual(obj.number, 1)

if __name__ == '__main__':
    unittest.main()