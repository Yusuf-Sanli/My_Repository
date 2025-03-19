# up, down , goto fonksiyonları
import turtle   
import time
t=turtle.Turtle()
t.speed(1) 
t.forward(100)

t.goto(100,100) # 100  100  demek  x ve y noktası

t.undo()        # çizdiğimiz çizim geri geliyor
t.undo() 

t.up()    # kalemin ucunu kaldırır(yani çizmez ancak kalemin ucuc istenilen noktaya gider)

t.goto(100,100)   # kalemin ucunu  bu noktaya getir

t.down()    # kalemin ucunu indirme


# çember çizme

t.circle(50)
t.up()
t.goto(100,-100)
t.down()
t.circle(50)



time.sleep(1)


