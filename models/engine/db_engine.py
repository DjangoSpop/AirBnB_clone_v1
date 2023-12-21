import mysqldb
import file_storage
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db')
def db_storage:
    dbcoonection = mysqldb.connect(host="localhost", user="hbnb_dev", passwd="hbnb_dev_pwd", db="hbnb_dev_db")
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM states")
    initial_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM states")
    final_count = cursor.fetchone()[0]
    db.close()





