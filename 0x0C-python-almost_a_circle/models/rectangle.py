#!/usr/bin/python3
"""Class Base will be the “base” of all other classes in this project"""


import json
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of a rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """What wee see when we print"""
        return(
                """[Rectangle] ({}) {}/{} - {}/{}""".format(
                    self.id, self.__x, self.__y, self.__width, self.__height
                    )
                 )

    def display(self):
        """prints in stdout the Rectangle with the character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def to_dictionary(self):
        """Returns a dictionary object"""
        return {
                'x': self.__x,
                'width': self.__width,
                'id': self.id,
                'height': self.__height,
                'y': self.__y
                }

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
                )

        with open(filename, 'w') as file:
            file.write(json_string)

    def update(self, *argv, **kwargs):
        """Update the Rectangle attributes with the provided arguments."""
        if argv and len(argv) > 0:
            count = len(argv)
            for i in range(count):
                if i == 0:
                    self.id = argv[0]
                if i == 1:
                    self.__width = argv[1]
                if i == 2:
                    self.__height = argv[2]
                if i == 3:
                    self.__x = argv[3]
                if i == 4:
                    self.__y = argv[4]
        else:
            if kwargs is not None:
                for key in kwargs:
                    if key == "id":
                        self.id = kwargs[key]
                    if key == "height":
                        self.__height = kwargs[key]
                    if key == "width":
                        self.__width = kwargs[key]
                    if key == "x":
                        self.__x = kwargs[key]
                    if key == "y":
                        self.__y = kwargs[key]
