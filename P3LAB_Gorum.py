# CTI-110 - Program calculates student grades
# P3LAB: Debugging 
# Adrian Gorum 
# 2-15-19
#

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = int(90)
    B_score = int(80)
    C_score = int(70)
    D_score = int(60)
    F_score = int(50)
    # TO DO: define the rest of the scores

    #Gather input from user to initiate score variable
    score = int(input('Enter grade: '))

    #Determine student grade based on user input
    if score >= A_score:
        print('Your grade is: A')
    elif (score >= B_score and score < A_score):
        print('Your grade is: B')
    elif (score >= C_score and score < B_score):
        print('Your grade is: C')
    elif (score >= D_score and score < C_score):
        print('Your grade is: D')
    else:
        print('Your grade is: F') # TO DO: finish this


# program start
main()
