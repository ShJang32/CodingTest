a, b = map(str, input().split())

a = int(''.join(list(reversed(a))))
b = int(''.join(list(reversed(b))))

print(max(a, b))