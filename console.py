#!/usr/bin/python3
""" the console """
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place

classes = {"BaseModel": BaseModel, "User": User, "City": City, "State": State,
           "Amenity": Amenity, "Review": Review, "Place": Place}

def parse(arg):
    """Convert a series of zero or more numbers to an
    argument list"""
    return list(map(str, arg.split()))

class HBNBCommand(cmd.Cmd):
    """commands"""
    prompt = '(hbnb) '

    def do_quit(self, input):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, input):
        """ exit command """
        print()
        return True

    def emptyline(self):
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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = parse(arg)
        if args == []:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = parse(arg)
        obj_list = []
        obj_dict = storage.all()
        if args == []:
            for obj in obj_dict.values():
                print(obj)
        elif args[0] in classes:
            for keys in obj_dict:
                key = keys.split(".")[0]
                if key == args[0]:
                    print(obj_dict[keys])
        else:
            print("** class doesn't exist **")
            return False

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = parse(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except ValueError:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except ValueError:
                                        args[3] = 0.0
                            setattr(storage.all()[k], args[2], args[3])
                            storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    """main loop for console"""
    HBNBCommand().cmdloop()
