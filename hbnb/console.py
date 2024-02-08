import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, line):
        """Quit command to exit the program USAGE: <quit>"""
        return True

    def do_EOF(self, line):
        """quits the console USAGE: <ctrl + 'D'>"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

