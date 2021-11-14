# Life stages
# Create a program that ask for an age of a person
# Display the life stage of the person
# Rules:
# 0-12: Kid
# 13-17: Teen
# 18: Debut
# 19 above: Adult

# Welcome statement
print("\nLet's see what's your life stage!")

# Ask for the age.
age = int(input("\nPlease enter your age: "))

# ****if-else section****
# test the input if classified as Kid
if age >= 0 and age <= 12:
    print(f"\nYour age is {age} years old!\nLife Stage Classification: You're a Kid!")
else:
    # test the input if classified as Teen
    if age >= 13 and age <= 17:
        print(f"\nYour age is {age} years old!\nLife Stage Classification: You're a Teen!")
    else:
        # test the input if classified as Debut
        if age == 18:
            print(f"\nYour age is {age} years old!\nLife Stage Classification: Debut!")
        else:
            # proceed directly as an adult classification
            print(f"\nYour age is {age} years old!\nLife Stage Classification: You're an Adult!")
# add ending/closing statement by using print
print("\nGreat!\n")      