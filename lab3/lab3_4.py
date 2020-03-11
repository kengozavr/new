from graph import *
import math

def update():
    moveObjectBy(oblako_move[0], 1, 0)
    moveObjectBy(oblako_move[1], 1, 0)
    moveObjectBy(oblako_move[2], 1, 0)
    moveObjectBy(oblako_move[3], 1, 0)
    moveObjectBy(oblako_move[4], 1, 0)
    moveObjectBy(oblako_move[5], 1, 0)
    moveObjectBy(oblako_move[6], 1, 0)

    if xCoord(oblako_move[0]) > 1100:
        moveObjectBy(oblako_move[0], -1300, 0)
        moveObjectBy(oblako_move[1], -1300, 0)
        moveObjectBy(oblako_move[2], -1300, 0)
        moveObjectBy(oblako_move[3], -1300, 0)
        moveObjectBy(oblako_move[4], -1300, 0)
        moveObjectBy(oblako_move[5], -1300, 0)
        moveObjectBy(oblako_move[6], -1300, 0)
def update2():
    moveObjectBy(korabl_move[0], 1, 0)
    moveObjectBy(korabl_move[1], 1, 0)
    moveObjectBy(korabl_move[2], 1, 0)
    moveObjectBy(korabl_move[3], 1, 0)
    moveObjectBy(korabl_move[4], 1, 0)
    moveObjectBy(korabl_move[5], 1, 0)
    moveObjectBy(korabl_move[6], 1, 0)

    if xCoord(korabl_move[0]) > 1100:
        moveObjectBy(korabl_move[0], -1300, 0)
        moveObjectBy(korabl_move[1], -1300, 0)
        moveObjectBy(korabl_move[2], -1300, 0)
        moveObjectBy(korabl_move[3], -1300, 0)
        moveObjectBy(korabl_move[4], -1300, 0)
        moveObjectBy(korabl_move[5], -1300, 0)
        moveObjectBy(korabl_move[6], -1300, 0)


def korabl( x, y, mashtab ):
    penColor( "black" )
    brushColor( 170, 90, 0 )
    # прямоугольник кормы
    l_base = 125
    h_base = 20
    korablik = []
    #1
    korablik.append(rectangle( x, y, x + l_base*mashtab, y + h_base*mashtab))
    #  нос корабля

    l_nose = 50
    #2
    korablik.append(polygon([( x + l_base*mashtab, y ), (x + l_base*mashtab + l_nose*mashtab, y), (x + l_base*mashtab, y + h_base*mashtab), ( x + l_base*mashtab, y )]))
    # задняя часть корабля
    moveTo( x, y + h_base*mashtab)
    chetvert_kruga = []
    chetvert_kruga.append(( x, y + h_base*mashtab ))
    penColor( "black" )
    brushColor( 170, 90, 0 )
    x1 = x
    for x1 in range( 1, int(20 * mashtab) + 1 ):
        y1 = y + ((h_base * mashtab)**2 - x1**2) ** 0.5
        chetvert_kruga.append(( x - x1, y1 ))
    chetvert_kruga.append(( x, y ))
    y1 = y + h_base*mashtab
    chetvert_kruga.append((x, y1))
    #3
    korablik.append(polygon(chetvert_kruga))
    # глаз на носу корабля
    penSize(3 * mashtab)
    penColor( "black" )
    brushColor( "white" )
    #4
    korablik.append(circle(x + 135*mashtab, y + 8*mashtab, 5*mashtab))
    # мачта
    penSize(5*mashtab)
    penColor( "black" )
    moveTo(x + 50*mashtab, y)
    #5
    korablik.append(lineTo(x + 50*mashtab, y-65*mashtab))
    # парус
    penSize(1)
    penColor( "black" )
    brushColor( 215, 220, 165 )
    #polygon([( 654, 330), ( 676, 265), ( 730, 265 ), ( 654, 330 )])
    #6
    korablik.append(polygon([(x + 52*mashtab, y), (x + 62.5*mashtab, y - 32.5*mashtab), (x + 90*mashtab, y - 32.5*mashtab), (x + 52*mashtab, y)]))
    #7
    korablik.append(polygon([(x + 62.5*mashtab, y - 32.5*mashtab), (x + 90*mashtab, y - 32.5*mashtab), ( x + 52*mashtab, y - 65*mashtab ), (x + 62.5*mashtab, y - 32.5*mashtab)]))
    return korablik

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
    return polygon(oval)
def oblaka(x,y,r1,r2):
    x1 = x
    y1 = y
    oblako = []
    oblako.append(oval(x1,y1,r1,r2))
    x1 = x1 + 30
    oblako.append(oval(x1, y1, r1, r2))
    x1 = x1 - 50
    y1 = y1 + 22
    oblako.append(oval(x1, y1, r1, r2))
    x1 = x1 + 30
    y1 = y1 + 2
    oblako.append(oval(x1, y1, r1, r2))
    x1 = x1 + 30
    oblako.append(oval(x1, y1, r1, r2))
    x1 = x1 + 20
    y1 = y1 - 24
    oblako.append(oval(x1, y1, r1, r2))
    x1 = x1 + 10
    y1 = y1 + 24
    oblako.append(oval(x1, y1, r1, r2))
    return oblako
def zub_sun( x, y, r1, r2 ):
    oval = []
    ugol = 0
    for i in range(72):
        x1 = r1 * math.cos(math.radians(ugol))
        y1 = r1 * math.sin(math.radians(ugol))
        oval.append((x + x1, y + y1))
        ugol += 2.5
        x1 = r2 * math.cos(math.radians(ugol))
        y1 = r2 * math.sin(math.radians(ugol))
        oval.append((x + x1, y + y1))
        ugol += 2.5
    polygon(oval)
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
penColor( 0, 215, 255 )
brushColor( 0, 215, 255 )
rectangle( 0, 0, 1000, 300)
penColor( 0, 50, 180 )
brushColor( 0, 50, 180 )
rectangle( 0, 301, 1000, 470)

# Песок

penColor( "yellow" )
brushColor( "yellow" )
sinusoida = []
for x in range(1001):
    y = 10 * math.sin(x/15)
    sinusoida.append(( x, 451 - y))
sinusoida.append(( 1000, 650))
sinusoida.append(( 0, 650))
sinusoida.append(( 0, 451))
polygon(sinusoida)

# Облака
oblaka( 200, 70, 22, 22 )
oblaka( 470, 60, 30, 30 )
oblako_move = oblaka( 150, 200, 34, 22 )

# солнце
penColor( "yellow" )
brushColor( "yellow" )
zub_sun( 900, 90, 60, 75 )

# кораблик

korabl_move = korabl( 250, 310, 1)
korabl( 550, 330, 2)

# зонтик
zont(180, 620, 2)
zont(360, 600, 1)

onTimer(update, 50)
onTimer(update2, 150)






run()