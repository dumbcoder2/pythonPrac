#1> wap to take input and print it mutilpicatio table
a=int(input("enter your number"))
for i in range(1,11):
    print(a,"*",i,"=",i*a)
    i+=1
else:
    print("done with the tables")

# 2>wap to great everyone in the list which start with s
l=["harry","soham","sachin","rahul"]
for i in l:
 if(i.startswith("s")):
    print("namasta",i)
  
# 3>q1 with while loop
a=int(input("enter your number"))
i=0
while(i<10):
 i=i+1
 print(a,"*",i,"=",i*a)
a = int(input("enter your number: "))

# 4>wap to find prime or even
for i in range(2, a):
    if (a % i) == 0:
        print("number is not prime")
        break
else:
    print("number is prime")

# 5>wap to find sum of all natural number using while loop
i = 0
sum = 0
while i <= 10:
    sum += i
    i += 1
print(sum)

# 6>factorial of number using loop

a=int(input("enter your name :"))
f=1
for i in range(1,a+1):
    f=f*i
print(f"the factorial of {a} is {f}")

# 7>wap to print * pattern

for i in range(3):
    for j in range(len(i)):
        i+=1
        print("*")
    print("*")

# 10>multiplication in reves order
a=int(input("enter your number"))
i=11
while(i>1):
 i=i-1
 print(a,"*",i,"=",i*a)

# 8> start pattern
n = int(input("enter your number: "))

for i in range(1, n+1):
    print(" " * (n - i), end="")     # spaces decrease each row
    print("* " * i)                  # stars increase each row