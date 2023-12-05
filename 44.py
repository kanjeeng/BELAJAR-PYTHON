a = int(input())

if a == 0:
      print('nol')
elif a > 0:
    print('positif')
    
    if a & 1:
       print(a, 'adalah ganjil')
    else:
       print(a, 'adalah genap')
       
else:
    print('negatif')
    if a & 1:
        print(a, 'adalah ganjil')
    else:
        print(a, 'adalah genap')