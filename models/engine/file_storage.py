#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents an abstracted storage engine."""

    def __init__(self):
        """Initialize FileStorage instance."""
        self._file_path = "file.json"
        self._objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return self._objects

    def new(self, obj):
        """Set obj in the objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self._objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        serialized_objects = {key: obj.to_dict() for key, obj in self._objects.items()}
        with open(self._file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file to objects."""
        try:
            with open(self._file_path) as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    self.new(eval(class_name)(**obj_data))
        except FileNotFoundError:
            pass
