class Wall(object):
  n: int
  nbDoors: int
  x: int
  y: int
  
  def __init__(self, coordinates, nbdoors=0):
    assert(isinstance(coordinates, tuple)), "Coordinates parameter must be a tuple"
    assert len(coordinates) == 2, 'There must be two coordinates'
    self.nbDoors = nbdoors