#!/usr/bin/python3
'''This module defines the Square class, derived from Rectangle.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represents a square shape, inheriting from Rectangle class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes a new Square instance with given parameters.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns a string representation of the Square instance.'''
        return '[{}] ({}) {}/{} - {}'.format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Getter method for the size of the square (width or height).'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter method for the size, updates both width and height.'''
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method to update instance attributes with args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes using positional or keyword args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns a dictionary representation of the Square instance.'''
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
