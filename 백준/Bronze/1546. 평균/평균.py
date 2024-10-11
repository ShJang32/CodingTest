# 세준이는 인성이 쓰레기라 기말고사 점수를 조작한다.
# 자기 점수 중 최댓값 = m
# 모든 점수를 점수/m*100
# 양심적이네
# 새로운 평균 출력, 소수점 1자리

n = int(input())
grade = list(map(int, input().split()))
m = max(grade)
total = sum(grade)

new_total = total / m * 100
print(new_total / n)