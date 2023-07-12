import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
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
