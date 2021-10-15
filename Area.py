from Wall import Wall
from typing import List
from Floor import Floor


class Area(object):

    def __init__(self, floor, wall=[]):
        assert(isinstance(floor, Floor)), "The floor parameter must be a Floor object."
        assert(isinstance(wall, list)), "The wall parameter must be a list."
        self.nbWalls = len(wall)
        self.walls = wall
        assert(self.nbWalls > 0), "There must be at least one Wall in the Area."
        nbdoors = 0
        for w in self.walls:
            nbdoors += w.nbDoors
            #need class wall to have coordinates
            #w.coordinate
            #assert(False), "Two walls musn't have the same coordinates."
            
        assert(nbdoors > 0), "There must be at least one Wall with at least one Door in the Area."

            