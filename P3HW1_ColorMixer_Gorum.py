# CTI-110 
# P3HW1 - Color Mixer 
# Adrian Gorum  
# 2-15-19
#

#Gather input from user for two Primary colors. Only options are Red, Blue, & Yellow
print("Enter 2 different primary colors (red, blue, or yellow) to find out which")
print("secondary color they make when mixed.")
print("")
prime_color1 = str(input("Enter the first primary color you'd like to mix? "))
prime_color2 = str(input("Enter the second primary color you'd like to mix? "))
print("")

#Initialize secondary color variable
secondary_color = str()

#Determine which secondary color is produced.
if (prime_color1 == "red" and prime_color2 == "blue")or(prime_color1 == "blue" and prime_color2 == "red"):
    secondary_color = "purple"
    print("The secondary color produced is",secondary_color+".")
elif (prime_color1 == "red" and prime_color2 == "yellow")or(prime_color1 == "yellow" and prime_color2 == "red"):
    secondary_color = "orange"
    print("The secondary color produced is",secondary_color+".")
elif (prime_color1 == "yellow" and prime_color2 == "blue")or(prime_color1 == "blue" and prime_color2 == "yellow"):
    secondary_color = "green"
    print("The secondary color produced is",secondary_color+".")
else:
    print("ERROR: You did not enter two different primary colors(red, blue, or yellow).")
      

      
