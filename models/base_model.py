import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel instance with provided arguments or create a new instance with unique id and current datetime as created_at.

        Args:
        *args: Not used.
        **kwargs: Attribute-value pairs to initialize the instance.
        """
        if kwargs:
            # Set each attribute value in kwargs as the instance's attribute.
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            
            # Convert created_at and updated_at string to datetime object.
            self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            # Create new instance with unique id and current datetime as created_at.
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.

        Returns:
        dict: Dictionary with all instance attributes and their values.
        """
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr
