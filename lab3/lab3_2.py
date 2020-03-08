from graph import *

windowSize( 1000, 650 )
canvasSize( 1000, 650 )
penColor( 0, 215, 255 )
brushColor( 0, 215, 255 )
rectangle( 0, 0, 1000, 300)
penColor( 0, 50, 180 )
brushColor( 0, 50, 180 )
rectangle( 0, 301, 1000, 450)
penColor( "yellow" )
brushColor( "yellow" )
rectangle( 0, 451, 1000, 650)
penColor( "black" )
brushColor( "white" )
circle( 200, 70, 22 )
circle( 230, 70, 22 )
circle( 180, 92, 22 )
circle( 210, 94, 22 )
circle( 240, 94, 22 )
circle( 260, 70, 22 )
circle( 270, 94, 22 )
penColor( "yellow" )
brushColor( "yellow" )
circle( 900, 90, 60 )
penColor( "black" )
brushColor( 170, 90, 0 )
rectangle( 550, 330, 800, 370 )
polygon([( 800, 330 ), ( 900, 330 ), ( 800, 370), ( 800, 330 ) ])
moveTo( 550, 370)
chetvert_kruga = []
chetvert_kruga.append(( 550, 370 ))
penColor( "black" )
brushColor( 170, 90, 0 )
for x in range( 0, 40 ):
    x += 1
    y = 330 + ( 1600 -  x**2 )**0.5
    chetvert_kruga.append(( 550 - x, y ))
chetvert_kruga.append(( 550, 330 ))
chetvert_kruga.append(( 550, 370 ))
polygon(chetvert_kruga)
penSize(5)
penColor( "black" )
brushColor( "white" )
circle( 820, 345, 10 )
# мачта
penSize(10)
penColor( "black" )
moveTo( 650, 330 )
lineTo( 650, 200 )
# парус
penSize(1)
penColor( "black" )
brushColor( 215, 220, 165 )
polygon([( 654, 330), ( 675, 265), ( 730, 265 ), ( 654, 330 )])
polygon([( 675, 265), ( 730, 265), ( 654, 200 ), ( 675, 265 )])

penSize(8)
penColor( 233, 155, 29 )
moveTo( 180, 620 )
lineTo( 180, 430 )

penSize(1)
penColor( "black" )
brushColor( 244, 81, 81 )
polygon([( 80, 430 ), ( 280, 430 ), ( 184, 385 ), ( 176, 385 ), ( 80, 430 )])
x = 176
y = 385
x1 = 80
y1 = 430
for i in range(3):
    x1 += 25
    line( x, y, x1, y1 )
penColor( 215, 73, 103 )
line( x, y, x, y1 )
x = 184
y = 385
x1 = 280
y1 = 430
penColor( 215, 73, 103 )
line( x, y, x, y1 )
penColor( "black" )
for i in range(3):
    x1 -= 25
    line( x, y, x1, y1 )






run()