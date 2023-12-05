# membuat list 
list_a = [1, 2, 3, 4, 5]

# inisialisasi
jumlah = 0
banyaknya_elemen = len(list_a)

# menjumlahkan dengan perulangan
for bilangan in list_a:
    jumlah += bilangan
    
# mencetak nilai rata-rata
print(jumlah/banyaknya_elemen)
