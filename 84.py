# fungsi untuk membuat dictionary dari dua list
def create_dict(l1, l2):
    return dict(zip(l1, l2))

# membaca input serangkaian kata bahasa Indonesia dipisahkan oleh spasi kosong
indonesia = input().split()

# membaca input serangkaian kata bahasa Inggrid dipisahkan oleh spasi kosong
inggris = input().split()

# membuat dictionary dari buah list dengan memanggil fungsi create_dict
kamus_in_en = create_dict(indonesia, inggris)

# membaca banyak n data uji dan casting
n = int(input())

# membaca data uji dan translasikan dengan for loop
for i in range(n):
    kata = input()
    print(kamus_in_en[kata])