def printMenu():
  print("1. es teh manis: 50")
  print("2. es kelapa: 100")
  print("3. es jeruk: 150")

# fungsi option
def option(x):
    if x == 0:
        printMenu()
    elif x == 2 :
        print("Rp.100")
    elif x == 3:
        print("Rp.150")
    elif x == 1:
        print("Rp.50")
    else:
        print("pilihan tidak tersedia")
x = int(input())
option(x)   
