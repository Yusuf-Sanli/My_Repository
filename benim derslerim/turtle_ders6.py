#çember çizerek renkli şekiller 
import turtle   
import time
t=turtle.Turtle()
t.speed(0) 

gg=turtle.Screen()
gg.bgcolor("grey")

for i in range(100):
    if i%2==0:
        t.color("yellow")
        t.circle(i)
    elif i%5==0:
        t.color("gray")
        t.circle(i)
    else :
        t.color("yellow")   
        t.circle(i)
t.reset()  
t.speed(0)
for i in range(100):
    if i%2==0:
        t.color("blue")
        t.circle(i,steps=8)
    elif i%5==0:
        t.color("green")
        t.circle(i,steps=8)
    else :
        t.color("red")   
        t.circle(i)
time.sleep(1)
