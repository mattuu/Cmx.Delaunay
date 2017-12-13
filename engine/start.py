class Point:
    def __init___(self, x, y):
        self.X = x
        self.Y = y

    def print(self):
        print(self.X, self.Y)

    X = 0
    Y = 0

POINTS = [{1, 2}, {3, 4}, {}]

for p in POINTS:
    print(p)


p = Point(100, 20)
p.print()