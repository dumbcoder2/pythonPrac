# 3>Quiz game in Python.
# import random 

you=input("enter your name")
start=input("enter 1 for start and 0 for end")
point=0
quizz ={"what color is sky?":"blue",
          "what color is orange?":"orange",
    "What is the capital of India?": "Delhi",
    "Who developed Python?": "Guido van Rossum",
    "What is 2 + 2?": "4"}

if(start=="1"):
    for question in quizz:
     print(question)
     answer = input("Enter your answer: ")
     if(answer.lower()==quizz[question].lower()):
        
        print("your right")
        point+=1
        
     else:
        print("your wrong")
    
    print(f"\nYour total points are: {point}")  
else:
   print("your exit for game!")         