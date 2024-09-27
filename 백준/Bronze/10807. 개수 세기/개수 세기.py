n = int(input())
arr = list(map(int, input().split()))
v = int(input())
total = 0

for num in arr:
    if num == v:
        total += 1

print(total)