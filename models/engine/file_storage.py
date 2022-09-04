#!/usr/bin/python3
"""Contains the defination of the class FileStorage"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """serialize and deserialize instance to JSON file and vice-versa
    Attributes:
        __file_path (str): - path to the JSON file(ex: file_name.json)
        __objects (dict): - empty but will store all objects
                            using <class name>.id
                            example:
                            (ex: to store a BaseModel object with
                            id=12121212,the key will be BaseModel.12121212)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name >.id
        Args:
            obj (any): - newly created object
        """
        object_class = obj.__class__.__name__
        id = obj.id
        class_id = object_class + "." + id
        FileStorage.__objects[class_id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path"""
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as writting:
            json.dump(dict_to_json, writting)

    def reload(self):
        """Deserializes the JSON file to __objects. only if the
        JSON file (__file_path) exists otherwise, do nothing.
        If the file does not exist, no exception raised
        """
        try:
            with open(__class__.__file_path) as rd:
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                dict_objs = json.load(rd)
                for key in dict_objs:
                    if key.split(".")[0] == 'BaseModel':
                        __class__.__objects[key] = BaseModel(**dict_objs[key])
                    elif key.split(".")[0] == 'User':
                        __class__.__objects[key] = User(**dict_objs[key])
                    elif key.split(".")[0] == 'State':
                        __class__.__objects[key] = State(**dict_objs[key])
                    elif key.split(".")[0] == 'City':
                        __class__.__objects[key] = City(**dict_objs[key])
                    elif key.split(".")[0] == 'Amenity':
                        __class__.__objects[key] = Amenity(**dict_objs[key])
                    elif key.split(".")[0] == 'Place':
                        __class__.__objects[key] = Place(**dict_objs[key])
                    elif key.split(".")[0] == 'Review':
                        __class__.__objects[key] = Review(**dict_objs[key])
        except FileNotFoundError:
            pass
