# 킹1, 퀸1, 룩2, 비숍2, 나이트2, 폰8
piece = list(map(int, input().split()))
origin = [1, 1, 2, 2, 2, 8]
answer = [0, 0, 0, 0, 0, 0]

for index in range(len(origin)):
  answer[index] = origin[index] - piece[index]

print(*answer)