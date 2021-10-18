from typing import List
from Coordinate import *

class Door(object):

    def __init__(self, coordinate):
        assert(isinstance(coordinate, Coordinate)), "The coordinate parameter must be a Coordinate"
        assert(len(coordinate) == 1), "The Coordinate element must contain a unique tuple"
        self.coordinate = coordinate

    def get_coordinates(self):
        return self.coordinate.get_list_coordinates()