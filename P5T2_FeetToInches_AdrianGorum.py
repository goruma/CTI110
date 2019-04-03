# A brief description of the project
# 4-2-2019
# CTI-110 P5T2_FeetToInches 
# Adrian Gorum
#

#Initialize global INCHES_IN_FOOT variable
INCHES_IN_FOOT = 12

#Main Function gets input from user for feet and calls feet_To_Inches function
def main():
    #Gather input from user for feet variable
    feet = float(input("Please enter a size in feet: "))

    #Displays feet to inches by calling feet_To_Inches function
    feet_To_Inches(feet)

#feet_To_Inches function converts user inputted feet value to inches and displays result
def feet_To_Inches(ft):
    #Convert feet to inches
    inches = ft * INCHES_IN_FOOT

    #Display results of conversion
    print("There are",inches,"inches in",ft,"feet.")

#Program Start
main()
