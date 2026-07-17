# 1>file read and operation

# read text file
f=open("file.txt")
data=f.read()
print(data)
f.close()

# 2>read only specific line in file

f=open("file.txt")
line1=f.readline()
print(line1,type(line1))
f.close()


# 3>write text file
str="create a new file with write operation "

f=open("file2.txt","w")
f.write(str)
f.close()

# 4>append string in the file
str="\nappend the program in file"
f=open("file2.txt","a")
f.write(str)
f.close()

# 5>with statement no close statement
with open("file2.txt") as f:
    print(f.read())
 
# 1>find Twinkle in poem
with open("file.txt")as f:
    content=f.read()
     
    if("Twinkle" in content):
        print("there is word Twinkle in file")
    else:
        print("there is no word Twinkle in file")    
