from Area import Area
from Floor import Floor
from Wall import Wall
from Door import Door
from typing import List
import unittest

class mock_area(Area):
    def __init__(self, floor, wall=[]):
        super().__init__(floor, wall)

class area_test(unittest.TestCase):

    def test_unique_floor_ok(self):
        Area(Floor(), wall=[Wall([(0,1), (0,2)], [Door()])])
    
    def test_error_when_no_unique_floor(self):
        floor1 = Floor()
        floor2 = Floor()
        with self.assertRaises(AssertionError):
            Area(floor=[floor1, floor2])

    def test_area_one_wall_ok(self):
        area = mock_area(floor=Floor(), wall=[Wall([(0,1), (0,2)], [Door()])])
        self.assertTrue(area.nbWalls == 1)

    def test_area_no_wall_error(self):
        with self.assertRaises(AssertionError):
            area = mock_area(floor=Floor())
    
    def test_area_one_door_ok(self):
        area = mock_area(floor=Floor(), wall=[Wall([(0,1), (0,2)], [Door()])])
        nbdoors = 0
        for w in area.walls:
            nbdoors += w.nbDoors 
        self.assertTrue(nbdoors > 0)
    
    def test_area_no_door_error(self):
        with self.assertRaises(AssertionError):
            mock_area(floor=Floor(), wall=[Wall([(0,1), (0,2)], [])])

    if __name__ =='__main__':
        pass