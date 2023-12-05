# pembuatan dictionary kosong
daftar_kata = dict()

# input kata pertama
kata = input()

# input kata-kata berikutnya
while kata != "#":
    # memeriksa apakah kata tidak ada dalam daftar kata
    if kata not in daftar_kata:
        # menambahkan elemen dalam dictionary dengan value 1
        daftar_kata[kata] = 1
    else:
        daftar_kata[kata] += 1
    # input kata selanjutnya
    kata = input()

# cetak dictionary
print(daftar_kata)