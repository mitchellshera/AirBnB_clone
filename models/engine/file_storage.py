#!/usr/bin/python3

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
        "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj is not None:
            key = obj.__class__.__name__ + "." + str(obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json_objects = {}
            for key, value in FileStorage.__objects.items():
                json_objects[key] = value.to_dict()
            j = json.dumps(json_objects)
            file.write(j)
            
    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for value in data.values():
                    my_class = value["__class__"]
                    my_class = eval(my_class)
                    obj = my_class(**value)
                    self.new(obj)
        except:
            pass
