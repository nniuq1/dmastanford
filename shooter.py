from gpiozero import Button, LED
from time import sleep
import random
shoot = Button(21)
left = Button(4)
right = Button(17)
facing = "right"
pp = 6
e1 = 20
b1f = ""
e2 = 20
b2f = ""
e3 = 20
b3f = ""
b1 = 20
b2 = 20
b3 = 20
run = True
while run:
    sleep(1)
    if b1 > pp:
        b1 += 1
    if b1 < pp:
        b1 -= 1
    if b2 > pp:
        b2 += 1
    if b2 < pp:
        b2 -= 1
    if b3 > pp:
        b3 += 1
    if shoot.is_pressed:
        b3 = b2
        b3f = b2f
        b2 = b1
        b2f = b1f
        if facing == "right":
            b1 = pp + 1
            b1f = facing 
        else:
            b1 = pp - 1
            b1f = facing
    elif right.is_pressed:
        facing = "right"
        pp += 1
    elif left.is_pressed:
        facing = "left"
        pp -= 1
    if b3 < pp:
        b3 -= 1
    if e1 == b1:
        e1 = e2
        e2 = e3
        e3 = 20
        b1 = 20
    if e1 == b2:
        e1 = e2
        e2 = e3
        e3 = 20
        b2 = 20
    if e1 == b3:
        e1 = e2
        e2 = e3
        e3 = 20
        b3 = 20
    if e2 == b1:
        e2 = e3
        e3 = 20
        b1 = 20
    if e2 == b2:
        e2 = e3
        e3 = 20
        b2 = 20
    if e2 == b3:
        e2 = e3
        e3 = 20
        b3 = 20
    if e3 == b1:
        e3 = 20
        b1 = 20
    if e3 == b2:
        e3 = 20
        b2 = 20
    if e3 == b3:
        e3 = 20
        b3 = 20
    if e1 > pp:
        e1 -= 1
    if e1 < pp:
        e1 += 1
    if e2 > pp:
        e2 -= 1
    if e2 < pp:
        e2 += 1
    if e3 > pp:
        e3 -= 1
    if e3 < pp:
        e3 += 1
    if e1 == b1:
        e1 = e2
        e2 = e3
        e3 = 20
        b1 = 20
    if e1 == b2:
        e1 = e2
        e2 = e3
        e3 = 20
        b2 = 20
    if e1 == b3:
        e1 = e2
        e2 = e3
        e3 = 20
        b3 = 20
    if e2 == b1:
        e2 = e3
        e3 = 20
        b1 = 20
    if e2 == b2:
        e2 = e3
        e3 = 20
        b2 = 20
    if e2 == b3:
        e2 = e3
        e3 = 20
        b3 = 20
    if e3 == b1:
        e3 = 20
        b1 = 20
    if e3 == b2:
        e3 = 20
        b2 = 20
    if e3 == b3:
        e3 = 20
        b3 = 20
    if e3 == 20:
        newe = random.randint(1,2)
        if newe == 1:
            were = random.randint(1,2)
            if were == 1:
                e3 = e2
                e2 = e1
                e1 = 1
            else:
                e3 = e2
                e2 = e1
                e1 = 11
    for f in range (11):
        i = f+1
        if b1 == i and b1f == "left" or b2 == i and b2f == "left" or b3 == i and b2f == "left":
            print ("<", end = "")
        elif b1 == i and b1f == "right" or b2 == i and b2f == "right" or b3 == i and b3f == "right":
            print (">", end = "")
        elif e1 == i or e2 == i or e3 == i:
            print ("A", end = "")
        elif pp == i and facing == "right":
            print("b",end = "")
        elif pp == i and facing == "left":
            print("d",end = "")
        else:
            print("_",end = "")
    print("")
    if e1 == pp or e2 == pp or e3 == pp:
        run = False
