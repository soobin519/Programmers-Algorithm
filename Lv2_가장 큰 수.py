def solution(numbers):
    answer = ''
    if sum(numbers)==0:
        return '0'
    else:    
        temp =[str(i)*3 for i in numbers]
        temp.sort(reverse=True)
        for i in temp:
            answer+=i[:len(i)//3]
        return answer

#solution2
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

#배열.sort(key=lambda x: 정렬기준)
