# membuat list 
list_a = ["java", "c++", "python", "go"]
list_b = ["java", "c++", "python", "go"]

# mengurutkan list_a membesar
list_a.sort(key = len)

# mengurutkan list_b mengecil
list_b.sort(key = len, reverse=True)

# mencetak list
print(list_a)
print(list_b)