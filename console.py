#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
