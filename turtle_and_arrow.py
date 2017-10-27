from turtle import *
import random
setup(500, 500)
Screen()
title("turtle and Arrow ")
move = Turtle()

move.speed(1)

ved=Turtle()
t=Turtle()
showturtle()

ved.shape('turtle')
def k1():
    ved.forward(50)
    move.fd(30)

def k2():
    ved.left(45)
    move.goto(ved.xcor(),ved.ycor())
def k3():
    ved.right(45)
    move.goto(ved.xcor(),ved.ycor())
def k4():
    ved.back(45)
    #move.bk(45)
onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")

t.up()
t.goto(random.randrange(600),random.randrange(600))

t.color(0,0,0)
t.up()
t.fd(10)
t.down()
t.begin_fill()
t.circle(100)
t.end_fill()

t.hideturtle()
listen()
mainloop()
