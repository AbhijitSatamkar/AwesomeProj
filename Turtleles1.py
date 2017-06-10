import turtle

def square(sqlen):
    for i in range(0,4):
        sqlen.forward(100)
        sqlen.right(90)


def shape():
    sqcir=turtle.Screen()
    sqcir.bgcolor("red")

    sq=turtle.Turtle()
    sq.color("yellow")
    sq.speed(2)
    sq.shape('turtle')
    for i in range(0,24):
       square(sq)
       sq.left(15)
    sqcir.exitonclick()

shape()