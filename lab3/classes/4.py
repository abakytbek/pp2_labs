import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print("Координаты:", self.x, self.y)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)


x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
p1 = Point(x1, y1)

x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))
p2 = Point(x2, y2)

p1.show()
p2.show()

print("Расстояние между точками:", p1.dist(p2))

nx = int(input("Введите новое x1: "))
ny = int(input("Введите новое y1: "))
p1.move(nx, ny)

p1.show()
