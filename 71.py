# input baris pertama dan casting tipe data
n = int(input())
# inisialisasi sebuah list kosong
l = []
# input untuk n baris berikutnya, simpan ke dalam list yang telah dibuat
for i in range(n):
    nilai = int(input())
    l.append(nilai)

# panggil fungsi set() untuk menghasilkan elemen unik dari list
s = set(l)

# tampilkan setiap elemen dari set
for i in sorted(s):
    print(i)