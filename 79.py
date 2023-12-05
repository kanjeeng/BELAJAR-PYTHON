# Fungsi gantiVokal, mengganti huruf vokal di text dengan string X
def gantiVokal(text, X):
    # daftar huruf vokal
    vokal = ['a', 'i', 'u', 'e', 'o']
    # untuk setiap huruf vokal di text, ganti dengan K. Gunakan string method replace
    for i in vokal :
        text = text.replace(i, X)
    # return
    return text

# Main program
# input baris pertama dan lakukan split
N, K = input().split()

# perulangan untuk input N baris berikutnya
for i in range(int(N)):     # pahami int(N) di sini!
    # input nama bunga
    bunga = input()
    # panggil fungsi gantiVokal
    hasil = gantiVokal(bunga, K)
    # ouput
    print(hasil)