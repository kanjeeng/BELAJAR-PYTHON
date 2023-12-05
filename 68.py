
# lengkapi fungsi mencari x_data di dalam data_list berikut ini
def find(data_list, x_data):
    if x_data in data_list:
        print(data_list.index(x_data))
    else:
        print("data tidak ditemukan")

d_list = [13, 53, 93, 33, 83] 
d_cari = int(input())
find(d_list,d_cari)