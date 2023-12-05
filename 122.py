 # membuat list 
list_a = [1, 2, 3, 4, 5]

# inisialisasi
jumlah = 0

# menjumlahkan dengan perulangan
for bilangan in list_a:
    if bilangan%2 != 0:
        jumlah += bilangan
    
# mencetak jumlah
print(jumlah)
