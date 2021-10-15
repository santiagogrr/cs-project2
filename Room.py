from Wall import Wall
from Door import Door
from typing import List
from Area import *

class Room(Area):
  
  def __init__(self, walls):
    self.walls = walls
    Door = False
    if len(walls) < 4:
      raise AssertionError("Not enough walls for a room.")
    for w in walls:
      if w.nbDoors > 0:
        Door = True
    if not Door:
      raise AssertionError("No doors in the room.") 
  walls: List[Wall]


  def add_wall():
    pass

  