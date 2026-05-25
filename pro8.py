# 1> find greater amoun a,b,c

# def gre():
#     a=int(input("enter your number"))
#     b=int(input("enter your number"))
#     c=int(input("enter your number"))
#     print("the greater number is:",max(a,b,c))

# gre()

# 2>convert cleusius into fahrenheit

# def f_to_c(f):
#     return 5 * (f - 32) / 9

# f = int(input("Enter temperature in Fahrenheit: "))
# print(f_to_c(f))

# 3>prevent from print fun() ti skip newline

# print("a")
# print("b")
# print("c",end=" ")
# print("d",end="")

# 4>calcu sum n of natural number

# def sum_n(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_n(n-1)
    
# x = int(input("enter your number: "))
# print("sum is", sum_n(x))

# 5> def star pattern 

# def patt(n):
#     if n == 0:
#         return
#     print("*"*n)
#     patt(n-1)
# patt(3)

# 6>cm to inch
# def cm_inche(inch):
#     return inch *2.54

# n=int(input("enter your inches: "))
# print(f"the corrsepnding value is:{cm_inche(n)}")

# 7> strip and remove form list 
# def rem(word):

#     l=["rohan","raj","niraj","abhi","krishna","himanshu"]
#     for i in l:
#      if word in l:
#       l.remove(word)
   
    
#     print(f"the return value of l is{l}")   
# rem("raj") 

# 8>    multipication table of given number

# def table(n):
#     for i in range(1,11):
#         print(f"{n}*{i}""=",n*i)
# num=int(input("enter your number"))        
# table(num)