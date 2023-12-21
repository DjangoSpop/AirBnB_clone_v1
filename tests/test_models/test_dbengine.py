import MySQLdb
import unittest

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Get the initial number of records in the table
cursor.execute("SELECT COUNT(*) FROM states")
initial_count = cursor.fetchone()[0]

# Execute the command or action you want to test
# ...

# Get the updated number of records in the table
cursor.execute("SELECT COUNT(*) FROM states")
updated_count = cursor.fetchone()[0]

# Compare the difference between the initial and updated counts
if updated_count - initial_count == 1:
    print("Test passed")
else:
    print("Test failed")

# Close the database connection
db.close()
