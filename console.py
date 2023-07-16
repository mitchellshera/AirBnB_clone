#!/usr/bin/python3
"""
This module is the entry point of the command interpreter
It contains the class HBNBCommand
"""
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                   "Place": Place, "Review": Review, "State": State, "User": User}
        if arg not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                   "Place": Place, "Review": Review, "State": State, "User": User}
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + '.' + args[1]
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                   "Place": Place, "Review": Review, "State": State, "User": User}
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + '.' + args[1]
        if key in objs:
            objs.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = arg.split()
        objs = storage.all()
        result = []
        if not args:
            for obj in objs.values():
                result.append(str(obj))
        else:
            if args[0] not in ["Amenity", "BaseModel", "City", "Place", "Review", "State", "User"]:
                print("** class doesn't exist **")
                return
            for key in objs:
                if key.split('.')[0] == args[0]:
                    result.append(str(objs[key]))
        print(result)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                   "Place": Place, "Review": Review, "State": State, "User": User}
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + '.' + args[1]
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objs[key]
        attr_name = args[2]
        attr_value = args[3]
        if attr_name == "id" or attr_name == "created_at" or attr_name == "updated_at":
            return
        setattr(obj, attr_name, attr_value)
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
