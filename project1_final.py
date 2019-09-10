# Cole Rau -- TCSS 142, Section A

# Code logic:
# The program starts with the function "main." The variable "user_napier1" is tested using the
# "character_validation" function. If "user_napier1" is a character, "user_napier1" is passed to the function
# "letters_to_numbers," which translates "user_napier1" (a character) into an integer. The result is printed
# to the screen. Next, the variable "user_napier2" is processed and printed the same way as "user_napier1" if
# "user_napier2" is a character. Then,
# the variable "user_operator" is tested using the function "operator_validation." If "user_operator" is an allowed
# operator (+, -, *, or /), the second half of the function "main" is executed. The second half of "main" has four
# if statements. One if statement is executed depending on whether "user_operator" is +, -, * or /.
# Next, one of the following operations occurs. Depending on whether "user_operator" is +, -, *, or /,
# "user_napier1 is either added to "user_napier2;" or "user_napier2" is subtracted from "user_napier1;" or
# "user_napier1" is multiplied by "user_napier2;" or "user_napier1" is divided by "user_napier2."
# The result of the calculation is printed to the screen. Finally, the "main" function asks the user if
# they want to repeat the program. If the user types "y," the program is repeated.
# If the user types "n," "Good bye" is printed to the screen.

# This function passes the variables "user_napier1" and "user_napier2" to the "character_
# validation" function, the "operator_validation function," the "letters_to_numbers" function, and the
# "integer_to_napier" function.
def main():
    user_response = "y"
    while user_response == "y":
        user_napier1 = input("Please enter a number in Napier's notation: ")
        while character_validation(user_napier1) == False:
            user_napier1 = input("Invalid input. Please enter a number in Napier's notation: ")
        print("The first number is {}.".format(letters_to_numbers(user_napier1)))

        user_napier2 = input("Please enter a second number in Napier's notation: ")
        while character_validation(user_napier2) == False:
            user_napier2 = input("Invalid input. Please enter a second number in Napier's notation: ")
        print("The second number is {}.".format(letters_to_numbers(user_napier2)))

        user_operator = input("Please enter a mathmatical operation (either +, -, *, or /): ")
        while operator_validation(user_operator) == False:
            user_operator = input("Invalid input. Please enter a mathmatical operation (either +, -, *, or /): ")

# The "addition," "subtraction," "multiplication, and "division" variables are passed to the
# "integer_to_napier" function. 
        if user_operator == "+":
            addition = letters_to_numbers(user_napier1) + letters_to_numbers(user_napier2)
            print("The result is {}.".format(addition))
        if user_operator == "-":
            subtraction = letters_to_numbers(user_napier1) - letters_to_numbers(user_napier2)
            print("The result is {}.".format(subtraction))
        if user_operator == "*":
            multiplication = letters_to_numbers(user_napier1) * letters_to_numbers(user_napier2)
            print("The result is {}.".format(multiplication))
        if user_operator == "/":
            division = letters_to_numbers(user_napier1) // letters_to_numbers(user_napier2)
            print("The result is {}.".format(division))

        user_response = input("Would you like to repeat the program? Enter y for yes, n for no: ")
        
    print("Good bye.") # If user enters "n," the beginning while loop is exited and "Good bye" is printed. 

# This function receives as parameters the variables "user_napier1" and "user_napier2" from the "main" function.
# This function returns True to "main" if the user's Napier's value is a character a-z. The function returns
# False to "main" if the user's Napier's value is not a character.
def character_validation(possible_napier):
    return possible_napier.isalpha()     

# This function receives as a parameter the "user_operator" variable from the "main" function. 
# This function returns True to "main" if the user's operator is +, -, /, or *. The function returns False to "main"
# if the user's operator is anything other than +, -, /, or *. 
def operator_validation(operator):
    if (operator == "+" or operator == "-" or operator == "/"
    or operator == "*"):
        result = True
    else:
        result = False
    return result

# This function receives as parameters the variables "user_napier1" and "user_napier2" from "main."
# This function translates the user's alphabetical input into an integer and returns the value to "main."
def letters_to_numbers(napier):
    napier_counter = 0
    for letter in napier:
        if letter == "a":
            napier_counter += 2 ** 0
        if letter == "b":
            napier_counter += 2 ** 1
        if letter == "c":
            napier_counter += 2 ** 2
        if letter == "d":
            napier_counter += 2 ** 3
        if letter == "e":
            napier_counter += 2 ** 4
        if letter == "f":
            napier_counter += 2 ** 5
        if letter == "g":
            napier_counter += 2 ** 6
        if letter == "h":
            napier_counter += 2 ** 7
        if letter == "i":
            napier_counter += 2 ** 8
        if letter == "j":
            napier_counter += 2 ** 9
        if letter == "k":
            napier_counter += 2 ** 10
        if letter == "l":
            napier_counter += 2 ** 11
        if letter == "m":
            napier_counter += 2 ** 12
        if letter == "n":
            napier_counter += 2 ** 13
        if letter == "o":
            napier_counter += 2 ** 14
        if letter == "p":
            napier_counter += 2 ** 15
        if letter == "q":
            napier_counter += 2 ** 16
        if letter == "r":
            napier_counter += 2 ** 17
        if letter == "s":
            napier_counter += 2 ** 18
        if letter == "t":
            napier_counter += 2 ** 19
        if letter == "u":
            napier_counter += 2 ** 20
        if letter == "v":
            napier_counter += 2 ** 21
        if letter == "w":
            napier_counter += 2 ** 22
        if letter == "x":
            napier_counter += 2 ** 23
        if letter == "y":
            napier_counter += 2 ** 24
        if letter == "z":
            napier_counter += 2 ** 25

    return napier_counter

main()
