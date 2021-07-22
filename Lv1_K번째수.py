def solution(array, commands):
    answer = []
    for i in commands:
        temp=sorted(array[i[0]-1:i[1]])
        print(temp)
        answer.append(temp[i[2]-1])
    return answer

#solution2
#lambda 인자 : 표현식
#map() 함수와 리스트를 인자로 받음
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
