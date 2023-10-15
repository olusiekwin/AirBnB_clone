#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import models, storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of a valid Class and print its id\n"""
        if not arg:
            print("** class name missing **")
            return
        
        class_name = arg.split()[0]
        if class_name not in models:
            print("** class doesn't exist **")
            return

        try:
            new_instance = models[class_name]()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Show the string representation of an instance\n"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]
        all_objects = storage.all()

        key = "{}.{}".format(class_name, instance_id)
        instance = all_objects.get(key, None)

        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """Delete an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]
        all_objects = storage.all()

        key = "{}.{}".format(class_name, instance_id)
        instance = all_objects.get(key, None)

        if not instance:
            print("** no instance found **")
        else:
            del all_objects[key]
            storage.save()

    def do_all(self, arg):
        """Show all instances or instances of a specific class\n"""
        class_name = arg if arg else None
        all_objects = storage.all()
        result = []

        if class_name:
            if class_name in models:
                for key, instance in all_objects.items():
                    if key.startswith(class_name + "."):
                        result.append(str(instance))
            else:
                print("** class doesn't exist **")
                return
        else:
            for instance in all_objects.values():
                result.append(str(instance))

        print(result)

    def do_update(self, arg):
        """Update an instance's attribute\n"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]
        all_objects = storage.all()

        key = "{}.{}".format(class_name, instance_id)
        instance = all_objects.get(key, None)

        if not instance:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name, attr_value = args[2], args[3]

        if hasattr(instance, attr_name):
            attr_value = eval(attr_value)
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            # print("** attribute doesn't exist **")
            attr_value = eval(attr_value)
            setattr(instance, attr_name, attr_value)
            instance.save()

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
