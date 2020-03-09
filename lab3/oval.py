from graph import *

def oval( x, y, r1, r2 ):
    penColor("black")
    brushColor("white")
    oval = []
    x1 = r1
    for i in range( 2*r1 ):
        y1 = (r2**2 - (x1**2*r2**2)/r1**2)**0.5
        oval.append((x - x1, y - y1))
        x1 -= 1
    for i in range( 2*r1 ):
        y1 = (r2**2 - (x1**2*r2**2)/r1**2)**0.5
        oval.append((x - x1, y + y1))
        x1 += 1
    polygon(oval)
oval( 100, 100, 50, 40 )
run()