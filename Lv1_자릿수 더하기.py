def solution(n):
    answer = 0
    l=list(str(n))
    for i in range(len(l)):
        answer+=int(l[i])
    return answer

#solution2
def sum_digit(number):
    return sum([int(i) for i in str(number)])
