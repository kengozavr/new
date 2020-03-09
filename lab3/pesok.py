from graph import *
import math

windowSize(1000, 650)
canvasSize(1000, 650)
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

run()

