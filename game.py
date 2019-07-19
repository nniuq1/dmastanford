from gpiozero import Button
Player1 = Button(21)
Player2 = Button(4)
p1 = 0
p2 = 0
win1 = True
while win1:
    if Player1.is_pressed:
        p1 += 1
        while Player1.is_pressed:
            print ("dong")
    if Player2.is_pressed:
        p2 += 1
        while Player2.is_pressed:
            print ("ding")
    if p2 == 20:
        print ("p2 win")
        win1 = False
    if p1 == 20:
        print ("p1 win")
        win1 = False
