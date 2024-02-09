import cmd
import __init__
import user


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        elif line != "User":
            print("** class doesn't exist **")
        else:
            new_instance = user.User()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
         based on the class name and id
         """
        store = {}
        content = line.split()
        if len(content) < 1:
            print("** class name missing **")
        elif content[0] != "User":
            print("** class doesn't exist **")
        elif len(content) < 2:
            print("** instance id missing **")
        else:
            class_name, instance_id = line.split()
            __init__.storage.reload()
            store = __init__.storage.all()
            if class_name + '.' + instance_id in store.keys():
                print(store[class_name + '.' + instance_id])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on `class name` and `id`"""
        store = {}
        content = line.split()
        if len(content) < 1:
            print("** class name missing **")
        elif content[0] != "User":
            print("** class doesn't exist **")
        elif len(content) < 2:
            print("** instance id missing **")
        else:
            class_name, instance_id = line.split()
            __init__.storage.reload()
            store = __init__.storage.all()
            if class_name + '.' + instance_id in store.keys():
                del store[class_name + '.' + instance_id]
                __init__.storage.save()
            else:
                print("** no instance found **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        store = {}
        content = line.split()
        if len(content) < 1:
            print("** class name missing **")
        elif len(content) == 1:
            print("** instance id missing **")
        elif len(content) == 2:
            print("** attribute name missing **")
        elif len(content) == 3:
            print("** value missing **")
        elif content[0] != "User":
            print("** class doesn't exist **")
        else:
            class_name, instance_id, attribute_name, attribute_value = content[0], content[1], content[2], content[3]
            __init__.storage.reload()
            store = __init__.storage.all()
            if class_name + '.' + instance_id in store.keys():
                store[class_name + '.' + instance_id][attribute_name] = attribute_value
                __init__.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        content = line.split()
        if len(content) == 1 and content[0] != "User":
            print("** class doesn't exist **")
        else:
            print(str(__init__.storage.all()))

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

