n = int(input())
arr = list(map(int, input().split()))
minimum = 1000000
maximum = -1000000

for element in arr:
    if element < minimum:
        minimum = element
        
    if element > maximum:
        maximum = element

print(minimum, maximum)