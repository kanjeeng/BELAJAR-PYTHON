# input n
n = int(input())
# input n baris berikutnya dan output
for i in range (0, n) :
    tahun = int(input())
    kabisat = tahun % 400 == 0 or tahun % 4 == 0 and tahun % 100 != 0
    print(kabisat)