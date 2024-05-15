from turtle import *


#we want to paint a house

#step 1: draw a square
width(7)
color ("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end the square

forward(70)
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)  #height of the door


penup()
goto(200, 200)
pendown()

color("red")
right(150)
forward(200)
left(120)
forward(200)

color("purple")
left(30)
forward(80)

#window
color("green")
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

#window 2
penup()
goto(200, 120)
pendown()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)



exitonclick()