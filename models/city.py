#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city."""

    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

    @property
    def state_id(self):
        """Getter for state_id attribute."""
        return self.__state_id

    @state_id.setter
    def state_id(self, value):
        """Setter for state_id attribute."""
        self.__state_id = value

    @property
    def name(self):
        """Getter for name attribute."""
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for name attribute."""
        self.__name = value
