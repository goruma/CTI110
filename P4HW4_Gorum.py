# This programs draws a polygonal shape using nested for loops
# 3-18-19
# P4HW4 - Nested Loops
# Adrian Gorum
#

def main():
    #Enable turtle graphics
    import turtle
    #Set screen variable
    window = turtle.Screen()
    #Set screen color
    window.bgcolor("red")

    #Pen Settings
    myPen = turtle.Turtle()
    myPen.shape("arrow")
    myPen.speed(10)
    myPen.pensize(8)
    myPen.color("yellow")
    
    #Nested loop to create square and then iterate the square 8 times at 45 degree angle
    for x in range(8):
        for y in range(4):
            #Create square shape
            myPen.forward(100)
            myPen.left(90)
        #Turn square 45 degrees to the left to start next iteration
        myPen.left(45)        

#Program Start
main()
