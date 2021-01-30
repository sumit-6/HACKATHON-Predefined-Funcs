from turtle import *
import numpy as np
import math
hideturtle()

def bluelines():
    screensize(2000,2000)
    hideturtle()
    speed(0)
    color('pink')
    for i in range(31):
        pu()
        goto(-15+i,-15)
        pd()
        goto(-15+i,15)
        pu()
    for j in range(31):
        pu()
        goto(-15,-15+j)
        pd()
        goto(15,-15+j)
        pu()


def setup():
    screensize()
    p=1
    hideturtle()
    speed(0)
    setworldcoordinates(-7,-7,7,7)
    setpos(0,0)
    clear()
    bluelines()
    setpos(0,0)
    setheading(0)
    pd()
    color('black')
    for i in range(15):
        setpos(0,0)
        fd(p)
        write(p)
        lt(90)
        setpos(0,0)
        fd(p)
        write(p)
        lt(90)
        setpos(0,0)
        fd(p)
        write(-p)
        lt(90)
        setpos(0,0)
        fd(p)
        write(-p)
        lt(90)
        p=p+1
setup()

def function_3(x):
    f=(np.cos((np.e)**(x/4)))
    return f
def fun_3(x):
    f=function_3(x)
    return f

a=15
x=-15
dx=0.05
while x<=a:
    x+=dx
    hideturtle()
    pensize(1)
    screensize(2000,2000)
    color('green')
    def draw_1(matA):
            pu()
            speed(0)
            goto(x,fun_3(x))
            pd()
            for point in matA:
                speed(0)
                goto(point[0],point[1])
    try:
        ayush=[[x+dx,fun_3(x+dx)]]
        draw_1(ayush)
    except(ValueError,ZeroDivisionError,TypeError):
        continue
