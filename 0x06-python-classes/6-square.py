#!/usr/bin/python3
"""class square."""


class Square:
    """Class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """New square initialization

        Args:
            size (int): Size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

    def area(self):
        """Return area of a square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """retrives size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrives position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:

            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
