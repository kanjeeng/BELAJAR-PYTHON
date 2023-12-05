'''
Program ini menerima inputan berupa 1 buah bilangan bulat positif (0 sampai 100)
Program ini akan mengeluarkan indeks prestasi sesuai dengan kriteria berikut
81 .. 100 : A
71 .. 80  : AB
66 .. 70  : B
61 .. 65  : BC
51 .. 60  : C
41 .. 50  : D
0  .. 40  : E
Jika tidak masuk ke dalam kriteria, program akan mengeluarkan 'Nilai tidak valid'
'''

x = int(input())
if x >= 0 and x <= 100:
    if x >= 81 and x <= 100:
        print('A')
    if x >= 71 and x <= 80:
        print('AB')
    if x >= 66 and x <= 70:
        print('B')
    if x >= 61 and x <= 65:
        print('BC')
    if x >= 51 and x <= 60:
        print('C')
    if x >= 41 and x <= 50:
        print('D')
    if x >= 0 and x <= 40:
        print('E')
else:
    print('Nilai tidak valid')