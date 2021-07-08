#실행속도가 매우 느린 solution
def solution(nums):
    answer = 0
    result=True
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                a=nums[i]+nums[j]+nums[k]
                for n in range(2,a):
                    if a%n==0:
                        result=True
                        break
                    else:
                        result=False
                if result==False:
                    answer+=1
    return answer

#soultion2
#combination함수를 사용하면 실행속도를 높일 수 있다.
#if문 의 위치를 어디에 두냐에 따라 코드의 길이가 달라진다.
#else문을 for문과 같은 줄에 쓰게되면, for문의 반복이 끝나고나서 else문이 실행(break로 빠져나가지 않는다면)

def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
