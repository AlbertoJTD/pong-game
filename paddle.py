from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xy_position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color('white')
        self.x_position = xy_position[0]
        self.y_position = xy_position[1]
        self.goto(self.x_position, self.y_position)

    def up(self):
        new_y_position = self.ycor() + 20
        self.goto(self.x_position, new_y_position)

    def down(self):
        new_y_position = self.ycor() - 20
        self.goto(self.x_position, new_y_position)