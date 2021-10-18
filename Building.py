from Floor import Floor
from typing import List


class Building(object):

    def __init__(self, floors):
        self.floors = floors
    
    floors: List[Floor]


test = Building([Floor(), Floor()])
for element in test.floors:
    print(element.floor_id)

for elem in test.floors:
    if test.floors.count(elem.floor_id) > 1:
        print(True)
    else:
        print(False)