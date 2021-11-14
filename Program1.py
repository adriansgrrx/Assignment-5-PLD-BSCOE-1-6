# Create a program that will ask for grade percentage
# Display the equivalent Grade/Mark and Description
# program #2: grading
# grade/mark    percentage     description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.50          79-81           Satisfactory
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropped

# example:
# input grade: 87.6
# grade/mark: 1.75
# description: Very good

# Steps
# 1. Ask for the grade percentage

#Validation
while True:
    try:
        grades = float(input("\nPlease enter your grade percentage: "))
    except ValueError:
        print("\nSorry, you've entered invalid characters. Please try again.")
        continue
    if grades < 65:
        print("\nSorry, please enter a grade percentage ranging from 65-100. Thank you.\n")
    else:
        break
    
if grades > 100:
    print("\nSorry, please enter a grade percentage ranging from 65-100. Thank you.\n")
else:
    print("\nBase on the grading system, here's your grade evaluation...")

# 2. Display the equivalent Grade/Mark and display the description

    if grades >= 97 and grades <= 100:
    #Display the equivalent Description
        print(f"\nGrade percentage: {grades}%\nEquivalent: 1.00\nDescription: Excellent\n")
    else:
        if grades >= 94 and grades <= 96:
            #Display the equivalent Description
            print(f"\nGrade percentage: {grades}%\nEquivalent: 1.25\nDescription: Excellent\n")
        else:
            if grades >= 91 and grades <= 93 or grades >= 88 and grades <= 90:
                #Display the equivalent Description
                print(f"\nGrade percentage: {grades}%\nEquivalent: 1.5\nDescription: Very Good\n")
            else:
                if grades >= 88 and grades <= 90:
                    #Display the equivalent Description
                    print(f"\nGrade percentage: {grades}%\nEquivalent: 1.75 \nDescription: Very Good\n")
                else:
                    if grades >= 85 and grades <= 87:
                        #Display the equivalent Description
                        print(f"\nGrade percentage: {grades}%\nEquivalent: 2.00 \nDescription: Good\n")
                    else:
                        if grades >= 82 and grades <= 84:
                            #Display the equivalent Description
                            print(f"\nGrade percentage: {grades}%\nEquivalent: 2.25 \nDescription: Good\n")
                        else:
                            if grades >= 79 and grades <= 81:
                                #Display the equivalent Description
                                print(f"\nGrade percentage: {grades}%\nEquivalent: 2.50 \nDescription: Satisfactory\n")
                            else:
                                if grades >= 76 and grades <= 78:
                                #Display the equivalent Description
                                    print(f"\nGrade percentage: {grades}%\nEquivalent: 2.75 \nDescription: Satisfactory\n")   
                                else:
                                    if grades == 75:
                                    #Display the equivalent Description
                                        print(f"\nGrade percentage: {grades}%\nEquivalent: 3.00 \nDescription: Passing\n")
                                    else:
                                        if grades >= 65 and grades <= 74:
                                        #Display the equivalent Description
                                            print(f"\nGrade percentage: {grades}%\nEquivalent: 5.00 \nDescription: Failure\n")
                                        else:
                                            if grades == INC:
                                            #Display the equivalent Description
                                                print(f"\nGrade percentage: {grades}%\nDescription: Incomplete\n")
                                            else:
                                                if grades == W:
                                                #Display the equivalent Description
                                                    print(f"\nGrade percentage: {grades}%\nDescription: Withrawn\n")
                                                else:
                                                    if grades == D:
                                                    #Display the equivalent Description
                                                        print(f"\nGrade percentage: {grades}%\nDescription: Dropped\n")

    print ("Congratulations! You did great!\n")                                                                          