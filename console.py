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

    classes = {
        'Amenity': Amenity,
        'BaseModel': BaseModel,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
    }

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

        args = arg.split()
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objs = storage.all()
        instance_id = args[1]
        instance_key = "{}.{}".format(class_name, instance_id)

        if instance_key in objs:
            print(objs[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objs = storage.all()
        instance_id = args[1]
        instance_key = "{}.{}".format(class_name, instance_id)

        if instance_key in objs:
            del objs[instance_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        objs = storage.all()
        instance_list = []

        if not arg:
            for instance_key in objs:
                instance_list.append(str(objs[instance_key]))
        else:
            class_name = arg.split()[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return

            for instance_key in objs:
                if instance_key.split('.')[0] == class_name:
                    instance_list.append(str(objs[instance_key]))

        print(instance_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objs = storage.all()
        instance_id = args[1]
        instance_key = "{}.{}".format(class_name, instance_id)

        if instance_key not in objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        if attribute_name == "id" or attribute_name == "created_at" or attribute_name == "updated_at":
            return

        instance = objs[instance_key]
        setattr(instance, attribute_name, attribute_value)
        storage.save()

    def default(self, line):
        """
        Default behavior for unknown commands.
        Implements the <class name>.<command>(<args>) syntax.
        """
        args = line.split('.')
        if len(args) >= 2:
            class_name = args[0]
            command_args = args[1].split('(')
            command = command_args[0]
            args = command_args[1].replace(')', '').split(',')

            if class_name in self.classes:
                if command == 'all':
                    self.do_all(class_name)
                elif command == 'count':
                    count = sum(
                        1 for key in storage.all() if key.split('.')[0] == class_name)
                    print(count)
                elif command == 'show':
                    if len(args) == 1:
                        self.do_show(class_name + ' ' + args[0])
                elif command == 'destroy':
                    if len(args) == 1:
                        self.do_destroy(class_name + ' ' + args[0])
                elif command == 'update':
                    if len(args) >= 2:
                        instance_id = args[0].strip().replace('\"', '')
                        attribute_name = args[1].strip().replace('\"', '')
                        attribute_value = args[2].strip().replace('\"', '')
                        self.do_update(
                            class_name + ' ' + instance_id + ' ' + attribute_name + ' ' + attribute_value)

    def do_user(self, arg):
        """Command for User class"""
        self.default('User.' + arg)

    def do_amenity(self, arg):
        """Command for Amenity class"""
        self.default('Amenity.' + arg)

    def do_base_model(self, arg):
        """Command for BaseModel class"""
        self.default('BaseModel.' + arg)

    def do_city(self, arg):
        """Command for City class"""
        self.default('City.' + arg)

    def do_place(self, arg):
        """Command for Place class"""
        self.default('Place.' + arg)

    def do_review(self, arg):
        """Command for Review class"""
        self.default('Review.' + arg)

    def do_state(self, arg):
        """Command for State class"""
        self.default('State.' + arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
