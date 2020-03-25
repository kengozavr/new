import tkinter as tk
from random import randint, choice

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self):
        self.R = randint(20, 50)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx = randint(-3, 3)
        self.dy = randint(-3, 3)
        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R, fill=choice(colors))

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def canvas_click_handler(event):
    print('Hello World! x=', event.x, 'y=', event.y)


def tick():
    ball.move()
    ball.show()
    root.after(50, tick)


def main():
    global root, canvas, ball, colors, stroka, schet

    root = tk.Tk()
    root.geometry("800x600")
    canvas = tk.Canvas(root)
    canvas.pack(expand = 1, fill=tk.BOTH)
    canvas.bind('<Button-1>', canvas_click_handler)
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    stroka = ["Счёт:", 0]
    schet = canvas.create_text(400, 30, text=stroka, justify=tk.CENTER, font="Verdana 20")
    ball = Ball()
    print("poehali")
    tick()
    root.mainloop()


if __name__ == "__main__":
    main()