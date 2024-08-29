total = int(input())
types = int(input())
temp = 0

for _ in range(types):
    price, quantity = map(int, input().split())
    temp += price * quantity

if (temp == total):
    print("Yes")
else:
    print("No")