# n개의 숫자 공백 없이 입력받음
# 모두 합해서 출력

num = int(input())
number = input()
total = 0

for i in range(num):
    total = total + int(number[i])

print(total)