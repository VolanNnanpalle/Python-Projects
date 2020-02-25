# -*- coding: UTF-8 -*-
"""

Rock, Paper, Scissors Game
Make a rock-paper-scissors game where it is the player vs the computer. The computer’s answer will be randomly generated, while the program will ask the user for their input.
"""


from random import randint


#rock beats scissors
#paper beats rock
#scissors beats paper
rock = 1
paper = 2
scissors = 3
computer = randint(1, 3)
print("\n\nWelcome to Rock, Paper, Scissors Game\n\n")
print("\n\n Rock = 1\n Paper = 2\n Scissors = 3\n\n")
print ("You will be playing the computer\n\n")

print("Plelae enter the respective valuese\n\n")
user_input = int(input("Rock, Paper, Scissors, SHOOT!"))

if(user_input == 1 & computer == 3):
    print  ("YOU WIN!\n")
    print(computer,"\n")
    print("You chose ROCK & the computer chose SCISSORS\n")
elif(user_input == 1 & computer == 2):
    print ("YOU LOSE!\n")
    print(computer, "\n")
    print("You chose ROCK & the computer chose PAPER\n")
elif(user_input==2 & computer==1):
    print ("YOU WIN!\n")
    print(computer, "\n")
    print("You chose PAPER & the computer chose ROCK\n")
elif(user_input==2 & computer==3):
    print ("YOU LOSE!\n")
    print(computer, "\n")
    print("You chose PAPER & the computer chose SCISSORS\n")
elif(user_input==3 & computer==2):
    print ("YOU WIN!\n")
    print(computer, "\n")
    print("You chose SCISSORS & the computer chose PAPER\n")
elif(user_input==3 & computer==1):
    print ("YOU LOSE!\n")
    print(computer, "\n")
    print("You chose SCISSORS & the computer chose ROCK\n")
elif(user_input == computer):
    print ("ITS A TIE!\n")
    print(computer, "\n")


print(computer)
print(user_input)
