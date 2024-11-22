def solution(num):
    answer = 'Even'
    
    num = abs(num) # num은 int 범위의 정수이므로, 음수를 고려해서 절대값 만들어주기
    
    for i in range(num):
        if num % 2 == 0 :
            answer = 'Even'
        else:
            answer = 'Odd'
    return answer