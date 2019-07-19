from gpiozero import Button, LED
from time import sleep
import random
jump = Button(4)
c1 = -1
c2 = -1
c3 = -1
c4 = -1
c5 = -1
c6 = -1
c7 = -1
c8 = -1
pp = 2
jumping = 0
while True:
    sleep (1)
    jumping -= 1
    c1 -= 1
    c2 -= 1
    c3 -= 1
    c4 -= 1
    c5 -= 1
    c6 -= 1
    c7 -= 1
    c8 -= 1
    if jump.is_pressed and jumping < 1:
        jumping = 4
    if c1<10 and c2<9:
        newe = random.randint(1,3)
        if newe == 1:
            c8 = c7
            c7 = c6
            c6 = c5
            c5 = c4
            c4 = c3
            c3 = c2
            c2 = c1
            c1 = 11
    if jumping > 0:
            print("  0        ")
    else:
            print("           ")
    for f in range (11):
        i = f+1
        if c1 == f or c2 == f or c3 == f or c4 == f or c5 == f or c6 == f or c7 == f or c8 == f:
            print("t",end = "")
        elif pp == f and jumping < 1:
            print("0",end = "")
        else:
            print("_",end = "")
    print("")
