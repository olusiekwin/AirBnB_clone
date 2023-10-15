#!/usr/bin/python3
"""
Console DOC
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    allowed_classes = [
        "BaseModel", "User", "State",
        "City", "Amenity", "Place", "Review"
    ]

    def do_quit(self, args):
        """
        Exit the command-line console.
        """
        return True

    def do_EOF(self, args):
        """
        Handle EOF (Ctrl+D) to exit the console.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of a specified class and print its ID.
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return

        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_all(self, arg):
        """
        Print string representations of instances based on the class name.
        """
        if not arg:
            print([str(v) for k, v in models.storage.all().items()])
        else:
            class_name = arg
            if class_name not in self.allowed_classes:
                print("** class doesn't exist **")
                return
            print([str(v) for k, v in models.storage.all().items() if
                   isinstance(v, globals()[class_name])])

    def do_update(self, arg):
        """
        Update an instance based on the class name and ID with a new attribute
        and value.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        attr_name = args[2]
        attr_value = args[3]

        key = "{}.{}".format(class_name, instance_id)
        instances = models.storage.all()
        if key in instances:
            instance = instances[key]
            try:
                attr_value = eval(attr_value)
            except (NameError, SyntaxError):
                pass
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
