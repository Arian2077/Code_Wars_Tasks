def solution(number):
    if number < 0:
        return 0
    result = 0
    for i in range(number):  
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

