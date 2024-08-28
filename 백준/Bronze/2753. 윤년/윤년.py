year = int(input())

# 윤년 =  4의 배수 이면서 100의 배수가 아닐때 or 400의 배수일때
if (year % 4 == 0 and year % 100 != 0):
    print(1)
elif (year % 400 == 0):
    print(1)
else:
    print(0)