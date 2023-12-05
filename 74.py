# input

inputBilangan = input()
# panggil string method split dan simpan ke dalam listBilangan
listBilangan = inputBilangan.split()

jumlah = 0
# lakukan perulangan sejumlah elemen list
for i in listBilangan:
    # lakukan casting dan penjumlahan
    jumlah = sum(map(float,listBilangan))
# output
print(jumlah)