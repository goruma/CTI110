def main():

    import turtle
    window = turtle.Screen()
    t = turtle.Turtle()
    t.shape("square")
    t.pensize(3)
    
    
    #For loop to make square
    for squ in range(4):
        t.pencolor("purple")
        t.forward(100)
        t.left(90)

    t.penup()
    t.forward(125)
    t.pendown()    
    
    #For loop to make triangle
    for tri in range(3):
        t.pencolor("red")
        t.forward(115)
        t.left(120)
    
    



#Program start
main()
