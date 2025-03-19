# çember çizmek
import turtle
import time
t=turtle.Turtle()
t.speed(9) 
form=turtle.Screen()
form.bgcolor("grey")
form.title("circle")
t.shape("classic")
t.circle(100)  #radius (yarıçapı)
t.circle(110,90)  # yarıçapı ve kaç derece gitsin
t.circle(120,360)
t.circle(125,360)

#t.reset()   # çizilenleri silme
t.circle(150,steps=6) #altıgen çizme
#-------------------------------------------
t.reset()
bb=turtle.Screen()
bb.bgcolor("white")
t.speed(0)
for i in range(150):
    if i%2==0:
        t.color("red","green")
        t.circle(i)
    else:
        t.color("blue","white")


time.sleep(2)
