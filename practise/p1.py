# 1>Print numbers from 1 to 10 using for loop
for i in range(1,11):
    print(i)

# 2> Print numbers from 10 to 1 using while loop.   

n=1;
while(n<=10):
    print(n)
    n=n+1

# 3>Find the sum of first n natural numbers.
n = int(input("Enter your number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)

# 4>Find factorial of a number
def fac(n):
    prod=1
    for i in range(1,n+1):
        prod=prod*i
    print("factorial",prod)
n=int(input("enter your word"))
fac(n)

# 5>Recursive factorial
def rec(n):
    if n==1:
        return 1;
    else:
         return n*rec(n-1)
    print(n)   
n=int(input("enter your number")) 
print(rec(n)) 

# 6>  Check whether a number is prime or not.
n=int(input("enter your number:"))
if(n%2==0):
    print("this is prime number",n)
else:
    print("this is non-prime number",n)

# 7>Print all even numbers between 1 to 100.

for i in range(0,101):
    if(i%2==0):
        print(i)
    
# 8>Count vowels in a string.
n = input("Enter a word: ")
l = ["a", "e", "i", "o", "u"]
count = 0
for i in n.lower():
    if i in l:
        count += 1

print("The number of vowels is:", count)

# 9>Reverse a string.
n=input("enter a word")
print("the reversed string is:",n[::-1])

# 10>Check whether a string is palindrome or not.
n=input("enter your word")
if(n[::-1]==n):
    print("the word is palindrome")
else:
        print("the word is not a  palindrome")

# 11>Count number of words in a sentence.
n=input("enter your sentences")
words=n.split()
print("number of words:",len(words))
 
# 12>Convert string to uppercase and lowercase.
n=input("enter your sentence")
print(n.lower())
print(n.upper())

# 13>Find the maximum element in a list.
l=["apple","mango","apple","graphes"]
for i in l:
    print(max(l,key=len))

#  14>Find the maximum element in a list.

l = [10, 25, 7, 89, 45]
print("Maximum element is:", max(l)) 

# 15>Find the sum of all elements in a list.  
l = [10, 25, 7, 89, 45]
print("the total of all element in list:",sum(l))

# 16>Remove duplicate elements from a list.
l = [10, 20, 10, 30, 40, 20, 50, 10, 30, 40, 50, 20]
m=list(set(l))
print("the real value is:",m)

# 17>Create a function to calculate area of circle.
def cal(a, b):
    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        c = a + b
        print("Addition:", c)

    elif op == "-":
        c = a - b
        print("Subtraction:", c)

    elif op == "*":
        c = a * b
        print("Multiplication:", c)

    elif op == "/":
        c = a / b
        print("Division:", c)

    else:
        print("Invalid operator")
cal(10, 5)
# 18>Create a function to calculate area of circle.
def area(r):
    pi=3.14
    area=pi*r*r
    print("area of circle is:",area)
r=float(input("enter your r"))
area(r)
# 19>Create a recursive function for factorial.
def fac(n):
    if n == 1 or n == 0:
      return 1
    else:
     return n * fac(n - 1)
print("the factorial of n is:",fac(5))
