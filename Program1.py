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
#Def function to ask fo the grade percentage
def inpt_grades():
    prcntg_grade =(input("\nPlease enter your Grade/Mark: "))
    return prcntg_grade
#Call the function
grades = inpt_grades()


# if and else statement section including the input process 
if grades.replace(".","",1).isdigit() == True:
#round-off plus float, in-case the grades are in decimal form. The command will round-off to the highest term.
    final_mark = round(float(grades))
# 2. Display the equivalent Grade/Mark and display the description
    if final_mark < 65:
        print(f"\nGrade percentage: {final_mark}% \nDescription: [NOT FOUND] Your input grade percentage could be; Incomplete[Inc.], Withrawn[W] or Dropped[D].\n")
    else:
        pass
        if final_mark > 100:
            print("\nSorry, please enter a grade percentage ranging from 65-100. Thank you.\n")
        else:
            print("\nBase on the grading system, here's your grade evaluation...")            
            if final_mark >= 97 and final_mark <= 100:
                #Display the equivalent Description
                print(f"\nGrade percentage: {final_mark}%\nEquivalent: 1.00\nDescription: Excellent\n")
            else:
                if final_mark >= 94 and final_mark <= 96:
                    #Display the equivalent Description
                    print(f"\nGrade percentage: {final_mark}%\nEquivalent: 1.25\nDescription: Excellent\n")
                else:
                    if final_mark >= 91 and final_mark <= 93:
                        #Display the equivalent Description
                        print(f"\nGrade percentage: {grades}%\nEquivalent: 1.5\nDescription: Very Good\n")
                    else:
                        if final_mark >= 88 and final_mark <= 90:
                            #Display the equivalent Description
                            print(f"\nGrade percentage: {final_mark}%\nEquivalent: 1.75 \nDescription: Very Good\n")
                        else:
                            if final_mark >= 85 and final_mark <= 87:
                                #Display the equivalent Description
                                print(f"\nGrade percentage: {final_mark}%\nEquivalent: 2.00 \nDescription: Good\n")
                            else:
                                if final_mark >= 82 and final_mark <= 84:
                                    #Display the equivalent Description
                                    print(f"\nGrade percentage: {final_mark}%\nEquivalent: 2.25 \nDescription: Good\n")
                                else:
                                    if final_mark >= 79 and final_mark <= 81:
                                        #Display the equivalent Description
                                        print(f"\nGrade percentage: {final_mark}%\nEquivalent: 2.50 \nDescription: Satisfactory\n")
                                    else:
                                        if final_mark >= 76 and final_mark <= 78:
                                            #Display the equivalent Description
                                            print(f"\nGrade percentage: {final_mark}%\nEquivalent: 2.75 \nDescription: Satisfactory\n")   
                                        else:
                                            if final_mark == 75:
                                                #Display the equivalent Description
                                                print(f"\nGrade percentage: {final_mark}%\nEquivalent: 3.00 \nDescription: Passing\n")
                                            else:
                                                if final_mark >= 65 and final_mark <= 74:
                                                #Display the equivalent Description
                                                    print(f"\nGrade percentage: {final_mark}%\nEquivalent: 5.00 \nDescription: Failure\n")
#non-nummerical input section of if else statements
else:                               
    nonnummerical_mark = grades
    if nonnummerical_mark == "INC." or nonnummerical_mark == "Inc." or nonnummerical_mark == "inc." or nonnummerical_mark == "inc":
        print(f"\nYour input: {nonnummerical_mark}\nDescription: Incomplete\n")
    else: 
        if nonnummerical_mark == "W" or nonnummerical_mark == "w": 
            print(f"\nYour input: {nonnummerical_mark}\nDescription: Withdrawn\n")
        else: 
            if nonnummerical_mark == "D" or nonnummerical_mark == "d":
                print(f"\nYour input: {nonnummerical_mark}\nDescription: Dropped\n")
            else:
                print(f"\n[NOT FOUND] {nonnummerical_mark} is not included in the system.\n")