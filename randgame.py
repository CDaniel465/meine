import random

x = random.randrange(0,100)
y = random.randrange(0,100)
z = random.randrange(0,100)
xwin = False
ywin = False
win = False

while True:
    xin = input("gib x coordinate ")
    yin = input("gib jetzt y coordinate ")
    
        
    if int(xin) > x:
        print("fuer x ist "+ xin +" zu groß")
    if int(xin) < x:
        print("fuer x ist"+ xin + "zu klein")
    if xwin == False:
        if int(xin) == x:
            print("x ist richtg")
            xwin = True
    if xin == "x":   
        break

    
    if int(yin) > y:
        print("fuer y ist "+yin+" zu groß")
    if int(yin) < y:
        print("fuer y ist "+yin+" zu klein")
    if ywin == False:
        if int(yin) == y:
            print("y ist richtig")
            ywin = True

    if int(yin) ==y and int(xin) == x:
        win = True

    if win == True:
        break


print("ende")
