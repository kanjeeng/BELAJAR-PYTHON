# input dan casting tipe data
kelakuan_buruk = (input())
prestasi = (input())
rata2 = float(input())

# ekspresi dari operator logika
ekspresi = (kelakuan_buruk == "TIDAK" or prestasi == "YA") and rata2 > 80
# pengkondisian dan output
if ekspresi:
	print ("Selamat, anda siswa terpuji!")
else :
	print ("Maaf, berusahalah lebih giat lagi")
 

