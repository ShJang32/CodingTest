import sys

answer_list = []

while True:
    sentence = sys.stdin.readline().rstrip()

    if not sentence:
        break
    
    answer_list.append(sentence)

for answer in answer_list:
    print(answer)