# Find the lowest number 
# Create a program that asks three numbers
# Find the lowest number using only if-else statement.
# Display the lowest number.

#Welcome statement
print("\nHey there!, please enter a number of your choice!")

# **********PROGRAM FLOW*****************
# 1. Ask for the first number.
first_number = int(input("\nEnter your first number: "))

# 2. Ask for the second number.
second_number = int(input("Enter your second number: "))

# 3. Ask for the third number.
third_number = int(input("Enter your third number: "))

#4. Define a variable for indication.
smallest_num = 0

# if-else statements section

# 5. if statement for the first input and present an inequalities.
if first_number < second_number and first_number < third_number :
    #Variable for the first number if it is the smallest
    smallest_num = first_number
# 6. else statement for the second input.
    # present an inequality
# 7. else statement for the third input.
        #proceeding to the last variable for the third number if it is the smallest.
#  8. Display