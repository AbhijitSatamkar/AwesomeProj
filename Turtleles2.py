import turtle

wall=turtle.Screen()
flower=turtle.Turtle()

def pud(line1):
    line1.color("blue")
    line1.shape('turtle')
    line1.speed(100)
    line1.right(30)
    line1.forward(100)
    line1.right(30)
    line1.forward(100)
    line1.right(150)
    line1.forward(100)
    line1.right(30)
    line1.forward(130)

for i in range(0,36):
    pud(flower)
    flower.right(10)

wall.exitonclick()