#Author: Hao CHEN
#Date: May 2014

import turtle             
userInput = int(input("How many sides do you want your polygon to have:"))
 
polygon = turtle.Turtle()    
count = 0
angle = 180 - (( userInput - 2 ) * 180 / userInput )
while count != userInput:
    polygon.forward(50) 
    polygon.left(angle) 
    count = count + 1
