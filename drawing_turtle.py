import turtle

def draw_square(some_turtle):
    for i in range(1,6):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(1,6):
        some_turtle.forward(200)
        some_turtle.left(120)

def draw_stuff():
    window = turtle.Screen()
    window.bgcolor('purple')
    #Creating steve -draws a square
    steve = turtle.Turtle()
    steve.shape('turtle')
    steve.color('green')
    steve.speed(2)
    draw_square(steve)
    #Creating amelie -draws a square
    amelie = turtle.Turtle()
    amelie.shape('turtle')
    amelie.color('gold')
    amelie.circle(100)
    #creating pinky -draws a triangle    
    pinky = turtle.Turtle()
    pinky.shape('turtle')
    pinky.color('pink')
    draw_triangle(pinky)
    window.exitonclick()

draw_stuff()
