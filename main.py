from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

#
screen = Screen()
turtle = Turtle()


# Screen setup
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

# Initialize paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

# Paddle controls
screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

# Start the game
game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()
