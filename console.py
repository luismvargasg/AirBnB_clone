#!/usr/bin/python3
"""Module to the program that contains the entry point of the command
interpreter.
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """initialization of HBNBCommand console to manage the different
    commands and inputs received through the keyboard.
    """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    do_EOF = do_quit

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
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_obj = BaseModel()
            print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            dir_obj = storage.all()
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
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            dir_obj = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in dir_obj.keys():
                print("** no instance found **")
            else:
                storage.delete(key)

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all.
        """
        if arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            dir_obj = storage.all()
            my_list = []
            for obj_id in dir_obj.keys():
                string = "[{}] ({}) {}".format(
                    dir_obj[obj_id]["__class__"],
                    dir_obj[obj_id]["id"],
                    dir_obj[obj_id])
                my_list.append(string)
            print(my_list)


def parse(arg):
    """Convert a series of zero or more numbers to an argument tuple"""
    return tuple(map(str, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
