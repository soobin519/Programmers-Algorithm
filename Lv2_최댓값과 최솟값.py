def solution(s):
    answer = ''
    temp = []
    for i in s.split(' '):
        temp.append(int(i))
    temp.sort()
    answer=str(temp[0])+' '+str(temp[-1])
    return answer

#solution2
#map(int,a) int형으로 변환해줌!
#max, min 함수 사용
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

#함술를 잘 사용하자.
