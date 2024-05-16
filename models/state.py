#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state."""

    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
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
