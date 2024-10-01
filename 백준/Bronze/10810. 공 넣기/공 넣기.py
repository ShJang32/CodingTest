# 바구니 n개
# 바구니 속 공 번호: n번
# 공 개수는 많이
# 1바구니 1공 / 첫 바구니는 패스

# 앞으로 m번 공 추가 / 모두 같은 번호 공 넣기
# 바구니에 공이 있으면 공 빼고 새로 넣기 / 공 넣을 바구니는 연속됨

n, m = map(int, input().split())
arr = [0]

for _ in range(m):
    i, j, k = map(int, input().split()) # i~j 까지 k번 공 넣기
    
    for index in range(i-1, j):
        # 배열 자리수 = 0 -> 만약에 자리가 부족하면 자리수 넓히기
        if (len(arr)) < j:
            for _ in range(n - len(arr)):
                arr.append(0)
        arr[index] = k
print(*(arr))