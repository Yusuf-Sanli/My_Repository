# belirli bir bölgeyi boyama
import turtle
import time
t=turtle.Turtle()
t.speed(0) 
t.begin_fill()  # boyamaya başlamak için
t.fillcolor("green")  # bölgenin rengi
for i in range(4):
    t.forward(200)
    t.left(90)

t.end_fill() # boyamayı bitirmek için

time.sleep(2)
