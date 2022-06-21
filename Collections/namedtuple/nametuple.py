from collections import namedtuple

# Create a nametuple type, Point
Point = namedtuple("Point", ['x', 'y'])

#Check if its a tuple
print(issubclass(Point, tuple))

#Instantiate the new type
point = Point(2, 4)

