# This program draws my initials using turtle graphics 
# 3-18-19
# CTI-110 P4T1a - Shapes
# Adrian Gorum
#
def main():

    #Turtle & Pen Settings
    import turtle
    window = turtle.Screen()
    window.bgcolor("yellow")
    t = turtle.Turtle()
    t.shape("triangle")
    t.pensize(10)    
    t.pencolor("purple")
    t.speed(1)
    
    #Pick up pen and start further on the left side of the window
    t.penup()
    t.forward(-150)
    t.pendown()
    
    #Draw an A    
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.left(180)
    t.forward(100)
    t.left(90)
    t.forward(100)

    #Pick up pen and put it down
    t.penup()
    t.forward(-275)
    t.left(-90)
    t.forward(100)    
    t.pendown()

    #Draw a G
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(55)
    
#Program start
main()
