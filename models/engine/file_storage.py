#!/usr/bin/python3
"""Module for FileStorage class."""
import json
from datetime import datetime
from models import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            object_dict = {}
            for key, value in self.__objects.items():
                object_dict[key] = value.to_dict()
            json.dump(object_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                object_dict = json.load(f)
                for key, value in object_dict.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass

