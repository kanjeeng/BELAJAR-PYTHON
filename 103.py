# membuat dictionary
dict_angka = {'a': 11, 'b': 22, 'c' : 33, 'd': 44}

# inisialisasi
jumlah = 0

# menjumlahkan dengan perulangan
for k, v in dict_angka.items():
    jumlah += v

# mencetak 
print(jumlah)