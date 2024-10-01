# 바구니 n개 (1번 ~ n번), 각 1공, 바구니와 같은 공
# m번 공을 바꾼다.
# 공 바꿀 바구니 2개 선택 후 서로 교환

n, m = map(int, input().split())
arr = [i+1 for i in range(n)] #초기 바구니와 초기 공
temp = 0 #i번째 바구니와 j번째 바구니를 바꿀 때 사용될 임시 저장소

for index in range(m): #바구니의 공 서로 바꾸기
    i, j = map(int, input().split())
    temp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = temp

print(*(arr)) #배열 풀어서 쓰기