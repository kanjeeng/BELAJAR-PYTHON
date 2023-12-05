# input
r = input()
# casting tipe data
r1 = float(r)
# pengkondisian dan output
if r1%7 ==0:
    luas = 22/7 * r1 * r1
else:
    luas = 3.14 * r1 * r1
print("Luas lingkaran berjari jari",r1,"adalah",luas)