#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
clear()
up()
home()
color('black')
shape('arrow')
#smiley face eyes
goto(-100,200)
color('blue')
dot(70)
up()
forward(200)
dot(70)
home()

#smiley face nose
color('red')
fillcolor('red')
width(2)
down()
forward(25)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)

#smiley face big smile
up()
goto(-150,-75)
color('orange')
width(10)
shape('square')
down()
forward(300)

#smiley face head
up()
goto(0,-250)
color('green')
down()
circle(300)





