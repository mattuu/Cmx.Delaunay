from point import Point
import sys

def generate(count):
    return (Point(i*10, i*20) for i in range(count))
