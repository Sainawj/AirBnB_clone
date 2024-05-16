#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place."""

    def __init__(self, *args, **kwargs):
        """Initialize Place instance."""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

    @property
    def city_id(self):
        """Getter for city_id attribute."""
        return self.__city_id

    @city_id.setter
    def city_id(self, value):
        """Setter for city_id attribute."""
        self.__city_id = value

    @property
    def user_id(self):
        """Getter for user_id attribute."""
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id attribute."""
        self.__user_id = value

    @property
    def name(self):
        """Getter for name attribute."""
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for name attribute."""
        self.__name = value

    @property
    def description(self):
        """Getter for description attribute."""
        return self.__description

    @description.setter
    def description(self, value):
        """Setter for description attribute."""
        self.__description = value

    @property
    def number_rooms(self):
        """Getter for number_rooms attribute."""
        return self.__number_rooms

    @number_rooms.setter
    def number_rooms(self, value):
        """Setter for number_rooms attribute."""
        self.__number_rooms = value

    @property
    def number_bathrooms(self):
        """Getter for number_bathrooms attribute."""
        return self.__number_bathrooms

    @number_bathrooms.setter
    def number_bathrooms(self, value):
        """Setter for number_bathrooms attribute."""
        self.__number_bathrooms = value

    @property
    def max_guest(self):
        """Getter for max_guest attribute."""
        return self.__max_guest

    @max_guest.setter
    def max_guest(self, value):
        """Setter for max_guest attribute."""
        self.__max_guest = value

    @property
    def price_by_night(self):
        """Getter for price_by_night attribute."""
        return self.__price_by_night

    @price_by_night.setter
    def price_by_night(self, value):
        """Setter for price_by_night attribute."""
        self.__price_by_night = value

    @property
    def latitude(self):
        """Getter for latitude attribute."""
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        """Setter for latitude attribute."""
        self.__latitude = value

    @property
    def longitude(self):
        """Getter for longitude attribute."""
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        """Setter for longitude attribute."""
        self.__longitude = value

    @property
    def amenity_ids(self):
        """Getter for amenity_ids attribute."""
        return self.__amenity_ids

    @amenity_ids.setter
    def amenity_ids(self, value):
        """Setter for amenity_ids attribute."""
        self.__amenity_ids = value
