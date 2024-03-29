import turtle

import colorgram
colors=colorgram.extract("painting.jpeg",12)
list1=[]
def tupless():
    for i in colors:
        r=i.rgb.r
        g=i.rgb.g
        b=i.rgb.b
        new_color=(r,g,b)
        list1.append(new_color)
tupless()
print(list1)


from turtle import Turtle,Screen
import random
turtle.colormode(255)

lola=Turtle()
lola.setheading(225)
lola.penup()
lola.forward(250)
lola.setheading(0)
j=5
while j<=50:
    for i in range(0,10):
        lola.dot(20,random.choice(list1))
        lola.penup()
        lola.forward(50)
    lola.setheading(180)
    lola.penup()
    lola.forward(500)
    lola.setheading(90)
    lola.penup()
    lola.forward(50)
    lola.setheading(0)
    j+=5



screen=Screen()
screen.exitonclick()
