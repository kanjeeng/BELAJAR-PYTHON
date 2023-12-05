# input banyaknya data dan casting
n = int(input())

# pembuatan dictionary kosong
grade = {}

# loop input dan menambahkan elemen dictionary
for i in range(n):
    # input dan unpacking list
    nim, nama, nilai = input().split()
    # casting
    nilai = int(nilai)
    # menambahkan elemen dictionary
    grade[nim] = [nama, nilai]

# cetak dictionary 
for k, v in grade.items():
    print(k, '=', v[0], v[1])