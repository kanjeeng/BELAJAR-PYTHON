
# fungsi selamat
def selamat (kelakuan_buruk,prestasi,rata2):
    if (kelakuan_buruk == "TIDAK" or prestasi == "YA") and rata2 > 80:
        print("Selamat, anda siswa terpuji!")
    else:
        print("Maaf, berusahalah lebih giat lagi")
     
a = input()
b = input()
c = float(input())
selamat(a,b,c)

