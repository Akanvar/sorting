from base_model import BaseModel
from datetime import datetime
import __init__


class User(BaseModel):
    """Creates a user class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        # __init__.storage.new(self.to_dict())

    # def save(self):
    #     self.updated_at = datetime.now()
    #     __init__.storage.save()

