def fib(n):
    assert n >= 0, x
    
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)

while True:
    try:
        try:
            x = int(input())
            print('fib({}) = {}'.format(x, fib(x)))
        except AssertionError:
            print("Fibonacci",x,"tidak terdefinisi")
            break
    except:
        break