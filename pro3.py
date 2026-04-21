"""Strings are immutable which means Strings are stored in memory as fixed sequences of characters.
Any operation that seems to modify a string actually creates a new string object.
The original string remains unchanged."""

# 1>print input name and good afternooning 
name=str(input("Enter your name:"))
print (name,"Good Afternoon")

# 2>printe name and date in string 
letter='''<name>
you are selected
<date>
'''
letter=letter.replace("<name>","nikhil")
letter=letter.replace("<date>","02-06-26")
print(letter)

# 3> refarce the following secentences with escape function
letter=print("Dear harry,\n\tThis python course is nice.\n\t\tThanks!")

# 4>find double space in program
a="today is sunday  & i love funday"
print(a.find("  "))

# 5>replace double space with triple space
a="today is sunday  & i love funday"
print(a.replace("  ","    "))