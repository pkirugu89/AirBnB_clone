#!/usr/bin/python3
"""
This module defines the HBNBCommand class
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command Intepreter class.
    """
    prompt = "(hbnb) "

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
