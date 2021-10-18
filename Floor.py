from Wall import Wall
from typing import List


class Floor(object):

    def __init__(self):
        self.nb_area = 1
        self.floor_id = None
    
    def set_floor_id(self, building):
        self.floor_id = building.set_counter()
