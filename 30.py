# input n
n = int(input())
# input n baris berikutnya dan proses penjumlahan
jumlah = 0
for i in range (0, n) :
    bilangan = float(input())
    jumlah = jumlah + bilangan
# menghitung rata-rata
rataan = jumlah / n
# output
print(rataan)