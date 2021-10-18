class Coordinate(object):  
  
  def __init__(self, list_of_coordinates):
    assert(isinstance(list_of_coordinates, list)), "Coordinates must be a list"
    assert len(list_of_coordinates) == 2, 'There must be two tuples in the list'
    assert len(list_of_coordinates[0]) == 2 and isinstance(list_of_coordinates[0], tuple), 'First coordinate must be a tuple'
    assert len(list_of_coordinates[1]) == 2 and isinstance(list_of_coordinates[1], tuple), 'Second coordinate must be a tuple'
    self.list_of_coordinates = list_of_coordinates