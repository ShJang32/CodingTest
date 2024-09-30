n, x = map(int, input().split())
a = list(map(int, input().split()))
results = []

for element in a:
    if element < x:
        print(element, end=' ')