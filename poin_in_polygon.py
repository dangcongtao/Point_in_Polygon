from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

point = Point(2, 2)
polygon = Polygon([(0, 0), (0, 1), (0, 10), (0, 20)])
print(polygon.contains(point))