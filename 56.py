# perulangan untuk input 20 baris
for i in range(0, 20):
    # input dan casting tipe data
    bilangan = float(input())
    # percabangan dan output
    if i % 2 == 0 :
        print("{:.3f}".format(bilangan))
    else:
        print("{:.10f}".format(bilangan))