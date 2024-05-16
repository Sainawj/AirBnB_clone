#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user."""

    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    @property
    def email(self):
        """Getter for email attribute."""
        return self.__email

    @email.setter
    def email(self, value):
        """Setter for email attribute."""
        self.__email = value

    @property
    def password(self):
        """Getter for password attribute."""
        return self.__password

    @password.setter
    def password(self, value):
        """Setter for password attribute."""
        self.__password = value

    @property
    def first_name(self):
        """Getter for first_name attribute."""
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        """Setter for first_name attribute."""
        self.__first_name = value

    @property
    def last_name(self):
        """Getter for last_name attribute."""
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """Setter for last_name attribute."""
        self.__last_name = value
