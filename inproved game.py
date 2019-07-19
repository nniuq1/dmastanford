from gpiozero import Button, LED
from time import sleep
import random
lb1 = LED(17)
lb1 = LED(22)
b1 = Button(4)
b2 = Button(21)

time = 0
for i in range (8):
    choise = random.randint(0,6)
    if choise == 1:
        lb1.on()
        while b1.button.off():
            sleep(0.1)
            time += 0.1
        lb2()
    elif choise == 2:
        lb2.on()
        while b2.button.off():
            sleep(0.1)
            time += 0.1
        lb1.off()
    else:
        sleep(0.25)
    sleep(1)

