# 2> Number guessing game.
import random
computer=random.choice(range(1,100))
while True:
 you=int(input("enter your number: "))

 if(you==computer):
    print("you win")

 else:
    if(you > computer):
     print("your number is to big")
    elif(you < computer):
        print("your number is too small")
    else:
       print("somethink went wrong")    
    