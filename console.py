#!/usr/bin/python3
""" the console """
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
classes = {"BaseModel": BaseModel, "User": User}


class HBNBCommand(cmd.Cmd):
    """commands"""
    prompt = "(hbnb) "

    def do_quit(self, input):
        """ exit command  """
        exit()

    def do_EOF(self, input):
        """ exit command """
        print()
        return True

    def do_emptyline(self):
        """ empty line """
        pass

    def do_create(self, arg):
        """ Creates a new instance, depending of the class
        saves it (to the JSON file) and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg in classes:
            new_instance = classes[arg]()
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")
    
    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        line = parse(arg)
        if line == []:
            print("** class name missing **")
        elif line[0] in classes:
            if len(line) == 1:
                print("** instance id missing **")
            if len(line) == 2:
                try:
                    all_objs = storage.all()
                    key = line[0] + "." + line[1]
                    obj = all_objs[key]
                    print(obj)
                except KeyError:
                    print("** class doesn't exist **")
    
    def do_delete(self, arg):
        """Deletes an instance based on the class name and id"""


def parse(arg):
    """Convert a series of zero or more numbers to an
    argument list"""
    return list(map(str, arg.split()))


    """ HELPS """

    def help_quit(self):
        """ help command """
        print("[USAGE]:  quit")

    def help_EOF(self):
        """ help command """
        print("[USAGE] Ctrl + d")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
