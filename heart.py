import turtle as t 
import time
t.left(45)
t.forward(150)
for i in range(200):
    t.forward(1)
    t.left(1)
t.left(45)
for i in range(200):
    t.backward(1)
    t.left(1)
t.left(180)
t.forward(150)
t.sleep(5)