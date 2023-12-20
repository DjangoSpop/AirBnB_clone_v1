#!/usr/bin/python3
""" """
import unittest
import MySQLdb
from models.state import State


class test_State(unittest.TestCase):
    def setUp(self):
        self.db = MySQLdb(host="localhost",user="hbnbtest",passwd="hbnb_test_pwd")
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT COUNT(*) FROM states")
        self.initial_count = self.cursor.fetchone()[0]


    def test_create_state(self):
        State.create(name = "Calfornia")

        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]
        self.assertEqual(final_count - self.initial_count, 1)
    def tearDown(self):
        self.db.close()
if __name__ == "__main__":
    unittest.main()
                
        