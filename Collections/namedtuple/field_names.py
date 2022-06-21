# nametuple(typename, fields)
from collections import namedtuple

# A list of strings for the field names
Point = namedtuple('Point', ['x', 'y'])
print(Point)
print(Point(2, 3))

# A sting with comma separated for the field names
Point = namedtuple('Point', 'x, y')
print(Point)
print(Point(2, 3))

# A generator expression for the field names
Point = namedtuple('Point', (field for field in 'xy'))
print(Point)
print(Point(2, 3))

# A sett for the field names
Point = namedtuple('Point', {'x', 'y'})
print(Point)
print(Point(2, 3))