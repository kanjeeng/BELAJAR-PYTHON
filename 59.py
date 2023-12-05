# input dan casting
a=int(input())
b=int(input())
c=int(input())
d=int(input())
# simpan dua nilai pertama ke dalam list
lis1 = [a, b]
# simpan dua nilai sisanya dan list1 ke dalam tuple
tup1 = ([c,d],[lis1])

# modifikasi isi tuple
tup1[0][0]=10
tup1[0][1]=sum(lis1)

# output
print('nilai tuple baru', (c,d,tup1[0]))