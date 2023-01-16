#!/usr/bin/python3
"""Class rectangle"""


class Rectangle:
    """class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of width and heigth

        Args:
            width (int): width of the rectangle
            height (int): Height of the rectangle

         """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrives width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrives height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if self.__height != 0 and self.__height != 0:
            return self.__height * 2 + 2 * self.__width
        else:
            return 0

    def __str__(self):
        """Print rect with #"""
        if self.__height != 0 and self.__height != 0:
            rect = []
            for i in range(self.__height):
                [rect.append(str(self.print_symbol))
                    for j in range(self.__width)]
                if i != self.__height - 1:
                    rect.append("\n")
            return ("".join(rect))
        else:
            return ""

    def __repr__(self):
        """Return string representation of rect
            to be able to recreate a new instancw using eval().
        """

        return ("Rectangle(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        """Print msg on deletion of any instance of rect"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
