# Program prompts user to enter a distance in kilometers, then converts that distance to miles.
# 4-2-2019
# CTI-110 P5T1_KilometerConverter 
# Adrian Gorum
#

#Initialize global variable for conversion factor
CONVERSION_FACTOR = 0.6214

#Main Function gets input in kilometers and calls displayMiles function
def main():
    #Get input for distance in Kilometers
    kilometers = float(input("Please enter a distance in kilometers: "))
    
    #Display conversion by calling displayMiles function
    displayMiles(kilometers)
    
#displayMiles function converts kilometers to miles and displays the conversion
def displayMiles(km):
    #Calculate kilometers to miles
    miles = km * CONVERSION_FACTOR

    #Display Conversion
    print(km,"kilometers =",format(miles,'.2f'),"miles.")

#Program Start
main()
