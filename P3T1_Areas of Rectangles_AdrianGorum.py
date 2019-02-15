#Program will measure the area of two rectangles from user input and output which
#rectangle has the greater area or if they are both equal.
#2-14-19
#P3T1 - Areas of Rectangles
#Adrian Gorum
#


rec1_length = int(input("What is the length of the first rectangle? "))
rec1_width = int(input("What is the width of the first rectangle? "))

print("")

print("The length of rectangle 1 is: ",rec1_length)
print("The width of rectangle 1 is: ",rec1_width)

print("")

rec2_length = int(input("What is the length of the second rectangle? "))
rec2_width = int(input("What is the width of the second rectangle? "))

print("")

print("The length of rectangle 2 is: ",rec2_length)
print("The width of rectangle 2 is: ",rec2_width)

print("")

rec1_area = int(rec1_length * rec1_width)
rec2_area = int(rec2_length * rec2_width)

print("")

print("Rectangle 1 area = ",rec1_area)
print("Rectangle 2 area = ",rec2_area)

print("")

if rec1_area == rec2_area:
    print("Both rectangles have the same area.")
else:
    
    if rec1_area > rec2_area:
        print("Rectangle 1 has the larger area.")
    else: 
        print("Rectange 2 has the larger area.")





