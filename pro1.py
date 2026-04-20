#1>mult-line print of content togerther at once
print('''
Trees are one of the most important natural resources on Earth.
They provide us with fresh, clean oxygen necessary for breathing.
Trees absorb carbon dioxide, reducing greenhouse gases and mitigating climate change.
They act as natural air purifiers by absorbing harmful pollutants.
Trees play a crucial role in preventing soil erosion with their strong roots.
They offer shade and cooler air, helping to reduce the temperature in urban areas.
Many species of birds, insects, and animals depend on trees for shelter.
We receive valuable resources from trees, including fruits, wood, medicine, and rubber.

      ''')
#2>table f 5
for i in range (0,10):
    print(5*i)
#3>   
import time
print(time.time())
#4>
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(index, voice.name, voice.id)
engine.setProperty('voice', voices[1].id)
engine.say("Hey GOODMORNING! how are you doing today")
engine.runAndWait()
5
import os

# specify the directory path (use '.' for current directory)
path = "."

try:
    files = os.listdir(path)
    
    print("Files and directories in", path, ":\n")
    for item in files:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You don't have permission to access this directory.")

