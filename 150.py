# draw square in Python Turtle
import turtle

# Input
sisi = int(input("Masukkan Ukuran bintang:"))

# Output
for i in range (5):
    turtle.forward(sisi)
    turtle.right(144)

turtle.done()