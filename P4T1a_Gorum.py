# This program draws a square and triangle using turtle graphics and for loops
# 3-18-19
# CTI-110 P4T1a - Shapes
# Adrian Gorum
#

def main():

    import turtle
    window = turtle.Screen()
    window.bgcolor("yellow")
    t = turtle.Turtle()
    t.shape("square")
    t.pensize(5)
    
    
    #For loop to make square
    for squ in range(4):
        t.pencolor("purple")
        t.forward(100)
        t.left(90)

    #Lift up pen, move right, set pen back down
    t.penup()
    t.forward(-125)
    t.pendown()    
    
    #For loop to make triangle
    for tri in range(3):
        t.pencolor("red")
        t.forward(115)
        t.left(120)

#Program start
main()
