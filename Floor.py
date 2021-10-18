from Wall import Wall
from typing import List


#TODO : We need to add the number of floors as a static attribute, also we need to be able to reset the nb of floors.
class Floor(object):
    counter = 0

    def __init__(self):
        #TODO just keep this, this isn't static (if we delete the thing above)
        self.nb_area = 1
        self.floor_id = Floor.counter
        Floor.counter += 1
