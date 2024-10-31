def solution(money):
    answer = []
    
    # 커피 개수
    num = money // 5500
    answer.append(num)
    
    # 남는 돈
    charge = money - 5500 * num
    answer.append(charge)
    
    return answer