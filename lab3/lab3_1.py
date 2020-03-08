from graph import *


penColor("black")
brushColor("yellow")
circle(250, 200, 150)

brushColor("red")
circle(200, 170, 30)
circle(300, 170, 30)
brushColor("black")
circle(200, 170, 10)
circle(300, 170, 10)
penSize(5)

polyline([( 170, 110 ), ( 250, 160 ), ( 330, 110 )])
polyline([( 200, 280 ), ( 250, 250 ), ( 300, 280 )])



run()