# input dan type casting
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

# isi tuple dengan data dari masukan
tup1 = (a,b,c,d)

# hitung banyaknya e pada tuple
jum_e = tup1.count(e)

#output
print("Jumlah angka", e, "pada tuple", jum_e)