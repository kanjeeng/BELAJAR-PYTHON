#input
a=str(input())
b=str(input())
c=str(input())
d=str(input())

# buat tuple tup1 dan tup2
tup1 =(a,b,c,d)
tup2 = (tup1[2:4]*3)

print('nilai tuple baru',(tup1 + tup2))