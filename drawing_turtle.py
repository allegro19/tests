import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor('purple')
# customising my turtle

    steve = turtle.Turtle()
    steve.shape('turtle')
    steve.color('green')
    steve.speed(2)
#making my turtle move
    line = 4
    while line>=0:
        steve.forward(200)
        steve.right(90)
        line=line-1
        
    amelie = turtle.Turtle()
    amelie.shape('turtle')
    amelie.color('gold')
    amelie.circle(100)
    
    pinky = turtle.Turtle()
    pinky.shape('turtle')
    pinky.color('pink')
    line =4
    while line>=0:
        pinky.forward(200)
        pinky.left(120)
        line = line-1
    window.exitonclick()

draw_square()
