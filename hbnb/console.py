import cmd
from base_model_1 import BaseModel, storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, class_name):
        """Creates a new instance of BaseModel"""

        if not class_name:
            print("** class name missing **")
        elif class_name != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, class_name, class_id):
        """Prints the string representation of an instance
         based on the class name and id
         """
        if not class_name:
            print("** class name missing **")
        elif class_name != "BaseModel":
            print("** class doesn't exist **")
        elif not class_id:
            print("** instance id missing **")
        storage.reload()
        





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

