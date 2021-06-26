
def solution(n):
    answer = 0
    a=list(str(n))
    a.sort(reverse=True)
    k=len(a)-1
    for i in a:        
        answer+=int(i)*(10**k)
        k-=1
    return answer

#solution2
#join 함수:  '구분자'.join(리스트)
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
