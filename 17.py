# input
a = input()
b = input()
operator = input()
# casting tipe data
a1 = float(a)
b1 = float(b)
# pengkondisian dan output
hasil = 0
if operator == "+":
  hasil = a1 + b1
elif operator == "-":
  hasil = a1 - b1
elif operator == "*":
  hasil = a1 * b1
elif operator == "/":
  hasil = a1 / b1
print(a1, operator, b1,"=",hasil)