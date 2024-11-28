word = input() # 2 ~ 15
time = 0

for alphabet in word:
    if 65 <= ord(alphabet) <= 67:
        time += 3

    elif ord(alphabet) <= 70:
        time += 4

    elif ord(alphabet) <= 73:
        time += 5

    elif ord(alphabet) <= 76:
        time += 6

    elif ord(alphabet) <= 79:
        time += 7

    elif ord(alphabet) <= 83:
        time += 8

    elif ord(alphabet) <= 86:
        time += 9

    elif ord(alphabet) <= 90:
        time += 10

print(time)