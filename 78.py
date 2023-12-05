# input
sentence = input()

# list yang berisi daftar huruf vokal
vowel = ["a","i","u","e","o"]

# inisialisasi sebuah string kosong untuk menyimpan hasil perubahan
new_sentence = []

# lakukan pengecekan untuk setiap karakter pada string
for s in sentence:
    # cek apabila s ada di list vokal maka
    if s in vowel:
        new_sentence += s.upper()
    else:   # apabila s adalah konsonan
        new_sentence += "_"
        
# output
print(''.join(new_sentence))