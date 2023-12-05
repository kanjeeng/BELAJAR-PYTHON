# input

sentence = input()

# panggil string method split dan simpan ke dalam list
listString = sentence.split()

# lakukan perulangan sejumlah elemen list
for i in listString:
    # panggil string method isdigit untuk pengecekan elemen list
    if  i.isdigit():
        # output
     print(i)