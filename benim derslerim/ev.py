# python turtle ile ev yapımı :

import turtle
import time

k=turtle.Turtle()
k.speed(2)
k.width(5)
k.shape("circle")
ev_konf={"duvar1":90,"duvar2":90,"duvar30":90,"duvar4":90,"cati1":135,"cati2":90}

for x,y in ev_konf.items():
    if "duvar" in x:
        k.color("green")
        k.right(y)
        k.forward(250)
    elif "cati" in x:
        k.color("red")
        k.left(y)
        k.forward(181)
time.sleep(1)







