# fungsi reverse_text
def reverse_text(text):
    # inisialisasi suatu string kosong
    result = ''
    # lakukan penelusuran untuk setiap karakter pada string
    for i in text:
        # susun secara terbalik dengan operasi concatenate
        result = i + result
    # return value
    return result

text = input()
print(reverse_text(text))