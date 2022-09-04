#!/usr/bin/python3
"""Define simple command line interpter
contains the entry point of the command interprete
"""


from ast import arg
import json
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """the class that handles commands
    inherits from cmd class
    """
    # contanins the list of classes used
    __class_list: list = ["BaseModel", "Place", "State", "User", "Amenity", "Review"]

    prompt: str = '(hbnb)'

    def do_help(self, arg: str) -> bool | None:
        """help command that produce help on certain topic"""
        return super().do_help(arg)

    def do_EOF(self, line):
        """EOF command to exit the program
        usage: Ctrl + D"""
        print()
        return True

    def do_quite(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when empty line + Enter
        Override the dafault behaviour, execute the previous command, with "do nothing" """
        pass

    def do_create(self, line):
        """Usage: create BaseModel
        Creates a new instance of BaseModel, saves it to JSON file
        and prints the id of newly created instance
        """
        args = line.split(" ")
        if args[0] == "":
            print("** class name missing **")
        elif args[0] not in __class__.__class_list:
            print("** class doesn't exist **")
        else:
            if args[0] == "BaseModel":
                new_instance = BaseModel()
            elif args[0] == "User":
                new_instance = User()
            elif args[0] == "State":
                new_instance = State()
            elif args[0] == "Amenity":
                new_instance = Amenity()
            elif args[0] == "City":
                new_instance = City()
            elif args[0] == "Place":
                new_instance = Place()
            elif arg[0] == "Review":
                new_instance = Review()
            print(new_instance.id)

    def do_show(self, line):
        """Usage: show <classname>
        Prints the string representation of
        an instance based on the class name and id"""
        args = line.split(" ")
        if args[0] == "":
            print("** class name missing **")
        else:
            if args[0] not in __class__.__class_list:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                all_objects = storage.all()
                for object_id in all_objects.keys():
                    if key == object_id:
                        print(all_objects[object_id])
                        break
                else:
                    print("** no instance found ** ")

    def do_destroy(self, line):
        """Usage destroy BaseModel <id>
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        args = line.split(" ")
        if args[0] == "":
            print("** class name missing **")
        else:
            if args[0] not in __class__.__class_list:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                all_object = storage.all()
                for object_id in all_object.keys():
                    if key == object_id:
                        del all_object[object_id]
                        break
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """Usage all <classname>
        Prints all string representation of all instances
        based or not on the class name.
        """
        args = line.split(" ")
        if args[0] == "" or args[0] in __class__.__class_list:
            object_list = []
            all_objects = storage.all()
            for object_key in all_objects.keys():
                if args[0] or object_key.split(".")[0] == args[0]:
                    object_list.append(str(all_objects[object_key]))
            print(object_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Usage: update <class name> <id> <attribute name> "<attribute value>
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        args = line.split(" ")
        if args[0] == "":
            print("** class name missing **")
        elif not args[0] in __class__.__class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** istance id is missing **")
        else:
            key = args[0] + "." + args[1]
            all_objects = storage.all()
            if key in all_objects.keys():
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(storage.all()[key], args[2], args[3])
                    storage.all()[key].save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
