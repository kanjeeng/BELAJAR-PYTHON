# Membaca input n dan casting
from shutil import move


n = int(input())

# Membuat dict dari input
movie = {}

for i in range(n):
    # input movie dan budget
    title = input()
    budget = float(input())
    # menambah elemen ke dict dengan judul movie sebagai key dan budget sebagai value
    movie[title] = budget

# mencetak dict
for key in movie:
    print(key, movie[key])

# menghitung rata-rata budget
rerata = sum(movie.values())/len(movie.values())

# output
print("Rata-rata budget: {:.2f}".format(rerata))
