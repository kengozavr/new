from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry("800x600")
c = Canvas(root, bg='white')
c.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

ball = c.create_oval(0, 0, 0, 0, fill='white')

flag_ball = 1

stroka = ["Счёт:", 0]
schet = c.create_text(400, 30, text = stroka, justify = CENTER, font = "Verdana 20")

def new_ball():
    global x, y, r, x_vector, y_vector, ball, time, flag_ball
    c.delete(ball)
    print("Sharik delete")
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    x_vector = rnd(-3, 3)
    y_vector = rnd(-3, 3)
    ball = c.create_oval(x - r, y - r, x + r, y + r, fill = choice(colors), width = 0)
    flag_ball = 1
    time = 0
    motion()
    c.bind('<Button-1>', click)
    root.after(1000, new_ball)


def motion():
    global x, y, time, x_vector, y_vector
    time += 50

    c.move(ball, x_vector, y_vector)
    x += x_vector
    y += y_vector
    if flag_ball:
        if c.coords(ball)[0] <= 0 or c.coords(ball)[2] >= 800:
            x_vector = -x_vector

    if flag_ball:
        if c.coords(ball)[1] <= 0 or c.coords(ball)[3] >= 600:
            y_vector = -y_vector

    if time < 1000 and flag_ball:
        root.after(50, motion)
    else:
        new_ball()




def click(event):
    global schet, flag_ball

    if ((event.x - x)**2 + (event.y - y)**2)**0.5 <= r:
        stroka[1] += 1
        c.delete(ball)
        flag_ball = 0
        c.delete(schet)
        schet = c.create_text(400, 30, text=stroka, justify=CENTER, font="Verdana 20")





new_ball()

c.bind('<Button-1>', click)


root.mainloop()
