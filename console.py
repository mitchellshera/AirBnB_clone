#!/usr/bin/python3
"""
This module is the entry point of the command interpreter
It contains the class HBNBCommand
"""
import cmd
import json
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_name = "BaseModel"

    def do_quit(self, *args):
        """     Quit the program """
        return True

    def do_EOF(self, *args):
        """Exit the program """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, *args):
        """
        create a new instance of BaseModel
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, *args):
        """
        Prints the string representation of an instance
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, *args):
        """
        Deletes an instance based on the class name and id
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, *args):
        """
        Prints all string representations of instances
        """
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]:
            obj_dict = models.storage.all(eval(args[0]))
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, *args):
        """
        Updates an instance based on the class name and id
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                obj = models.storage.all()[key]
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    setattr(obj, attr_name, attr_value)
                    models.storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
