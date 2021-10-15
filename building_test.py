from Building import Building
from Floor import Floor
from typing import List
import unittest


class building_test(unittest.TestCase):

    ##Building test
    def test_building_has_floors(self):
        building = Building([Floor(), Floor()])
        self.assertGreater(len(building.floors), 1)
    
    def test_new_building_floors_start_at_0(self):
        building = Building([Floor()])
        self.assertEqual(len(building.floors[0]), 0)

    def test_each_floor_has_unique_number(self):
        building = Building([Floor(), Floor()])
        self.assertEqual(len(set(building.floors)), len(building.floors))

    def test_error_raised_when_not_enough_floors(self):
        with self.assertRaises(AssertionError):
            Building(Floor(None))



    if __name__ =='__main__':
        pass