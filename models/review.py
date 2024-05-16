#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review."""

    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    @property
    def place_id(self):
        """Getter for place_id attribute."""
        return self.__place_id

    @place_id.setter
    def place_id(self, value):
        """Setter for place_id attribute."""
        self.__place_id = value

    @property
    def user_id(self):
        """Getter for user_id attribute."""
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id attribute."""
        self.__user_id = value

    @property
    def text(self):
        """Getter for text attribute."""
        return self.__text

    @text.setter
    def text(self, value):
        """Setter for text attribute."""
        self.__text = value
