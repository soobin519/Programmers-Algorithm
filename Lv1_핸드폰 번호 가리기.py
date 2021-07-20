def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):  
        answer+='*'
    for j in range(len(phone_number)-4, len(phone_number)):
        answer+=phone_number[j]
    return answer

#solution2
#범위를 배열의 인덱스 개념을 이용하여 설정할 수 있다. 
def solution(phone_number):
    answer = ''
    for i in range(0, len(phone_number[0:-4])):
        answer = answer + "*"
    answer = answer + phone_number[-4:]
    return answer
