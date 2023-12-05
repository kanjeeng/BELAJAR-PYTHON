# fungsi faktorial
def faktorial(n):
    hasil = 1
    i = n
    while i > 0:
        hasil *= i
        i -= 1
    return hasil

# fungsi kombinasi
def kombinasi(a, b):
    hasil = faktorial(a)/(faktorial(b)*(faktorial(a-b)))
    hasil = int(hasil)
    return hasil

a = int(input())
b = int(input())
print(kombinasi(a,b))