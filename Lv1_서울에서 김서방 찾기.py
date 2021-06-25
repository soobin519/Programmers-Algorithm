def solution(seoul):
    answer=''
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            answer =("김서방은 %d에 있다" %i)
    return answer

#solution2
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
