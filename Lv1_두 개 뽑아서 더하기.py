def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j] not in answer: #중복 방지 코드
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    
    return answer

#solution2
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
#set()함수 이용- 집합의 성질을 이용하여 해결, 단 집합으로 만들어준 후 다시 list로 만들어줘야 함 
