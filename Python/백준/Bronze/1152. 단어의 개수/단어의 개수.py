sentence = input()
answer = 0
sentence = sentence + " "

for word in range(len(sentence)):
    if sentence[word] == " " and sentence[word - 1] != " ":
        answer += 1

print(answer)