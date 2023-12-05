text = input()
idx = int(input())

try:
    print(text[idx])
except IndexError:
    print("string index out of range")