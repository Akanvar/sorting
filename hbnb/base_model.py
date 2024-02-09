from datetime import datetime
import uuid
import __init__


class BaseModel:
    """creates a base class for the project"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            __init__.storage.new(self.to_dict())

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        __init__.storage.save()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary

