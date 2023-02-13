import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self, x, y):
        self.x += x
        self.y += y
    def dist(self, p2):
        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

point1 = Point(1, 2)
print(point1.show())
point1.move(0, 10)
print(point1.show())
point2 = Point(5, 6)
print(point1.dist(point2))
    