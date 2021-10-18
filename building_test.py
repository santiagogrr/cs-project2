from Building import Building
from Floor import Floor
from typing import List
import unittest


class building_test(unittest.TestCase):

    ##Building test
    def test_building_has_floors(self):
        building = Building([Floor(), Floor()])
        self.assertGreater(len(building.floors), 0)
    
    def test_new_building_floors_start_at_0(self):
        building = Building([Floor()])
        self.assertEqual(building.floors[0].floor_id, 0)

    def test_each_floor_has_unique_number(self):
        building = Building([Floor(), Floor()])
        flag = False
        for elem in building.floors:
            if building.floors.count(elem.floor_id) > 1:
                flag = True
            else:
                flag = False
        self.assertEqual(flag, False)

    def test_error_raised_when_no_floors(self):
        with self.assertRaises(AssertionError):
            Building([])



    if __name__ =='__main__':
        pass