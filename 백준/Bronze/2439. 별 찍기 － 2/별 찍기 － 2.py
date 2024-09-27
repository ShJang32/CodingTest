n = int(input())

for num in range(1, n+1):
    print(' ' * (n-num) + '*' * num)
    num += 1