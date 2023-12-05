# fungsi faktorial
def faktorial(n):
    hasil = 1
    i = n
    while i > 0:
        hasil *= i
        i -= 1
    return hasil

# fungsi permutasi
def permutasi(a, b):
    hasil = faktorial(a)/faktorial(a - b)
    hasil = int(hasil)
    return hasil

a = int(input())
b = int(input())
print(permutasi(a,b))

