from typing import List
import unittest

class Element():
    def __init__(self, coordinate):
        pass 

class mock_element(Element):
    def __init__(self, coordinates):
        assert len(coordinates) > 0, "Element has no coordinates."
        self.coordinates=coordinates

class element_test(unittest.TestCase):

    def test_element_at_least_one_coordinate(self):
        elt = mock_element([(0,0)])
        self.assertEqual(elt.coordinates, [(0,0)])


    def test_element_raises_error_when_no_coordinate(self):
        with self.assertRaises(AssertionError):
            elt = mock_element([])

    if __name__ =='__main__':
        pass