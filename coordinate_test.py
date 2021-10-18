from Coordinate import Coordinate
from typing import List
import unittest

class coordinate_test(unittest.TestCase):

    def test_good_coordinates_no_errors(self):
        Coordinate([(0,1),(2,1)])

    def test_error_different_tuples(self):
        coordinate = Coordinate([(0,1), (2,1)])
        self.assertNotEqual(coordinate.list_of_coordinates[0],coordinate.list_of_coordinates[1] )

    def test_error_raised_when_same_coordinates(self):
        with self.assertRaises(AssertionError):
            Coordinate([(2,1), (2,1)])

    
    if __name__ =='__main__':
        pass