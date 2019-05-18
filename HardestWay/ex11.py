print("How old are you?",end="") #We put a end=' ' at the end of each print line. This tells print to not end
#the line with a newline character and go to the next line.就是让我们的输入不要另起一行的意思：How old are you? 23
age = input()
print("How tall are you?",end = "")
height = input()
print("How much do you weight?", end = '')
weight = input()

print(f"So, you are {age} old, {height} tall and {weight} heavy")
#print("So, you are %s old, %s tall and %s heavy"%(age, height, weight))
