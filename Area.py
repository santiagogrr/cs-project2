from Wall import Wall
from typing import List
from Floor import Floor


class Area(object):

    def __init__(self, floor):
        assert(isinstance(floor, Floor)), "The floor parameter must be a Floor object."