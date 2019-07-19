from gpiozero import Button, LED
from time import sleep
import random
green = LED(25)
red = LED(17)
p1 = Button(4)
p2 = Button(21)
p1d = 0
p2d = 0
while p1d < 10 and p2d < 10:
    color = random.randint(1,2)
    tim = random.randint(10,100)
    if color == 1:
        red.on()
        for i in range(tim):
            if p1.is_pressed:
                p1d = 0
                print("p1 go back")
            if p2.is_pressed:
                p2d = 0
                print("p2 go back")
            sleep (.1)
        red.off()
    else:
        green.on()
        for i in range(tim):
            if p1.is_pressed:
                p1d += 0.1
            if p2.is_pressed:
                p2d += 0.1
            sleep (.1)
        green.off()
    print(p1d)
    print(p2d)
