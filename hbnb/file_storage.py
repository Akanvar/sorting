import json
import os.path
import user


class FileStorage:
    """class for storing json files"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj['__class__'] + '.' + obj['id']] = obj

    def save(self):
        json_string = json.dumps(self.__objects)
        with open(self.__file_path, 'w') as file:
            file.write(json_string)

    def reload(self):
        obj_dic = {}
        if self.__file_path and os.path.getsize(self.__file_path) != 0:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
                # for key, value in obj_dic.items():
                #     # class_name, class_id = key.split('.')
                #     # cls = eval(class_name)
                #     instance = user.User()
                #     self.__objects[key] = instance

