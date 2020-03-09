from graph import *


windowSize( 1000, 650 )
canvasSize( 1000, 650 )
penColor( "black" )
brushColor( 170, 90, 0 )
moveTo( 550, 370)
chetvert_kruga = []
chetvert_kruga.append(( 550, 370 ))
penColor( "black" )
brushColor( 170, 90, 0 )
for x in range( 1, 41 ):
    y = 330 + ( 1600 -  x**2 )**0.5
    chetvert_kruga.append(( 550 - x, y ))
chetvert_kruga.append(( 550, 330 ))
chetvert_kruga.append(( 550, 370 ))
polygon(chetvert_kruga)
run()
