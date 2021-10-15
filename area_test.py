from Area import Area
from Floor import Floor
from typing import List
import unittest


class area_test(unittest.TestCase):

    def test_unique_floor_ok(self):
        Area(Floor())
    
    def test_error_when_no_unique_floor(self):
        floor1 = Floor()
        floor2 = Floor()
        with self.assertRaises(AssertionError):
            Area(floor=[floor1, floor2])



    if __name__ =='__main__':
        pass