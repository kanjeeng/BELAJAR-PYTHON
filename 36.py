# fungsi luas_alas
def luas_alas(r):
    luas = 3.14 * r ** 2
    return luas

# fungsi volume_kerucut
def volume_kerucut(r, t):
    luas = 1/3*luas_alas(r)*t 
    return luas

r = int(input())
t = int(input())
print(volume_kerucut(r,t))