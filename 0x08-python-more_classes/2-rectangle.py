#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """this represents a rectangle"""

    def __init__(self, width=0, height=0):
        """rectangle_class
        Args:
            width: width of a rec
            height: height of a rec
        Raises:
            TypeError: !int
            ValueError: less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """rets width atts"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """rets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

