# import modul
import math
# input 
a = input()
b = input()
#casting tipe data
a1 = int(a)
b1 = int(b)
# panggil fungsi faktorial untuk mencari nilai faktorial a dan b
f_a = math.factorial(a1)
f_b = math.factorial(b1)
# panggil fungsi faktorial untuk mencari nilai a permutasi b
p = int(f_a/math.factorial(a1-b1))
# panggil fungsi faktorial untuk mencari nilai a kombinasi b
c = int(f_a/((math.factorial(a1-b1)) * f_b))
# output
print(a+"! =",f_a,"dan",b+"! =",f_b)
print("permutasi("+a+","+b+") =",p)
print("kombinasi("+a+","+b+") =",c)
