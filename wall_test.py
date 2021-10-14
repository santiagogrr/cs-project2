from Wall import Wall
from Room import Room
from typing import List
import unittest

class wall_test(unittest.TestCase):

    def test_good_coordinates_no_errors(self):
        Wall([(0,1),(0,1)])

    def test_error_raised_when_only_one_coordinate(self):
        with self.assertRaises(AssertionError):
            Wall([(0,),(0,)])
    
    def test_error_raised_when_three_coordinates(self):
        with self.assertRaises(AssertionError):
            Wall([(0,1,2),(0,1,2)])
    
    def test_error_raised_when_three_set_of_coordinates(self):
        with self.assertRaises(AssertionError):
            Wall([(0,1),(0,1),(0,1)])
    
    def test_error_raised_when_list_only_have_one_set_of_coordinates(self):
        with self.assertRaises(AssertionError):
            Wall([(0,1)])
    
    #???
    
    if __name__ =='__main__':
        pass