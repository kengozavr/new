import tkinter as tk
from random import choice, randint

class Ball:
    def __init__(self):
        self.r = randint(30, 50)
        self.x = randint(self.r, 800 - self.r)
        self.y = randint(self.r, 600 - self.r)

        self.x_vector = randint(-3, 3)
        self.y_vector = randint(-3, 3)
        self.flag_ball = 1
        self.time = 0
        self.ball_n = canvas.create_oval(self.x - self.r, self.y - self.r,
                                    self.x + self.r, self.y + self.r,
                                    fill=choice(colors))

    def move(self):
        self.x += self.x_vector
        self.y += self.y_vector
        if self.flag_ball:
            if (self.x - self.r) <= 0 or (self.x + self.r) >= 800:
                self.x_vector = -self.x_vector
        if self.flag_ball:
            if (self.y - self.r) <= 0 or (self.y + self.r) >= 600:
                self.y_vector = -self.y_vector

    def show(self):
        canvas.move(self.ball_n, self.x_vector, self.y_vector)



def click(event):
    global schet, flag_ball

    if ((event.x - ball.x)**2 + (event.y - ball.y)**2)**0.5 <= ball.r:
        stroka[1] += 1
        canvas.delete(ball.ball_n)
        ball.flag_ball = 0
        flag_ball = 0
        canvas.delete(schet)
        schet = canvas.create_text(400, 30, text=stroka, justify=tk.CENTER, font="Verdana 20")

def move_ball():
    ball.show()
    ball.move()
    root.after(50, move_ball)


def main():
    global root, canvas, ball, colors, schet

    root = tk.Tk()
    root.geometry("800x600")
    canvas = tk.Canvas(root)
    canvas.pack(fill = tk.BOTH, expand = 1)
    canvas.bind('<Button-1>', click)
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    stroka = ["Счёт:", 0]
    schet = canvas.create_text(400, 30, text = stroka, justify = tk.CENTER, font = "Verdana 20")
    print("poehaly")
    ball = Ball()
    move_ball()

    root.mainloop()



if __name__ == "__main__":
    main()






