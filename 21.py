# input
x1 = input()
x2 = input()
x3 = input()
# casting tipe data
ix1 = int(x1)
ix2 = int(x2)
ix3 = int(x3)
# pengkondisian dan output
if ix1 + ix2 > ix3:
    if ix3 + ix2 >ix1 :
        if ix1 + ix3 > ix2:
            print("Sisi segitiga")
        else:
            print("Bukan sisi segitiga")
    else:
        print("Bukan sisi segitiga")
else:
    print("Bukan sisi segitiga")