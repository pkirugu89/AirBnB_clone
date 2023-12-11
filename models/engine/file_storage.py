#!/usr/bin/python3
""" FileStorage class."""
import json
from models.base_model import BaseModel
from os.path import isfile
from models.user import User


class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserialize the JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dict __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """
        set in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the json file.
        """
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            objs = FileStorage.__objects
            dict_obj = {k: v.to_dict() for k, v in objs.items()}
            json.dump(dict_obj, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects.
        """
        if isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                try:
                    dict_obj = json.load(file)
                    for key, value in dict_obj.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        obj = cls(**value)
                        self.__objects[key] = obj
                except Exception as e:
                    pass
