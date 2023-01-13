from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(x=0, y=270)
        self.count = 0
        self.display()
        self.color("white")

    def display(self):
        self.clear()
        self.write(f"Score: {self.count}", move=False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.count += 1
        self.display()

    def over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
