

import turtle
'''
t=turtle.Turtle()
for i in range(5):
    t.forward(100)
    t.right(144)
turtle.done()
'''
t=turtle.Turtle()
def luo(n):
    if n>0:
        t.forward(n)
        t.left(90)
        luo(n-10)

luo(400)
