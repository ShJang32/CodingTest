def solution(a, b):
    answer = 0
    
    if (a <= b):
        for num in range(a, b+1):
            answer += num
        return answer
    else:
        for num in range(a, b-1, -1):
            answer += num
        return answer