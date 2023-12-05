# input
sentence = input()

# casting menjadi list
listString = [i for i in sentence]

# lakukan perulangan untuk setiap elemen list
i = 0
while i < len(listString):
    # cek apabila genap, rubah menjadi huruf besar dengan string method upper
    if i % 2 == 0:
        listString[i] = sentence[i].upper()
    # increment
    i += 1

# panggil string method join untuk menggabungkan list menjadi string
for i in listString:
    hasil = ''.join(map(str, listString))

# output
print(hasil)