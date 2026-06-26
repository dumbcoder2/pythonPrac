# Password generator.
import random

def generate(length):
 Uppercaseletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 upper=random.choice(Uppercaseletters)
 lowercase="abcdefghijklmnopqrstuvwxyz"
 lower=random.choice(lowercase)
 digit="123456789"
 dig=random.choice(digit)
 specialsign="!@#$%&*"
 spe=random.choice(specialsign)
 allchar = Uppercaseletters + lowercase + digit + specialsign
 password = ""
 for i in range(length):
    password +=random.choice(allchar)
 
 return password
 
# print(generate()) 

try:
    user = int(input("password length should be atleast 8 character:"))

    if( user >= 8 and user <= 20):
        print("this is your password", generate(user))

    else:
        print("weak password")

except:
    print("enter valid number")