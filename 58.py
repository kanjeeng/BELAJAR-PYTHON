# assign list pertama dan kedua
list1 = [5, 6, 7, 8]
list2 = [7, 8, 9, 10]
# input nilai x dan y, lakukan casting
x = int(input())
y = int(input())
# tambahakan elemen list sesuai deksripsi soal 
list2.append(list1[x])
list1.append(list2[y])
# output
print(list1)
print(list2)