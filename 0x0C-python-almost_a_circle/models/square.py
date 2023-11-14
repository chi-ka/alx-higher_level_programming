#!/usr/bin/python3
"""Class Base will be the “base” of all other classes in this project"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square based on Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size"""
        return self.height

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer.")
        if value < 0:
            raise ValueError("size must be > 0.")
        self.height = value
        self.width = value

    def __str__(self):
        """Return a string representation of the Square."""
        return(
                """[Square] ({}) {}/{} - {} """.format(
                    self.id, self.x, self.y, self.height
                    )
                )

    def to_dictionary(self):
        """Returns a dictionary object"""
        return {'id': self.id, 'x': self.x, 'size': self.height, 'y': self.y}

    def update(self, *args, **kwargs):
        """Update the Rectangle attributes with the provided arguments."""
        if args and len(args) > 0:
            count = len(args)
            for i in range(count):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if kwargs is not None:
                for key in kwargs:
                    if key == "id":
                        self.id = kwargs[key]
                    if key == "size":
                        self.height = kwargs[key]
                        self.width = kwargs[key]
                    if key == "x":
                        self.x = kwargs[key]
                    if key == "y":
                        self.y = kwargs[key]
