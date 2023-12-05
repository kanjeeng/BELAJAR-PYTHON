# Membaca input banyaknya mobil dan casting
n = int(input())

# Membuat dict dari input dengan loop for
mobil = {}
for i in range(n):
    # input
    merek = input()
    harga = float(input())
    # menambahkan elemen dict dengan merek sebagai key dan harga sebagai value
    mobil[merek] = harga

# mencetak dict dengan loop for
for key, value in mobil.items():
    print(key,':', value)

# menghitung harga termahal
key_max = max(mobil, key = mobil.get)
value_max = mobil[key_max]

# mencetak mobil dengan harga termahal
print("Harga termahal: {} ({})".format(key_max, value_max))

# menghitung harga termahal
key_min = min(mobil, key = mobil.get)
value_min = mobil[key_min]

# mencetak mobil dengan harga termurah
print("Harga termurah: {} ({})".format(key_min, value_min))

# menghitung rata-rata harga mobil
rerata = sum(mobil.values()) / len(mobil.values())

# mencetak rata-rata harga mobil
print("Rata-rata harga: {:.2f}".format(rerata))
