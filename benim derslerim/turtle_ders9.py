# analog saat 

import turtle   
import time
t=turtle.Turtle()
ss=turtle.Screen()  # nesne oluşturma
ss.setup(width=450,height=450)
ss.bgcolor("blue")
ss.title("Analog saat uygulamasi")
ss.tracer(0)
kalem=turtle.Turtle()    # nesne oluşturma
kalem.speed(0)
kalem.pensize(3)


def Cizim(saat,dakika,saniye,kalem):
    kalem.begin_fill()
    kalem.color("black")
    kalem.up()
    kalem.goto(0,210)
    kalem.setheading(180)
    kalem.color("red")
    kalem.pendown()
    kalem.circle(210)
    kalem.end_fill()

    kalem.penup()
    kalem.goto(0,0)
    kalem.setheading(90)
    kalem.begin_fill()
    kalem.color("black")
    for i in range(12):
        kalem.fd(190)
        kalem.pendown()
        kalem.fd(20)
        kalem.penup()
        kalem.goto(0,0)
        kalem.rt(30)

    kalem.end_fill()
 
 #saat   
   
    kalem.up()
    kalem.goto(0,0)
    kalem.color("blue")
    kalem.setheading(90)
    bilgi=(saat/12)*360
    kalem.rt(bilgi)
    kalem.pendown()
    kalem.fd(90)
#dakika
    kalem.end_fill()
    kalem.up()
    kalem.goto(0,0)
    kalem.color("yellow")
    kalem.setheading(90)
    bilgi=(dakika/60)*360
    kalem.rt(bilgi)
    kalem.pendown()
    kalem.fd(120)
#saniye
    kalem.end_fill()
    kalem.up()
    kalem.goto(0,0)
    kalem.color("grey")
    kalem.setheading(90)
    bilgi=(saniye/60)*360
    kalem.rt(bilgi)
    kalem.pendown()
    kalem.fd(150)

while True:


 saat=int(time.strftime("%I"))
 dakika=int(time.strftime("%M"))
 saniye=int(time.strftime("%S")) 

 Cizim(saat,dakika,saniye,kalem)
 ss.update()
 kalem.clear()


time.sleep(2)