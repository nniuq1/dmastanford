from gpiozero import Button, LED
from time import sleep
import random
lb2 = LED(25)
lb1 = LED(17)
b1 = Button(4)
b2 = Button(21)
rang = 8
time = 0
while rang > 0:
    choise = random.randint(0,4)
    if choise == 1:
        lb1.on()
        while not b1.is_pressed:
            sleep(0.1)
            time += 0.1
        lb1.off()
    elif choise == 2:
        lb2.on()
        while not b2.is_pressed:
            sleep(0.1)
            time += 0.1
        lb2.off()
    else:
        sleep(0.25)
        rang += 1
    sleep(1)
    rang -= 1
print(time)

