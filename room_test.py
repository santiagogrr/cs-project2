from Wall import Wall
from Room import Room
from Door import Door
from typing import List
from Coordinate import *
import unittest


class room_test(unittest.TestCase):

  def test_room_has_at_least_four_walls(self):
    room = Room([Wall([(0,0), (0,0)]),Wall([(0,0), (0,0)], [Door(Coordinate([(0, 0)]))]), Wall([(0,0), (0,0)]),Wall([(0,0), (0,0)])])
    self.assertGreaterEqual(len(room.walls), 4)

  def test_one_wall_has_a_door(self):
    room = Room([Wall([(0,0), (0,0)]),Wall([(0,0), (0,0)]), Wall([(0,0), (0,0)], [Door(Coordinate([(0, 0)]))]),Wall([(0,0), (0,0)])])
    hasDoor = False
    for wall in room.walls:
      if wall.nbDoors > 0:
        hasDoor = True
    self.assertTrue(hasDoor)

  def test_error_raised_when_not_enough_walls(self):
    with self.assertRaises(AssertionError):
      Room([Wall([(0,0), (0,0)]),Wall([(0,0), (0,0)]), Wall([(0,0), (0,0)], [Door(Coordinate([(0, 0)]))])])
  
  def test_error_raised_when_not_enough_doors(self):
    with self.assertRaises(AssertionError):
      Room([Wall([(0,0), (0,0)]),Wall([(0,0), (0,0)]), Wall([(0,0), (0,0)]),Wall([(0,0), (0,0)])])



  if __name__ =='__main__':
    pass


