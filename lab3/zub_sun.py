from graph import *
import math


def zub_sun( x, y, r1, r2 ):
    oval = []
    ugol = 0
    for i in range(36):
        x1 = r1 * math.cos(math.radians(ugol))
        y1 = r1 * math.sin(math.radians(ugol))
        oval.append((x + x1, y + y1))
        ugol += 5
        x1 = r2 * math.cos(math.radians(ugol))
        y1 = r2 * math.sin(math.radians(ugol))
        oval.append((x + x1, y + y1))
        ugol += 5
    polygon(oval)


penColor("yellow")
brushColor("yellow")
zub_sun( 150, 100, 60, 75 )

run()