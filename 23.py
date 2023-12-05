# input dan casting tipe data
x1 = int(input())
x2 = int(input())
x3 = int(input())
# pengkondisian dan output
kondisi = x3 + x2 >x1
kondisi = x3 + x1 >x2
kondisi = x1 + x2 >x3
if kondisi:
    print("Sisi segitiga")
else:
    print("Bukan sisi segitiga")