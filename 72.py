# fungsi untuk mengganti isi elemen dari list menjadi kategori "balita" atau "bukan balita" berdasarkan data umur
def kategorisasi(umur_list):
    i = 0
    while i < len(umur_list):
        if umur_list[i] <= 5:
            umur_list[i] = 'balita'
        else:
            umur_list[i] = 'bukan balita'
        i += 1

# fungsi print
def print_list(umur_list):
    for x in umur_list:
        print(x)
        
n = int(input()); l = list()
for i in range(n):
    umur = int(input())
    l.append(umur)

kategorisasi(l)
print_list(l)