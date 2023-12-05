# input kata pertama
kata = input()

# pembuatan dictionary, input kata, menghitung banyak karakter
# menghitung banyak huruf
dict1 = {}
while kata != "stop":
    banyak_huruf = len(kata)
    dict1[kata] = banyak_huruf
    kata = input()

# cetak dictionary
print(dict1)