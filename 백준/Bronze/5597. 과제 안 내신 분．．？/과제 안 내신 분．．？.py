# 학생 30명 (1~30)
# 28명 과제 제출, 2명 안낸사람 출석번호
submit = [0 for _ in range(31)]

for _ in range(28):
    n = int(input())
    submit[n] = n

for index in range(1, 31):
    if submit[index] == 0:
        print(index)