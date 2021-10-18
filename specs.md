# Specs

building has coordinates.
each element being a wall or sth else :desc by coord. Also room.
composition : when building destroyed, area & elements deleted.

wall inherits the class element.

Coordinate
* attribute : list of 2-tuples (assert all of that)
* no two tuples are the same


Area : room, patio, corridor

room

* ~~has at least four walls.~~
* ~~at least one wall has at least one door~~
* coordinates : two coordinates
* overlapping coordinates between walls of an area or walls of a building (except if same wall)
* weird coordinates
* each wall must touch two others (one shared coordinate, and not the same two)

Element

* Needs coordinates (x, y)
* coordinates are different per element

Area

* Needs coordinates
* ~~Needs a unique floor (test when no floors)
* ~~At least one wall~~
* ~~At least one door~~
* super().function(self)

* one coordinate should be shared with only one other wall in the area.
* walls should only overlap in one coordinate (nowhere else)

Patios

* doesn't need four walls

Corridor

* Inherits Room.

Floor

* needs a unique number (maybe implement )
* belongs to one building
* can have multiple areas
* needs at least one area
* one area must touch another if there is more than one area.

Door

* Needs only one coordinate

Wall

* ~~Needs only two coordinates~~
* If there's a door, its coordinates must be between the coordinates of the wall.


Building

* at least one floor
* a floor is created first, then added to building. When added, it is assigned a number (starting from 0).
* (later) ability to change number of floor, and delete a floor.