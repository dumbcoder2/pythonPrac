#  stone","paper" and "scissor

import random

computer = random.choice([1,2,3])

your = input("Enter your value : ")

yourdict = {
    "stone":1,
    "paper":2,
    "scissor":3
}

reversedict = {
    1:"stone",
    2:"paper",
    3:"scissor"
}

you = yourdict[your]

print(f"You chose {reversedict[you]} and computer chose {reversedict[computer]}")

if(you == computer):
    print("It's a Draw")

else:
    if(you == 1 and computer == 2):
        print("Computer wins")

    elif(you == 1 and computer == 3):
        print("You win")

    elif(you == 2 and computer == 1):
        print("You win")

    elif(you == 2 and computer == 3):
        print("Computer wins")

    elif(you == 3 and computer == 1):
        print("Computer wins")

    elif(you == 3 and computer == 2):
        print("You win")

    else:
        print("Something went wrong")