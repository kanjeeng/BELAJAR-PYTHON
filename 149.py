# draw square in Python Turtle
import turtle
kata = 0
# Input
while kata != "stop":
    kata = input()
#bergerak ke atas sebesar 50 satuan
    if kata == "U":
        turtle.left(90)
        turtle.forward(50)
#bergerak ke bawah sebesar 50 satuan
    if kata == "D":
        turtle.left(90)
        turtle.forward(50)
#bergerak ke kiri sebesar 50 satuan
    if kata == "L":
        turtle.left(90)
        turtle.forward(50)
#bergerak ke kanan sebesar 50 satuan
    if kata == "R":
        turtle.left(90)
        turtle.forward(50)
turtle.done()