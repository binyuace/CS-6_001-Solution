#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:57:39 2017

@author: king
"""

# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
class Triangle(Shape):
    def __init__(self, base ,height):
                 self.base =float(base)
                 self.height=float(height)
    def area(self):
                 self.area=0.5*self.base*self.height
    def __str__(self):
                 return 'Triangle with base = '+str(self.base)+' and height = '+str(self.height)
    def __eq__(self,other):
                 return type(other)== Triangle and self.base == other.base and self.height == other.height
    
                 
## TO DO: Implement the `Triangle` class,  which also extends `Shape`.

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.



class ShapeSet():
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.circle = []
        self.square=[]
        self.triangle = [] 
    
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        if type(sh)==Circle and sh not in self.circle:
            self.circle.append(sh)
        if type(sh)==Square and sh not in self.square:
            self.square.append(sh)
        if type(sh)==Triangle and sh not in self.triangle:
            self.triangle.append(sh)
            # print sh, "added to set."
    
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        for i in self.circle:
            yield i
        for i in self.square:
            yield i
        for i in self.triangle:
            yield i
    
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        my_string = ""
        for each in self.circle:
            my_string += str(each) + "\n"
        for each in self.square:
            my_string += str(each) + "\n"
        for each in self.triangle:
            my_string += str(each) + "\n"
        return my_string
    

def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    maximum=0
    theone=()
    for items in shapes:
        if items.area==maximum:
            theone=theone+(items,)
        if items.area>maximum:
            maximum=items.area
            theone=(items,)
    return theone
        
    ## TO DO

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    temp=Shape()
    s=ShapeSet()
    inputfile=open(filename)
    for lines in inputfile:
        lines=lines.split(',')
        if lines[0]=='triangle':
            temp=Triangle(float(lines[1]),float(lines[2]) )
        if lines[0]== 'square':
            temp=Square(float(lines[1]))
        if lines[0]== 'circle':
            temp=Circle(float(lines[1]))
        s.addShape(temp)
    return s
    
f='shapes.txt'
shapeset = readShapesFromFile(f)


        
