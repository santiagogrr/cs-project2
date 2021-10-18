from typing import List


class Element(object):

    def __init__(self, coordinates):
        assert len(coordinates) > 0, "Element has no coordinates."
        self.coordinates=coordinates