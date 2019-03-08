def main():

    import turtle
    window = turtle.Screen()
    t = turtle.Turtle()
    t.shape("triangle")
    t.pensize(10)    
    t.pencolor("purple")    
    
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
