import json
import os.path
import user


class FileStorage:
    """class for storing json files"""
    __file_path = "file.json"
    __objects = {}
    user_info = {}

    def all(self):
        self.reload()
        return self.user_info

    def new(self, obj):
        self.__objects[obj['__class__'] + '.' + obj['id']] = obj

    def save(self):
        if self.__file_path and os.path.getsize(self.__file_path) != 0:
            with open(self.__file_path, 'r') as file:
                current_data = json.load(file)
        else:
            current_data = {}

        current_data.update(self.__objects)
        json_string = json.dumps(current_data)
        with open(self.__file_path, 'w') as file:
            file.write(json_string)

    def reload(self):
        self.user_info = self.__objects.copy()
        if self.__file_path and os.path.getsize(self.__file_path) != 0:
            with open(self.__file_path, 'r') as file:
                obj_dic = json.load(file)
                for key, value in obj_dic.items():
                    instance = user.User(**value)
                    self.user_info[key] = instance
                    # print(f"This is {self.__objects}")

