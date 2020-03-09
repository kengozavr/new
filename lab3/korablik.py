from graph import *
import math


def korabl( x, y, mashtab ):
    penColor( "black" )
    brushColor( 170, 90, 0 )
    # прямоугольник кормы
    l_base = 125
    h_base = 20
    #rectangle( 550, 330, 800, 370 )
    rectangle( x, y, x + l_base*mashtab, y + h_base*mashtab)
    #  нос корабля
    #polygon([( 800, 330 ), ( 900, 330 ), ( 800, 370), ( 800, 330 ) ])
    l_nose = 50
    polygon([( x + l_base*mashtab, y ), (x + l_base*mashtab + l_nose*mashtab, y), (x + l_base*mashtab, y + h_base*mashtab), ( x + l_base*mashtab, y )])
    # задняя часть корабля
    moveTo( x, y + h_base*mashtab)
    chetvert_kruga = []
    chetvert_kruga.append(( x, y + h_base*mashtab ))
    print(x, y + h_base*mashtab)
    penColor( "black" )
    brushColor( 170, 90, 0 )
    x1 = x
    for x1 in range( 1, int(20 * mashtab) + 1 ):
        y1 = y + ((h_base * mashtab)**2 - x1**2) ** 0.5
        print( x - x1, y1 )
        chetvert_kruga.append(( x - x1, y1 ))
    chetvert_kruga.append(( x, y ))
    y1 = y + h_base*mashtab
    chetvert_kruga.append((x, y1))
    polygon(chetvert_kruga)
    # глаз на носу корабля
    penSize(3 * mashtab)
    penColor( "black" )
    brushColor( "white" )
    circle(x + 135*mashtab, y + 8*mashtab, 5*mashtab)
    # мачта
    penSize(5*mashtab)
    penColor( "black" )
    moveTo(x + 50*mashtab, y)
    lineTo(x + 50*mashtab, y-65*mashtab)
    # парус
    penSize(1)
    penColor( "black" )
    brushColor( 215, 220, 165 )
    #polygon([( 654, 330), ( 676, 265), ( 730, 265 ), ( 654, 330 )])
    polygon([(x + 52*mashtab, y), (x + 62.5*mashtab, y - 32.5*mashtab), (x + 90*mashtab, y - 32.5*mashtab), (x + 52*mashtab, y)])
    polygon([(x + 62.5*mashtab, y - 32.5*mashtab), (x + 90*mashtab, y - 32.5*mashtab), ( x + 52*mashtab, y - 65*mashtab ), (x + 62.5*mashtab, y - 32.5*mashtab)])
windowSize( 1000, 650 )
canvasSize( 1000, 650 )
korabl( 550, 330, 2)
korabl( 100, 150, 1)
korabl (300, 400, 1.5)
run()