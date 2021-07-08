#solution1 - 실행시간이 다소 오래 걸림
def solution(left, right):
    answer = 0
    count=0
    while(left<=right):
        for i in range(1,left+1):
            if(left%i==0):
                count+=1
        if(count%2==0):
            answer+=left
        else: 
            answer-=left
        left+=1
        count=0
    return answer

#solution2 - 제곱수는 약수의 개수가 홀수라는 사실을 알면 쉽게 풀어낼 수 있다.
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
