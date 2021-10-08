# Specs

building has coordinates.
each element being a wall or sth else :desc by coord. Also room.
composition : when building destroyed, area & elements deleted.

wall inherits the class element.

Area : room, patio, corridor

room

* ~~has at least four walls.~~
* ~~at least one wall has at least one door~~ 
* coordinates : two coordinates
* overlapping coordinates between walls of an area or walls of a building (except if same wall)
* weird coordinates

Building

* at least one Area
* at least one floor
* .

Area

* Needs a unique floor
* At least one wall
* At least one door
* super().function(self)

* one coordinate should be shared with only one other wall in the area.
* walls should only overlap in coordinates (nowhere else)

Patios

* doesn't need four walls

Corridor

* l

Floor

* needs a unique number.
* belongs to one building (necessary?)
* can have multiple areas
* needs at least one area