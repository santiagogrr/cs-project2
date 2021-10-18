from Door import Door
from Coordinate import *
class Wall(object):
  
  
  def __init__(self, list_of_coordinates, door_list=[]):
    #TODO : door list must be implemented
    assert(isinstance(list_of_coordinates, list)), "Coordinates parameter must be a list"
    assert len(list_of_coordinates) == 2, 'There must be two set of coordinates'
    assert len(list_of_coordinates[0]) == 2 and isinstance(list_of_coordinates[0], tuple), 'First coordinate must be a tuple'
    assert len(list_of_coordinates[1]) == 2 and isinstance(list_of_coordinates[1], tuple), 'Second coordinate must be a tuple'
    self.door_list = door_list
    self.nbDoors = len(door_list)