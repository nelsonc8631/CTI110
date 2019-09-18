"""this program will draw to diamonds and fill them with the color green
using the turtle function"""
##9/18/2019
#CTI-110 P2H2W2_TurtleGraphic
#Christopher Nelson

import turtle
turtle.speed(1)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(45,45)
turtle.goto(90,0)
turtle.goto(45,-45)
turtle.goto(-45,45)
turtle.goto(-90,0)
turtle.goto(-45,-45)
turtle.goto(45,45)
turtle.end_fill()

