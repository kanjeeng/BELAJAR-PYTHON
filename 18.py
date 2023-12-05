# input
from re import A


a = input()
b = input()
# casting tipe data
a1 = int(a)
b1 = int(b)
# pengkondisian dan output
if a1<b1:
    x = a1  
    y = b1
else:
    x = b1
    y = a1
print("x =",x,"dan y =",y)