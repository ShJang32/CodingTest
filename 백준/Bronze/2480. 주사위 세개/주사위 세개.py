a, b, c = map(int, input().split())
prize = 0

def is_same(prize):
    if (a == b):
        if (b == c):
            # 3 3 3
            prize = 10000 + a * 1000
            return prize
        else:
            # 3 3 6
            prize = 1000 + a * 100
            return prize
    else:
        if (a == c):
            # 3 6 3
            prize = 1000 + a * 100
            return prize

        else:
            if (b == c):
                # 3 6 6
                prize = 1000 + b * 100
                return prize
            else:  
                # 3 6 5
                prize = max(a, b, c) * 100
                return prize


print(is_same(prize))