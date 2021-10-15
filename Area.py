from Wall import Wall
from typing import List
from Floor import Floor


class Area(object):

    def __init__(self, floor, wall=[]):
        assert(isinstance(floor, Floor)), "The floor parameter must be a Floor object."
        assert(isinstance(wall, list)), "The wall parameter must be a list."
        self.nbWalls = len(wall)
        assert(self.nbWalls > 0), "There must be at least one wall in the Area."
