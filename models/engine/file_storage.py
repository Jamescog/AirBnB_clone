#!/usr/bin/python3
"""Contains the defination of the class FileStorage"""


import json
from models.base_model import BaseModel


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
        """deserialize the JSON file to __objects
        ---> only if the JSON file(__file_path) exists
        ---> otherwise do nothing, no exception would be raised
        """
        try:
            with open(FileStorage.__file_path) as reading:
                object_dictionary = json.load(reading)
                for single_object in object_dictionary.values():
                    class_name = single_object["__class__"]
                    del single_object["__class__"]
                    self.new(eval(class_name)(**single_object))
        except FileNotFoundError:
            return

