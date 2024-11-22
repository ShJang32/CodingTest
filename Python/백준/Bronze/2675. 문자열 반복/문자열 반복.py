t = int(input())
p = ''

for i in range(t):
    r, s = input().split()

    for j in s:
        for k in range(int(r)):
            p += j
    p += '\n'

print(p)