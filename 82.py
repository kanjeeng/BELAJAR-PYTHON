# Membaca input n dan casting
n = int(input())

# Membuat dict dari input
movie = {}

for i in range(n):
    # input title dan budget
    title = input()
    budget = float(input())
    # menambah elemen dict dengan judul movie sebagai key dan budget sebagai value
    movie[title] = budget

# mencetak dict
for key in movie:
    print(key, movie[key])

# mencetak movie dengan budget termurah
key_min = min(movie, key = movie.get)
value_min = movie[key_min]
print("Budget termurah:", key_min, value_min)

# mencetak movie dengan budget termahal
key_max = max(movie, key = movie.get)
value_max = movie[key_max]
print("Budget termahal:", key_max, value_max)