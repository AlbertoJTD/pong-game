from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')

    def move(self):
        x_position = self.xcor() + 10
        y_position = self.ycor() + 10
        self.goto(x_position, y_position)
