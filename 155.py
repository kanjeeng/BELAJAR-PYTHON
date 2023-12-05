def triangle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
import turtle

# Inisialisasi
t = turtle.Turtle()

# Input
n = int(input("banyak lingkaran : "))
sisi = 100
x = 0
y = 0

for i in range(n):
    
        t.left(60)
        t.forward(sisi)

        t.right(120)
        t.forward(sisi)
        
        t.right(120)
        t.forward(sisi)

        if i <= 2:
            triangle(x, y)
            x = x - 200
            y = y
turtle.done()