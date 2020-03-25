


from tkinter import *
from random import randrange as rnd, choice


root = Tk()

root.geometry('800x600')

canv = Canvas(root, bg = 'white')

canv.pack(fill = BOTH, expand = 1)
canv.update()

colors = ['red', 'orange', 'yellow', 'green', 'blue']


stroka = ["Счёт:", 0]
schet = canv.create_text(400, 100, text = "stroka", justify = CENTER, font = "Verdana 20")

ball = canv.create_oval(0, 0, 0, 0, fill = "white", width = 0)

def new_ball():
    global x, y, r, x_vector, y_vector, ball, time
    canv.delete(ball)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    x_vector = rnd(-3, 3)
    y_vector = rnd(-3, 3)
    ball = canv.create_oval(x - r, y - r, x + r, y + r, fill = choice(colors), width = 0)
    time = 0
    move_ball()
    root.after(1000, new_ball)

def move_ball():
    global x_vector, y_vector, time, ball
    print(canv.coords(ball)[0], " ", canv.coords(ball)[1], " ", canv.coords(ball)[2], " ", canv.coords(ball)[3], " ", x_vector, " ", y_vector)
    time += 50
    canv.move(ball, x_vector, y_vector)

    if canv.coords(ball)[0] <= 0 or canv.coords(ball)[2] >= 800:
        x_vector = -x_vector
        print("skidysh X")
    if canv.coords(ball)[1] <= 0 or canv.coords(ball)[3] >= 600:
        y_vector = -y_vector
        print("skidysh Y")
    if time <= 1000:
        root.after(50, move_ball())




def click(event):
    global schet
    if ((event.x - x)**2 + (event.y - y)**2)**0.5 <= r:
        stroka[1] += 1
        canv.delete(ball)
        canv.delete(schet)
        schet = canv.create_text(400, 30, text=stroka, justify=CENTER, font="Verdana 20")

new_ball()

canv.bind('<Button-1>', click)

mainloop()