# çokgen  çizme 
import turtle   
import time
t=turtle.Turtle()
t.speed(5) 
sc=turtle.Screen()  # nesne olustur (sc)
sc.bgcolor("black")

t.begin_fill()
t.color("red")       # üçgen
t.circle(50,steps=3)    

t.end_fill()
#--------------------------
t.up()
t.goto(150,150)

t.begin_fill()     # kare
t.color("blue")
t.circle(50,steps=4)

t.end_fill()
#--------------------------
t.up()
t.goto(-150,150)

t.begin_fill()        # beşgen
t.color("yellow")
t.circle(50,steps=5)

t.end_fill()

#--------------------------
t.up()
t.goto(-150,-150)

t.begin_fill()
t.color("grey")
t.circle(50,steps=6)

t.end_fill()

#--------------------------
t.up()
t.goto(150,-150)

t.begin_fill()
t.color("orange")       #sekizgen
t.circle(50,steps=8)

t.end_fill()


time.sleep(1)

