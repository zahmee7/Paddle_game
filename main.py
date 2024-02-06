from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()

screen.listen()
screen.title("Day 22 of code")
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)


ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down,"s")

game_is_on = True

scoreboard = Scoreboard()
while game_is_on:
    screen.update()
    time.sleep(ball.time_speed)
    ball.move()

    if ball.ycor() <-280 or ball.ycor() > 280  :
        ball.bounce()

    if ball.distance(r_paddle)<50 and ball.xcor() >325 or ball.distance(l_paddle)<50 and ball.xcor() >-325 :
        ball.bounce_paddle()



    if ball.xcor() > 400:
        ball.reset_ball()


    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_increase_score()






screen.exitonclick()