# fungsi
def hitungVolumeSilinder(r,t):
  volume = 3.14* r * r * t
  return volume

# main program
jari2 = int(input())
tinggi = int(input())
hasil = hitungVolumeSilinder(jari2, tinggi)
print(hasil)