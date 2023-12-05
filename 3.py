# pendefinisian fungsi
def pembuangan_spasi_kosong(string):
    return string.replace(" ", "")

# input
string1 = input()
string2 = input()

# memanggil fungsi
hasil1 = pembuangan_spasi_kosong(string1)
hasil2 = pembuangan_spasi_kosong(string2)

# output
print(hasil1+""+hasil2)