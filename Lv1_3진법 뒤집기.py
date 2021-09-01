def solution(n):
    answer = 0
    temp=[]
    while n>0:
        temp.append(n%3)
        n=n//3
    for i in range(len(temp)):
        answer+=temp[i]*(3**(len(temp)-i-1))        
    return answer

#solution2
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
#int(문자, n진법) 을 사용하면 n진법에서 10진법으로 변환할 수 있다.
