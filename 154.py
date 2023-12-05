# draw square in Python Turtle
import turtle

# Input
panjang = int(input("Masukkan Panjang ? "))
lebar = int(input("Masukkan Lebar ? "))

# Output
turtle.right(90)
turtle.forward(lebar)

turtle.right(90)
turtle.forward(panjang)

turtle.right(90)
turtle.forward(lebar)

turtle.right(90)
turtle.forward(panjang)

turtle.done()