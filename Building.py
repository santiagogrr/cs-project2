from Floor import Floor
from typing import List


class Building(object):

    def __init__(self, floors):
        self.floors = floors
    
    floors: List[Floor]

