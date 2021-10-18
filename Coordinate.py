class Coordinate(object):  
  
  def __init__(self, list_of_coordinates):
    assert(isinstance(list_of_coordinates, list)), "Coordinates must be a list"
    assert len(list_of_coordinates) <= 2 and len(list_of_coordinates) >= 1, 'There must be one or two tuples in the list'
    assert len(list_of_coordinates[0]) == 2 and isinstance(list_of_coordinates[0], tuple), 'First coordinate must be a tuple'
    if len(list_of_coordinates) == 2:
      assert(list_of_coordinates[1] != list_of_coordinates[0]), "Two coordinates must be different."
      assert len(list_of_coordinates[1]) == 2 and isinstance(list_of_coordinates[1], tuple), 'Second coordinate must be a tuple'
    self.list_of_coordinates = list_of_coordinates


  def __len__(self):
    return len(self.list_of_coordinates)

  def get_list_coordinates(self):
    return self.list_of_coordinates