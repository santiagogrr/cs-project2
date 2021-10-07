from Wall import Wall
from typing import List


class Room(object):
  
  def __init__(self, walls):
    self.walls = walls
    if len(walls) < 4:
      raise AssertionError("Not enough walls for a room.")
  
  walls: List[Wall]


  def add_wall():
    pass

  