def konversiWaktu(detik):
  jam = detik // 3600
  detik = detik % 3600
  menit = detik // 60
  detik = detik % 60
  return jam, menit, detik

detik = int(input())
jam, menit, detik = konversiWaktu(detik)
print (jam, "jam", menit, "menit", detik, "detik")