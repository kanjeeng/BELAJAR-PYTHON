# baca n data dan casting
n = int(input())

# inisialisasi dict jumlah skor
jumlah_skor = {}
skor = 0

# loop pembuatan dict
for i in range(n):
    # membaca setiap baris dan mengubahnya menjadi list
    baris = input().split()
    # membuat key dari kolom pertama
    nama = baris[0]
    # membuat value dari kolom kedua sampai terakhir 
    jumlah_skor[nama] = [float(v) for v in baris[1:]]

# menghitung jumlah skor 
for k1, v1 in jumlah_skor.items():
    jumlah_skor[k1].append(sum(v1))

# cetak dictionary 
for k, v in jumlah_skor.items():
    print(k, end=' ')
    for i in v:
        print(i, end=' ')
    print()