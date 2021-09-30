from Wall import Wall
from Room import Room
from typing import List
import unittest


class RoomTest(unittest.TestCase):

  def test_room_has_at_least_four_walls(self):
    room = Room([Wall(),Wall(), Wall(),Wall()])
    self.assertGreaterEqual(len(room.walls), 4)

  def test_one_wall_has_a_door(self):
    room = Room([Wall(0),Wall(0), Wall(1),Wall(0)])
    hasDoor = False
    for wall in room.walls:
      if wall.nbDoors > 0:
        hasDoor = True
    self.assertTrue(hasDoor)

  def test_error_raised_when_not_enough_walls(self):
    room = Room([Wall(0),Wall(0), Wall(1),Wall(0)])
    hasDoor = False
    for wall in room.walls:
      if wall.nbDoors > 0:
        hasDoor = True
    self.assertTrue(hasDoor)

  if __name__ =='__main__':
    pass


