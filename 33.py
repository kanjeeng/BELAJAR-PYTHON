x = int(input())
# fungsi even(nilai)
def even(nilai):
    hasil = nilai % 2 == 0
    return hasil

# fungsi odd(nilai)
def odd(nilai):
    hasil = nilai % 2 != 0
    return hasil

print(even(x))
print(odd(x))