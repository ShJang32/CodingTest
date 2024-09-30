maximum = 0
max_index = 0

for index in range(1, 10):
    num = int(input())
    
    if num > maximum:
        maximum = num
        max_index = index

print(maximum)
print(max_index)