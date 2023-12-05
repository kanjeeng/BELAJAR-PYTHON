# lengkapi fungsi membagi data_list menjadi positif_list dan negatif_list
def membagi(data_list, positif_list, negatif_list):
    for data in data_list:
        if data > 0:
            positif_list.append(data)
        elif data < 0:
            negatif_list.append(data)

d_list = [-13, 0, 53, -93, 33, -83, 0] 
p_list = list(); n_list = list()
membagi(d_list , p_list, n_list)
print("positif list:",p_list)
print("negatif list:",n_list)