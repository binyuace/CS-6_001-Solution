#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 13:41:17 2017

@author: king
"""

import ps11
 



a = Position(2,2)

b = RectangularRoom(10,12)

b.cleanTileAtPosition(a)

print b.getNumCleanedTiles()
print b.getNumTiles()
print b.getRandomPosition().getX()