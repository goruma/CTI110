# This programs keeps a running total of the number of bugs collected over five days.
# 3-18-19
# CTI-110 P4T2 - Bug Collector
# Adrian Gorum
#

#Pseudocode
#Inform user of what program does
#Initialize accumulator variable for bug_sum
#Use a for loop to gather input from user 5 times
#Calculate total sum using bug_sum variable and user inputed numbers
#Display total bugs collected

def main():
    
    #Inform user of program's purpose
    print("************************************************************************")
    print("This program will keep a running total of the number of bugs collected \nduring",
          "a period of 5 days and then display the total.\n")

    #initialize accumulator variable
    bug_sum = 0

    #for loop gathers input 5 times
    for days in range(1,6):
        #Prompt user to input bugs collected
        print("Would you kindly enter the number of bugs collected on day {}?" .format(days))
        
        #Gather input from user for number of bugs
        bug_num = int(input())
        
        #bug_sum accumulates based on user inputed bug_num variable
        bug_sum += bug_num

    #Display the total of bugs collected after 5 days
    print("You collected a total of {} bugs over a 5 day period!" .format(bug_sum))
    
#Program Start
main()
