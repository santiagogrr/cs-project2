from Floor import Floor
from typing import List


class Building(object):

    def __init__(self, floors):
        assert(isinstance(floors, list)), "The floors argument must be a list."
        assert all([isinstance(f, Floor) for f in floors]), "Every element in the floor list must be a Floor."
        assert(len(floors) > 0)
        self.floors = floors
        self.floor_counter = -1
        for f in floors :
            f.set_floor_id(self)
    

    def set_counter(self):
        self.floor_counter += 1
        return self.floor_counter
    
