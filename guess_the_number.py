"""

Guess The Number

Write a programme where the computer randomly generates a number between 0 and 20. The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high, or too low. 

"""

from random import randint

print()
random_number = randint(0, 20)
user_guess = 0
continue_guess = 0

print("\n\nWelcome to Guess the Number\n\n")


while(continue_guess == 0):
    user_guess = input("Please guess a number betwwen 0 and 20: ")

    if(user_guess == random_number):
        print ("YOUR GUESS IS RIGHT!")
        # check if user wants to continue
        continue_guess = input(
            "Do you want to keep guessing? If so please enter 0 to continue or 1 to exit game ")
        if (continue_guess == 0):
            random_number = randint(0, 20)

        else:
            exit()

    elif(user_guess != random_number):
        print ("Your guess is wrong")
        # check if guess was low or high
        if (user_guess > random_number):
            print("Your guess was too high")
        else:
            print ("Your guess was too low")
        # check if user wants to continue
        continue_guess = input(
            "Do you want to keep guessing? If so please enter 0 to continue or any value to exit game ")
