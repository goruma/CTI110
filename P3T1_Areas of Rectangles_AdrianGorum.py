#Program will measure the area of two rectangles from user input and output which
#rectangle has the greater area or if they are both equal.
#2-14-19
#P3T1 - Areas of Rectangles
#Adrian Gorum
#

#Pseudocode
#Gather input from user on rectangle1 length and width and rectangle2 length and width >
#calculate the area of rectangle 1 > calculate the area of rectangle 2 > display whether
#rectangle 1 or rectangle 2 has the greater area or if they are the same
#

#Gather input from user on the length and width of rectangle 1.
rec1_length = int(input("What is the length of the first rectangle? "))
rec1_width = int(input("What is the width of the first rectangle? "))

print("")

#Gather input from user on the length and width of rectangle 2.
rec2_length = int(input("What is the length of the second rectangle? "))
rec2_width = int(input("What is the width of the second rectangle? "))

print("")

#Calculate area of both rectangles.
rec1_area = int(rec1_length * rec1_width)
rec2_area = int(rec2_length * rec2_width)

#Determine which area is greater or if they are the same, then display results.
if rec1_area == rec2_area:
    print("Both rectangles have the same area.")
else:    
    if rec1_area > rec2_area:
        print("Rectangle 1 has the larger area.")
    else: 
        print("Rectangle 2 has the larger area.")





