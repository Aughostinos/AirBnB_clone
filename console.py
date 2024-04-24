#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys
import models
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
        """Prints the string representation of an
        instance based on the class name and id"""
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
        dic_obj = models.storage.all()

        if class_name_id in dic_obj:
            print(dic_obj[class_name_id])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
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
        dic_obj = models.storage.all()

        if class_name_id in dic_obj:
            dic_obj.pop(class_name_id)
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all
        instances based or not on the class name"""
        args = arg.split()
        if len(args) > 0:
            class_name = args[0]
            try:
                cls = globals()[class_name]
            except KeyError:
                print("** class doesn't exist **")
                return
            dic_obj = models.storage.all()
            for key, value in dic_obj.items():
                if isinstance(value, cls):
                    print(value)
        else:
            dic_obj = models.storage.all()
            for key, value in dic_obj.items():
                print(value)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        class_name = args[0]
        class_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]
        try:
            cls = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        class_name_id = '{}.{}'.format(class_name, class_id)
        dic_obj = models.storage.all()

        if class_name_id not in dic_obj:
            print("** no instance found **")
            return
        instance = dic_obj[class_name_id]
        if hasattr(instance, attribute_name) and /
        attribute_name not in ['id', 'created_at', 'updated_at']:
            attr_type = type(getattr(instance, attribute_name, str))
            casted_value = attr_type(attribute_value)
            setattr(instance, attribute_name, casted_value)
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
