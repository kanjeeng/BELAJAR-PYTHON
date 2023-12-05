# fungsi untuk mencari banyaknya kemunculan x di dalam data_list
def counting(data_list, x):
    # panggil fungsi count di sini
    hasil = data_list.count(x)
    # return kan hasil counting
    return hasil

list1 = [2,3,4,3,10,3,5,6,3]
x = 3
print("The count of elemen",x," is ",counting(list1 ,x))