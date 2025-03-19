# çizim yapma
import turtle   
import time

t=turtle.Turtle()
ss=turtle.Screen()
t.shape("turtle")
ss.bgcolor("white")

t.speed(0)
for i in range(40):
    t.circle(5*i)
    t.circle(-5*i)
    turtle.left(i)

t.reset()
color=["red","gray","white","orange","green","blue","violet"]
t.speed(0)
t.pensize(3)
for k in range(100):
    t.circle(5*k)
    t.circle(-5*k)
    t.left(k)
    t.color(color[k%7])

ss.mainloop()


