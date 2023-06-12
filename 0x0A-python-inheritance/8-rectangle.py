#!/usr/bin/python3
"""Gets baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """def rectangles"""

    def __init__(self, width, height):
        """Initialize a new Rect
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
