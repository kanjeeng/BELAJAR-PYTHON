dict_angka = {'a': 11, 'b': 22, 'c' : 33, 'd': 44}
min_key = min(dict_angka, key=dict_angka.get)
print(min_key)
