# membaca data menjadi list
key1 = input().split(" ")
value1 = input().split(" ")
key2 = input().split(" ")
value2 = input().split(" ")

# membentuk dictionary 1
dict1 = dict(zip(key1, value1))

# membentuk dictionary 2
dict2 = dict(zip(key2, value2))

# user-defined fungsi menggabungkan dua dictionary
def update_dict(dict1, dict2):
    for k, v in dict2.items():
        dict1[k] = v

# menggabungkan dua dictionary
update_dict(dict1, dict2)

# cetak dictionary
print(dict1)