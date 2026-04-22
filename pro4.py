"""
List=
A list is a collection of items,Mutable (you can change it),Defined using []
append(x)	Adds item at end,insert(i, x)	Adds item at index,
extend(iterable)	Adds multiple items,remove(x)	Removes specific value
pop(i)	Removes item at index,clear()	Removes all elements
index(x)	Returns index of value,count(x)	Counts occurrences
sort()	Sorts list,reverse()	Reverses list,copy()	Returns copy of list

A tuple is also a collection of items
Immutable (cannot be changed)
Defined using parentheses ()
count(x)	Counts occurrences,index(x)	Finds index of value
"""
# 1>to store four frits as input in list

Fruits=[]
f1=input("enter your fruit")
(Fruits.append(f1))
f2=input("enter your fruit")
(Fruits.append(f2))
f3=input("enter your fruit")
(Fruits.append(f3))
f4=input("enter your fruit")
(Fruits.append(f4))
print(Fruits)

# 2>wap to accept mark of 4 stu and sorten them 
marks=[]
stu1=int(input("enter your marks:",))
marks.append(stu1)
stu2=int(input("enter your marks:",))
marks.append(stu2)
stu3=int(input("enter your marks:",))
marks.append(stu3)
stu4=int(input("enter your marks:",))
marks.append(stu4)
print("Before sorting:", marks)
print(marks)
marks.sort()
print("After sorting:", marks)
print(type(marks))

# 3>write a immutable tuple
a=("harry","nikhil",1,4)
a[2]="ball"
print(a)

# 4>wap list of 4 number sum
a=[]
f1=int(input("enter your number: "))
a.append(f1)
f2=int(input("enter your number: "))
a.append(f2)
f3=int(input("enter your number: "))
a.append(f3)
f4=int(input("enter your number: "))
a.append(f4)
print(a)
print("the sum of numbers are:",sum(a))

# 5> WAP to count the number of zero in there
a=(7,0,8,0,0,9)
b=a.count(0)
print(b)
