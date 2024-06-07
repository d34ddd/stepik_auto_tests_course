import turtle

def draw_rectangle(x, y, widht, height):
    turtle.goto(x, y)
    turtle.pencolor('blue')
    turtle.fillcolor('black')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(widht)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
