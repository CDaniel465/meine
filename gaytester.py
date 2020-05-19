import sys
import random
args=sys.argv
i = 0
name = args[1]
while i < 3 :
    number = random.randrange(0,100)
    if number<50:
        print(name+" du bist Schwul")
        print(number)
        i+=1
    else:   
        print(name+" du bist nicht Schwul")
        print(number)
        i+=1
