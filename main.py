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

    # Detect collision at the top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #elif ball.xcord() > 320 or ball.xcor() < -320:

screen.exitonclick()
