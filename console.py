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
    """
    This class contains the command interpreter
    """
    prompt = "(hbnb) "
    class_name = "BaseModel"

    def do_quit(self, *arg):
        """ Exit the program """
        return True

    def do_EOF(self, *arg):
        """ Exit the program """
        return True

    def emptyline(self):
        """ Do nothing when empty line is passed as argument"""
        pass

    def do_create(self, *args):
        """
        create a new instance of BaseModel
        """
        if len(args) < 2:
            print("** class name missing **")
        elif args[1] is not class_name:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel(args)
            new_instance.save()
            print(new_instance.id)

    def do_show(self, *args):
        """Print the string represantation of an instance"""
        if not args:
            print("** class name missing **")
        elif args[1] is not class_name:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[1] + "." + args[2]
            all_objects = models.storage.all()
            if obj_key in all_objects:
                print(all_objects[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, *args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        elif args[1] is not class_name:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[1] + '.' + args[2]
            all_objs = models.storage.all()
            if obj_key in all_objs:
                del all_objs[obj_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, *args):
        """print all string representations of instances """
        all_objs = models.storage.all()
        if args and args[1] is not class_name:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj_key in all_objs:
                if not arg or obj_key.split(".")[0] == args[1]:
                    obj_list.append(str(all_objs[obj_key]))
            print(obj_list)

    def do_update(self, *args):
        """Update an instance base on the class name and id"""
        len_args = len(args)
        if len_args < 2:
            print("** class name missing **")
        elif args[1] is not class_name:
            print("** class doesn't exist **")
        elif len_args < 3:
            print("** instance id missing **")
        else:
            obj_key = args[1] + "." + args[2]
            all_objs = models.storage.all()
            if obj_key not in all_objs:
                print("** no instance found **")
            elif len_args < 4:
                print("** attribute name missing **")
            elif len_args < 5:
                print("** value missing **")
            else:
                attr_name = args[3]
                attr_value = args[4]
                obj_instance = all_objs[obj_key]
                setattr(obj_instance, attr_name, attr_value)
                obj_instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
