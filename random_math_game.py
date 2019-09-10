import random

def main():
    response = "y" or "Y"
    while response == "y" or "Y":
        prompt_one = input("This game asks you to answer some randomly generated math questions. \nThere's no time limit because I'm not good at coding."
                           "\nType start in lowercase letters to begin: ")

        while prompt_one != "start":
            prompt_one = input("That's a weird way to spell start. \nType start in lowercase letters to begin: ")

        print("Cool.")

        question_one()

# fxn prompts the user with two random numbers between 1 and 99, with which they are to add together
def question_one():
    count = 0

    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)

    answer = int(number_one + number_two)
    print(str(number_one) + " + " + str(number_two) + " equals? ")
    user_guess = int(input())

    if user_guess == answer:
        print("I'm literally crying.")
        count += 1
    if user_guess != answer:
        print("Yeah dude that's wrong.")

    if count == 0:
        print("You have " + str(count) + " points.")

    if count == 1:
        print("You have " + str(count) + " point.")

    question_two(count)

def question_two(count):
    random_integer = random.randint(1, 10)
    print("Question Two: What is the derivative of " + str(random_integer) + "x^3? ")

    answer = 3 * random_integer
    answer_part_two = "x^2"
    
    user_guess = input()

    if str(user_guess) == str(answer) + str(answer_part_two):
        print("omg")
        count += 1

    if str(user_guess) != str(answer) + str(answer_part_two):
        print("how could you betray me like this")

    if count == 0:
        print("You still have " + str(count) + " points lol")

    if count == 1:
        print("You have " + str(count) + " point.")

    if count > 1:
        print("You have " + str(count) + " points.")

    question_three(count)
    
def question_three(count):
    random_integer = random.randint(2, 10)
    print("Question Three: What is the derivative of sin(" + str(random_integer) + "x)? ")

    answer = random_integer
    answer_part_two = "cos("
    answer_part_three = random_integer
    answer_part_four = "x)"

    user_guess = input()

    if str(user_guess) == str(answer) + str(answer_part_two) + str(answer_part_three) + str(answer_part_four):
        print("Great Scott") 
        count += 1

    if str(user_guess) != str(answer) + str(answer_part_two) + str(answer_part_three) + str(answer_part_four):
        print("pathetic")

    if count == 0:
        print("You still have " + str(count) + " points :(")

    if count == 1:
        print("You have " + str(count) + " point.")

    if count > 1:
        print("You have " + str(count) + " points.")

    question_four(count)
    
def question_four(count):
    random_integer = random.randint(2, 10)
    print("Question Four: What is the derivative of e^" + str(random_integer) + "x? ")

    answer = random_integer
    answer_part_two = "e^"
    answer_part_three = random_integer
    answer_part_four = "x"

    user_guess = input()

    if str(user_guess) == str(answer) + str(answer_part_two) + str(answer_part_three) + str(answer_part_four):
        print("dope dude") 
        count += 1

    if str(user_guess) != str(answer) + str(answer_part_two) + str(answer_part_three) + str(answer_part_four):
        print("oh")

    if count == 0:
        print("You have " + str(count) + " points.")

    if count == 1:
        print("You have " + str(count) + " point.")

    if count > 1:
        print("You have " + str(count) + " points.")

    question_five(count)
    
def question_five(count):
    print("Question Five: Can you name a country in Africa?"
          "\nIf you cannot name a country, please type \"the american education system failed me\" ")

    user_guess = input()

    if user_guess == "yes" or user_guess == "Yes":
        print("hell yeah")
        count += 1
    else:
        print("me too man")

    total(count)

def total(count):
    if count == 5:
        print("YOU GOT A PERFECT SCORE!!!")

    if count < 5 and count > 1:
        print("You got " + str(count) + " points!")

    if count == 1:
        print("You got 1 point!")

    if count == 0:
        print("You finished with 0 points.")

        print("Thanks for playing!")
        
main() 
