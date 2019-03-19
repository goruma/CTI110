# This programs draws a snowflake using a for loop
# 3-18-19
# P4t1c - Snowflake
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
    myPen.speed(5)
    myPen.pensize(7)
    myPen.color("yellow")

    #Function to draw one branch of snowflake
    def branch():
        #First branch of snowflake
        myPen.left(90)
        myPen.forward(100)
        myPen.forward(-40)
        myPen.left(40)
        myPen.forward(30)
        myPen.forward(-30)
        myPen.right(80)
        myPen.forward(30)
        myPen.forward(-30)
        myPen.left(40)        
        myPen.forward(-40)
        myPen.left(40)
        myPen.forward(20)
        myPen.forward(-20)
        myPen.right(80)
        myPen.forward(20)
        myPen.forward(-20)
        myPen.left(40)
        myPen.forward(-20)
        #Turn branch 45 degrees for new branch to start
        myPen.right(45)

    #Function to use loop to draw 8 branches of snowflake
    def drawSnowflake():
        for x in range (8):
            branch()

    #Call the drawSnowflake function
    drawSnowflake()    
        

#Program Start
main()
