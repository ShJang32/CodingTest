# 몇번 문자열을 입력받을지 받고,
# 개수 만큼 문자열 입력 받는다.
# 첫글자와 마지막 글자를 출력한다.

num = int(input())

for i in range(num):
    word = input()
    print(word[0], end='')
    print(word[-1])