# input dan casting tipe data
tahun = int(input())
# ekspresi dari operasi logika
# kabisat adalah 'tahun yang habis dibagi 400' atau 'habis dibagi 4' dan 'tidak habis dibagi 100'.
kabisat = tahun%400 == 0 or tahun%4 == 0 and tahun%100 != 0
# output
print(kabisat)