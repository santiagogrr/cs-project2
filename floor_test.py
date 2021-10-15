from Floor import Floor
from typing import List
import unittest


class floor_test(unittest.TestCase):

    def test_contains_at_least_one_area(self):
        floor = Floor()
        self.assertGreaterEqual(floor.nb_area, 1)

    def test_each_floor_has_unique_number(self):
        floor = Floor()
        self.assertEqual(False)

    ##Building test
    def test_new_building_floors_start_at_0(self):
        floor = Floor()
        self.assertGreaterEqual(floor.nb_area, 1)


    if __name__ =='__main__':
        pass