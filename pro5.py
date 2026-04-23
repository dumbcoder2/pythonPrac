'''dir() returns a list of attributes + methods of an object.'add','remove','update','clear','union'
A set is a collection that is:Unordered,Unique elements only,Mutable,Only hashable (immutable) items allowed'''

# 1> wap to take input 1 dir hindi and english taking  as list
words = {"namasta":"greeting",
       "bolo":"speak",
       "nahi":"nah",
       "shukriya":"thanks"
       }
word=input("Enter your word:")
print(words[word])

# 2>wap to take 4 no as input and display uniuqe once
e=set()
f1=int(input("Enter you number:"))
e.add(f1)
f2=int(input("Enter you number:"))
e.add(f2)
f3=int(input("Enter you number:"))
e.add(f3)
f4=int(input("Enter you number:"))
e.add(f4)
print(e)

# 3>can we have a set with 18 int and 28 as str value
e=set()
e.add(18)
e.add('28')
print((e))

# 4>find len of the set 
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

# 5find the type
s={}
print(type(s))

# 6>create a empty dir take 4 value as inpput based on name:languages
s={}
name=input("enter your name and lanugae:")
lan=input("enter your lanugae:")
s.update({name:lan})
name=input("enter your name and lanugae:")
lan=input("enter your lanugae:")
s.update({name:lan})
name=input("enter your name and lanugae:")
lan=input("enter your lanugae:")
s.update({name:lan})
name=input("enter your name and lanugae:")
lan=input("enter your lanugae:")
s.update({name:lan})
name=input("enter your name and lanugae:")
lan=input("enter your lanugae:")
s.update({name:lan})
print(s)

# 7> slove this problem
s={8,7,9,"harry",(1,2)}
s.remove((1,2))
print(s)
s.add((2,3))
print(s)