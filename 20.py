# input
from ipaddress import ip_address


a = input()
b = input()
# casting tipe data
a1 = int(a)
b1 = int(b)
# pengkondisian dan output
hasil = a1 - b1
if hasil < 0:
    hasil = abs(hasil)
print("Nilai mutlak dari",a1,"dikurangi",b1,"adalah",hasil)