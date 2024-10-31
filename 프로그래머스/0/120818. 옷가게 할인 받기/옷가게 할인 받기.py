def solution(price):
    answer = 0
    
    if 300000 <= price < 500000:
        answer = int(price - price * 0.1)
    elif 100000 <= price < 300000:
        answer = int(price - price * 0.05)
    elif 10 <= price < 100000:
        answer = int(price)
    elif price >= 500000:
        answer = int(price - price * 0.2)
    return answer

# 100000 -> 5, 300000 -> 10, 500000 -> 20