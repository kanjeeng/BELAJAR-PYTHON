c = 0
inp = int(input())
while c<inp:
    try:
        a, b = map(int, input().split())
        print(a % b)
        c+=1
    except Exception as e:
        print(e)