r = float(input())
R = float(input())
t = float(input())

phi = 3.14

volume = 1/3*phi*t*(R**2 + R*r+r**2)

print('{:.2f}'.format(volume))