#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represents an amenity."""
    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""

    @property
    def name(self):
        """Getter for name attribute."""
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for name attribute."""
        self.__name = value
