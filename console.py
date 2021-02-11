#!/usr/bin/python3
""" the console """
import cmd


class HBNBCommand(cmd.Cmd):
    """commands"""
    prompt = "(hbnb) "

    def do_quit(self, input):
        """ exit command  """
        exit()

    def do_EOF(self, input):
        """ exit command """
        print()
        return True

    def do_emptyline(self):
        """ empty line """
        pass


    """ HELPS """

    def help_quit(self):
        """ help command """
        print("[USAGE]:  quit")

    def help_EOF(self):
        """ help command """
        print("[USAGE] Ctrl + d")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
