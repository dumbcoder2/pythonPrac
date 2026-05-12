# if can be independence but elif can't

# 1>find the greater number enter by user 4 input
a = int(input("enter your number: "))
b = int(input("enter your number: "))
c = int(input("enter your number: "))
d = int(input("enter your number: "))

if (a > b and a > c and a > d):
    print("a is greater number")
elif (b > a and b > c and b > d):
    print("b is greater number")
elif (c > a and c > b and c > d):
    print("c is greater number")
else:
    print("d is greater number")  

print("End of the program")     
# 2>wap to take 3 subj mark input and tell pass or fail max=40 less=33
sub1 = int(input("enter marks of subject 1: "))
sub2 = int(input("enter marks of subject 2: "))
sub3 = int(input("enter marks of subject 3: "))

if (sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("You are pass")
else:
    print("You are fail, better luck next time")

# 3>make alot of money,buy now,subscribe now,click here wap to dectective this
a=input("enter your comment")
if ( a=="alot of money" or a=="buy now" or a=="subscribe now" or a=="click here"):
    print("your commet is reject due to spamming")
else:
     print(a)   

# 4>wap to find username ontain 10 letter or what
name=input("enter your name:")
b=len(name)
if(b<=10):
    print("your name is valid")
    
# 5>wap to find a name is present in list or not
a=["nikhil","aman","khaif","akshat","billu"]
name=input("enter your name: ")
if name in a:
    print("this name is laready taken")
else:
    print(name)   

# 6> grade calucluate
a=int(input("enter your marks"))
if(a>=90 and a<=100):
 print("youre grade is x:",a)
elif(a>=80 and a<=89):
 print("youre grade is a:",a)
elif(a>=70 and a<=79):
 print("youre grade is b:",a)
elif(a>=60 and a<=69):
 print("youre grade is c:",a)
elif(a>=50 and a<=59):
 print("youre grade is d:",a)
else:
 print("better luck next time",a)

# 7>post harry
post=input("enter your post")
if (post.lower() in post.lower()):
 print("this post is talking about harry")
else:
 print("this post is not talking about harry") 