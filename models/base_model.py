#!/usr/bin/python3
"""this scripts contains the defination of BaseModel class"""

import models
import uuid
from datetime import datetime


class BaseModel():
    """Defines all common attributes and methods for all other classes

    Attributes:
        id(str): -assign an uuid when an instance is created
        created_at(datetime): -  assign with the
            current datetime when an instance is created
        updated_at(datetime) -  assign with the current datetime when an
         instance is created and it will be updated
         every time you change your object

    """
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel.
        Args:
            *args (any): variable number of args(Unused)
            **kwargs (dict): Key/Value pairs of attributes

        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute <updated_at>
        with the current datetime"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all key/value pairs -
        of __dict__ of the instance"""
        copy_dict = self.__dict__.copy()
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        copy_dict["__class__"] = self.__class__.__name__
        return copy_dict

    def __str__(self):
        """print [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

