from point import Point
import point_generator

points = point_generator.generate(10)
for p in points:
    p.print()
