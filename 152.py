import turtle

def drawCircle(t, x, y, r):
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Draw Circle
    t.circle(r)

t = turtle.Turtle()

# Input
n = int(input("banyak lingkaran : "))
r = int(input("jari jari lingkaran : "))

# Inisialisasi
diameter = r * 2
print("jarak antara lingkaran : ", diameter)
x = -200
y = 0

# Perulangan
for n in range(n):
    drawCircle(t, x, y, r)
    x=x+diameter
