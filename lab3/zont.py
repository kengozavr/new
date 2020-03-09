from graph import *

def zont(x, y, mashtab):
    penSize(4*mashtab)
    penColor( 233, 155, 29 )
    moveTo(x, y)
    lineTo(x, y - 85*mashtab)

    penSize(1)
    penColor( "black" )
    brushColor( 244, 81, 81 )
    polygon([(x - 50*mashtab,y - 85*mashtab), (x + 50*mashtab, y - 85*mashtab), (x + 2*mashtab, y - 107.5*mashtab),
             (x - 2*mashtab, y - 107.5*mashtab), (x - 50*mashtab,y - 85*mashtab)])
    x2 = x - 2*mashtab
    y2 = y - 107.5*mashtab
    x1 = x - 50*mashtab
    y1 = y - 85*mashtab
    delta = (x2 - x1)/4
    for i in range(3):
        x1 += delta
        line( x2, y2, x1, y1 )
    penColor( 215, 73, 103 )
    line( x2, y2, x2, y1 )
    x2 = x + 2*mashtab
    y2 = y - 107.5*mashtab
    x1 = x + 50*mashtab
    y1 = y - 85*mashtab
    penColor( 215, 73, 103 )
    line( x2, y2, x2, y1 )
    penColor( "black" )
    for i in range(3):
        x1 -= delta
        line( x2, y2, x1, y1 )


windowSize( 1000, 650 )
canvasSize( 1000, 650 )
zont(300, 300, 2)
zont(500, 300, 1)
zont(200, 500, 1.5)





run()