import json
from os import path
from models.base_model import BaseModel
import models

class FileStorage:
    """It serializes instances to a JSON file and 
    deserializes back to instances"""
    
    file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the obj in __objects with key <obj class name>.id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (file_path).
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file (file_path) to __objects.
        """
        try:
            with open(FileStorage.file_path, "r") as file:
                data = json.load(file)
                for value in data.values():
                    my_class = value["__class__"]
                    my_class = eval(my_class)
                    obj = my_class(**value)
                    self.new(obj)
        except:
            pass