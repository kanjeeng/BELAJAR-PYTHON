x = int(input())

if x % 3 == 0 and x % 5 != 0:
    print(x, 'habis dibagi 3')
elif x % 5 == 0 and x % 3 != 0:
    print(x, 'habis dibagi 5')
elif x % 5 == 0 and x % 3 == 0:
    print(x, 'habis dibagi 3 dan 5')
else:
    print(x, 'tidak habis dibagi 3 atau 5')