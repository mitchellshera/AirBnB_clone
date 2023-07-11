#!/usr/bin/python3

"""
This module is the entry point of the command interpreter
It contains the class HBNBCommand
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class contains the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Exit the program """
        return True

    def do_EOF(self, arg):
        """ Exit the program """
        return True

    def emptyline(self):
        """ Do nothing when empty line is passed as argument"""
        pass

    def do_create(self, args):
        """ 


if __name__ == '__main__':
    HBNBCommand().cmdloop()
