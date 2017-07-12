# Quick play with turtle.Turtle class. Drawing a multi-color flower.
import turtle
window = turtle.Screen()
window.bgcolor("black")

def draw_flower():
    Pencil_1 = turtle.Turtle()
    Pencil_1.shape("circle")
    Pencil_1.speed(0)

    for i in range (0,60):
        for i in range(0,4):
            Pencil_1.color("Green")
            Pencil_1.forward(75)
            Pencil_1.left(90)        
        Pencil_1.left(6)
        Pencil_1.color("Olive")
        Pencil_1.circle(37)
        
    Pencil_1.right(90)
    Pencil_1.forward(250)
    Pencil_1.color("Yellow")
    Pencil_1.backward(250)
    Pencil_1.setpos(-25,0)
    Pencil_1.circle(25)
    Pencil_1.setpos(0,0)
    
    window.exitonclick()

draw_flower()    
