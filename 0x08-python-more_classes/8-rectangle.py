#!/usr/bin/python3

"""Defines a rectangle class."""

class Rectangle:
    """
    Define a rectangle class
    """
    number_of_instances = 0

    def __init__(self, width, height):
        """
        Initialize a rectangle object with given width and height

        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Return a string representation of the rectangle

        Returns:
        str: string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.width, self.height)

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
        int: area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle

        Returns:
        int: perimeter of the rectangle
        """
        return 2 * (self.width + self.height)

    def __del__(self):
        """
        Delete a rectangle instance and decrement number of instances
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

