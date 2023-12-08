import uuid
from datetime import datetime


class BaseModel:
    """
    Base model for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Base class constructor.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return "[{}] ({}) {}\
                ".format(self.__class.__name, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dict containing all keys/values of __dict__ of the instance.
        """
        result = self.__dict__.copy()
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        result['__class__'] = self.__class__.__name__
        return result
