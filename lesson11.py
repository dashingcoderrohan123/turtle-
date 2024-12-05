import turtle


screen = turtle.Screen()
screen.bgcolor("blue")  

square_turtle = turtle.Turtle()
square_turtle.speed(2)  


for _ in range(4):
    square_turtle.forward(100)
    square_turtle.left(90)      
square_turtle.hideturtle()
