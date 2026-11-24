import turtle

screen = turtle.Screen()
screen.setup(800, 650)
screen.title("Fractal Lab")
screen.bgcolor("#101426")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.pensize(2)

tips = []


def branch(size):
    if size < 16:
        tips.append(pen.pos())
        return
    pen.forward(size)
    pen.left(28)
    branch(size * 0.7)
    pen.right(56)
    branch(size * 0.7)
    pen.left(28)
    pen.backward(size)


pen.penup()
pen.goto(0, -260)
pen.setheading(90)
pen.pendown()
branch(110)

# Add decorations here in feature/decor

screen.update()
screen.mainloop()