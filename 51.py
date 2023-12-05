sum = 0
while True:
    try:
        sum += int(input())
    except ValueError:
        print('Nilai tidak valid')
    except EOFError:
        print(sum)
        break