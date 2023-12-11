#!/usr/bin/python3
"""
This module defines the HBNBCommand class,
an interactive command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command Intepreter class.
    """
    prompt = "(hbnb) "
    # Add valid class names as needed
    valid_classes = ["BaseModel"]

    def emptyline(self):
        """
        Called when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it to the JSON file and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the str representation of the instance
        based on the class name and id.
        Usage: show <class name> <id>.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into a JSON file).
        Usage: destroy <class name> <id>
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        # Form the key using the correct instance ID
        key = f"{class_name}.{instance_id}"
        print("Debug: Class Name:", class_name)
        print("Debug: Instance ID:", instance_id)
        print("Debug: Formed Key:", key)
        # Retrieve objects from storage
        dict_objs = storage.all()
        print("Debug: Storage Content:", dict_objs)

        if key in dict_objs:
            del dict_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all str representation of all instances based
        or not on the class name.
        Usage: all [<class name>]
        """
        args = arg.split()
        obj_list = []

        if not args:
            for key, val in storage.all().items():
                obj_list.append(str(val))
        else:
            class_name = args[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return

            for key, value in storage.all().items():
                if key.split('.')[0] == class_name:
                    obj_list.append(str(value))

        print(obj_list)

    def do_update(self, arg):
        """
        Update an instance based on the class name and id by adding
        or updating attribute. (Save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3].strip('"')

        obj = storage.all()[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def do_quit(self, arg):
        """
        Command that exits the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program with EOF (Ctrl+D).
        """
        # print new line before exiting
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
