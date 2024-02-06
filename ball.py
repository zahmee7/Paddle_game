from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("normal")
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xcor_move = 10
        self.ycor_move = 10
        self.time_speed = 0.1


    def reset_ball(self):
        self.goto(0,0)
        self.bounce_paddle()
        self.time_speed = 0.1
    def move_after_l_gole(self):
        self.xcor_move *= 1
    def move(self):
        new_y = self.ycor() + self.ycor_move
        new_x = self.xcor() + self.xcor_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.ycor_move *= -1

    def bounce_paddle(self):
        self.xcor_move *= -1
        self.time_speed *=0.9


