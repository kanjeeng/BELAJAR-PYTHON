# import modul math
import math
# input dan casting tipe data
a = int(input())
b = int(input())

# jumlahkan kuadrat dari a dan kuadrat dari b menggunakan fungsi pow()
jumlah = math.pow(a, 2) + math.pow(b, 2)

# hitung nilai c berdasarkan akar dari jumlah, gunakan fungsi sqrt()
c = math.sqrt(jumlah)

# output
print("Sisi miring adalah", c)