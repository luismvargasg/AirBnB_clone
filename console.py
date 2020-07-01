#!/usr/bin/python3
"""Module to the program that contains the entry point of the command
interpreter.
"""
import cmd
import sys
import models
import datetime as dt
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """initialization of HBNBCommand console to manage the different
    commands and inputs received through the keyboard.
    """
    list_Class = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Method called when an empty line is entered in response to
        the prompt so it doesn´t repeat the last nonempty command entered.
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id. Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.list_Class:
            print("** class doesn't exist **")
        else:
            new_obj = eval(arg + '()')
            print(new_obj.id)
            models.storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.list_Class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            dir_obj = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in dir_obj.keys():
                print("** no instance found **")
            else:
                print(dir_obj[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.list_Class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            dir_obj = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in dir_obj.keys():
                print("** no instance found **")
            else:
                models.storage.delete(key)

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all.
        """
        if arg not in HBNBCommand.list_Class and len(arg) != 0:
            print("** class doesn't exist **")
        else:
            dir_obj = models.storage.all()
            my_list = []
            for obj_id in dir_obj.keys():
                if dir_obj[obj_id]["__class__"] == arg or len(arg) == 0:
                    string = "[{}] ({}) {}".format(
                        dir_obj[obj_id]["__class__"],
                        dir_obj[obj_id]["id"],
                        dir_obj[obj_id])

                    my_list.append(string)
            print(my_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file). Ex: $ update
        BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
        """
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.list_Class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            dir_obj = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in dir_obj.keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                dir_obj[key].update({args[2]: "{:s}".format(str(args[3]))})
                new_dict = dir_obj[key]
                base_obj = BaseModel(**new_dict)
                base_obj.updated_at = dt.datetime.now()
                models.storage.save()


def parse(arg):
    """Convert a series of zero or more numbers to an argument tuple"""
    return tuple(map(str, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
