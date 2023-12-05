from re import X


def MinMax(x,y):
    if x > y :
        minimum = y
        maksimum = x
    else:
        minimum = x
        maksimum = y
    return minimum, maksimum

a = int(input())
b = int(input())
i,j = MinMax(a,b)
print("terbesar",j)
print("terkecil",i)