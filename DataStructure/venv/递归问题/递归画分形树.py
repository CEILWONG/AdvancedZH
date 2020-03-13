

import turtle

t=turtle.Turtle()

def tree(length):
    if length>2:
        t.forward(length)
        t.right(20)
        tree(length-20)
        t.left(40)
        tree(length-20)
        t.right(20)
        t.back(length)


tree(100)