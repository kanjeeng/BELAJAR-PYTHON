# draw square in Python Turtle
import turtle

# Input
keliling = int(input("Masukan Keliling ? "))
sisi = keliling / 4

# Output
turtle.left(45)
turtle.forward(sisi)     

turtle.left(90)
turtle.forward(sisi)   

turtle.left(90)
turtle.forward(sisi) 

turtle.left(90)
turtle.forward(sisi)
turtle.left(45)

turtle.done()