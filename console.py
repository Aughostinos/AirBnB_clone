#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """class definition"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'exit the program'
        return True

    def do_EOF(self, arg):
        'end of the file'
        return True

    def emptyline(self):
        'handle empty line input'
        pass

    def do_create(self, arg):
        'create new class'
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            cls = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return
        instance = cls()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]
        try:
            cls = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return
        class_name_id = '{}.{}'.format(class_name, class_id)
        if class_name_id in models.storage.all():
            print(models.storage.all()[class_name_id])
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
