#input
a = input()
b = input()
c = input()
d = input()
#type casting
a1 = int(a)
b1 = int(b)
c1 = int(c)
d1 = int(d)

mylist=[a1,b1,c1,d1]

# penjumlahan
z = sum(mylist)

# nilai paling minimum 
x = min(mylist)

# nilai paling maksimum
y = max(mylist)

# banyaknya anggota didalam list
w = len(mylist)

print(w,x,y,z)
