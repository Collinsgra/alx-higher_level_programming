#!/usr/bin/python3
"""Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize objects"""
        self.id = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width value"""
        return self.__width

    @property
    def height(self):
        """the height"""
        return self.__height

    @property
    def x(self):
        """value of x"""
        return self.__x

    @property
    def y(self):
        """Value of y"""
        return self.__y

    # List of setter functions
    @width.setter
    def width(self, value):
        """value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """sets height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """sets the x value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """sts y value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Def rectangle areas"""
        return self.__height * self.__width

    def display(self):
        """reps rec with # """
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """string class representation"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Assigns an args to each attrib"""

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for g, h in kwargs.items():
                if g == "id":
                    if h is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = h
                elif g == "width":
                    self.width = h
                elif g == "height":
                    self.height = h
                elif g == "x":
                    self.x = h
                elif g == "y":
                    self.y = h

    def to_dictionary(self):
        """Returns Rectangle representation"""

        dict_object = {'id': self.id, 'width': self.__width,
                       'height': self.__height, 'x': self.__x,
                       'y': self.__y}

        return dict_object

