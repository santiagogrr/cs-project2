from typing import List
from Door import *
from Coordinate import *
import unittest

class door_test(unittest.TestCase):

    def test_only_one_coordinate_ok(self):
        door = Door(Coordinate([(0,0)]))
        self.assertEqual(door.get_coordinates(), [(0,0)])

    def test_error_when_two_coordinates(self):
        with self.assertRaises(AssertionError):
            Door(Coordinate([(0,0), (0,1)]))

    if __name__ =='__main__':
        pass