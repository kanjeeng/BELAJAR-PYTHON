# draw square in Python Turtle
import turtle
#Masukkan banyak sisi
b = int(input("Masukkan banyak sisi ? "))

#Masukkan panjang sisi
p = int(input("Masukkan panjang sisi ? "))

#Perulangan
for i in range(b):
    turtle.left(360 / b)
    turtle.forward(p)
    

turtle.done()