# 1>To view files in dir 

import os
path='.'
for iteam in os.listdir(path):
    print(iteam) 
# 2> cal two value input

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print("your adding value is",a+b)

# 3>find a reminder
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("your reminder is:",a%b)

# 4>greater or not (==)
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("is a greter then b",a>b)

# 5>average of user input
a=int(input("Enter your number"))
b=int(input("Enter your number"))
print("your average value is",(a+b)/2)

# 6>square of value
a=int(input("enter your number:"))
print("the square of your value is",a**2)

# 7>input type
a=input("Enter your input")
print((a))

