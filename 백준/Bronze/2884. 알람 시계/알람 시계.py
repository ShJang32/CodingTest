hour, minuite = map(int, input().split())

minuite = minuite - 45

if (minuite < 0):
    hour = hour - 1
    minuite = minuite + 60

    if (hour < 0):
        hour = hour + 24


print(hour, minuite)