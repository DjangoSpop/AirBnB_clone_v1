import os
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() 

user = os.environ.get('HBNB_MYSQL_USER')
pwd = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
db = os.environ.get('HBNB_MYSQL_DB')

engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db))
Session = scoped_session(sessionmaker(bind=engine))

class ConectDataBase:
    """This class manages storage of hbnb models in MySQL format"""
    def __init__(self):
        """Initialize the class"""
        self.__session = Session()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        if cls is None:
            objs = self.__session.query(User, State, City, Amenity, Place, Review)
            objs = objs.all()
            objs = objs + self.__session.query(BaseModel).all()
            return {type(obj).__name__ + '.' + obj.id: obj for obj in objs}
        else:
            objs = self.__session.query(classes[cls]).all()
            return {type(obj).__name__ + '.' + obj.id: obj for obj in objs}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(engine)
