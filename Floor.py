from Wall import Wall
from typing import List


#TODO : We need to add the number of floors as a static attribute, also we need to be able to reset the nb of floors.
class Floor(object):
    #TODO THIS IS STATIC! Change this (in other classes)!!!
    nb_area: int

    def __init__(self):
        #TODO just keep this, this isn't static (if we delete the thing above)
        self.nb_area = 1
