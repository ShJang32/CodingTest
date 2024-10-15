# 단어 s 입력
# 단어에 포함되어 있는 알파벳이 처음 등장하는 위치를 출력
# 포함되어 있지 않으면 -1 출력

s = input() # baekjoon
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for alpha in alphabet: # a
    flag = 0
    for index in range(len(s)):
        if (alpha == s[index]):
            print(index, end=' ')
            flag = 1
            break
    if (flag != 1):
        print(-1, end=' ')