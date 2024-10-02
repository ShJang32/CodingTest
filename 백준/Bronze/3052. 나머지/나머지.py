# 나머지 = a % b
# 숫자 10개 입력 받고, 42로 나눈 나머지 구하기
# 그 후 나머지 중에서 서로 다른 값이 몇개 있는지 구하기

balance = []
equal = 0

# 10개 숫자 입력 받기 (0 <= n < 1000)
for _ in range(10):
    n = int(input())

    balance.append(n % 42)

# 나머지 비교해서 결과가 다른 나머지 개수 세기
for i in range(10):
    flag = 0
    for j in range(i+1, 10):
        if balance[i] == balance[j]:
            flag = 1
    equal += flag

print(10 - equal)