from Wall import Wall
from Room import Room
from typing import List
import unittest


class RoomTest(unittest.TestCase):

  def test_room_has_at_least_four_walls(self):
    room = Room([Wall(),Wall(), Wall(),Wall()])
    self.assertGreaterEqual(len(room.walls), 4)



  if __name__ =='__main__':
    pass


