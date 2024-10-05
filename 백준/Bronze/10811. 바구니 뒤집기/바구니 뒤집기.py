# 바구니 N개 (1~N까지)
# m회 바구니 순서를 역순으로 만들거임
# 역순으로 바꿀 때, 범위를 정하고, 범위에 있는 바구니의 순서를 역순으로 함

n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
temp = [0 for _ in range(n)]

for a in range(m):
    i, j = map(int, input().split())
    temporary = i-1
    
    for e in range(j-1, i-2, -1):
        temp[temporary] = arr[e]
        temporary += 1
    for ee in range(i-1, j):
        arr[ee] = temp[ee]
print(*(arr))
