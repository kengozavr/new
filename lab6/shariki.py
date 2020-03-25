from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

ball = canv.create_oval(0, 0, 0, 0, fill = "white", width = 0)

def new_ball():
    global x, y, r, ball
    canv.delete(ball)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    x_vector = rnd(-3, 3)
    y_vector = rnd(-3, 3)
    t = 0
    ball = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    while t < 1000:
        t += 50
        print(canv.coords(ball)[0], " ", canv.coords(ball)[1], " ", canv.coords(ball)[2], " ", canv.coords(ball)[3], " ", x_vector, " ", y_vector)
        canv.move(ball, 1, 1)

        if canv.coords(ball)[0] <= 0 or canv.coords(ball)[2] >= 800:
            x_vector = -x_vector
        if canv.coords(ball)[1] <= 0 or canv.coords(ball)[3] >= 600:
            y_vector = -y_vector
        time.sleep(0.05)



    root.after(1000, new_ball)


def click(event):
    print('click')


new_ball()
canv.bind('<Button-1>', click)
mainloop()
