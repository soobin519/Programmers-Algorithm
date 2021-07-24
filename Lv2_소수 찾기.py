# permutations 순열
# combinations 조합
from itertools import permutations
def solution(numbers):
    answer=0
    #숫자 조합
    for i in range(1,len(numbers)+1):
        temp=set(permutations(numbers,i))
        for i in temp:
            a=''.join(i)
            if a[0]!='0' and a!='1': #맨 앞의 수가 O이 아니고, 1이 아닌 경우
                #소수 찾기            
                for i in range(2,int(a)):
                    if int(a)%i==0: break
                else: answer+=1
    return answer

#solution2
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
