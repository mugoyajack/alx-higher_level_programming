#!/usr/bin/python3
"""class square."""


class Square:
    def __init__(self, size=0):
        """New square initialization
        
        Args:
            size (int): Size of a square
        """
        self.size = size

    def area(self):
        """Return area of a square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """retrives size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value