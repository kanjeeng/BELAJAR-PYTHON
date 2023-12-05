# fungsi untuk membuat dictionary dari dua list
def create_dict(l1, l2):
    return dict(zip(l1, l2))

# membaca input dua buah list of string
nim = input().split()
nama = input().split()

# membuat dictionary 1 dari 2 buah list
student = create_dict(nim, nama)

# membaca input nim mahasiswa hadir menjadi list
nim_hadir = input().split()

# mencari mahasiswa yang tidak hadir
for n in student:
    if n not in nim_hadir:
        print(n, student[n], "tidak hadir")