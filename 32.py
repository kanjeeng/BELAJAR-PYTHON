# fungsi untuk menghitung luas lingkaran
def luas_lingkaran(r):
    luas =  3.14 * r**2
    return luas
    
# input dan casting tipe data
r1 = float(input())
r2 = float(input())
r3 = float(input())

# hitung luas lingkaran
luas1 = luas_lingkaran(r1)
luas2 = luas_lingkaran(r2)
luas3 = luas_lingkaran(r3)

# output
print("Luas lingkaran 1 =",luas1)
print("Luas lingkaran 2 =",luas2)
print("Luas lingkaran 3 =",luas3)