#소수: 1과 자기 자신만을 약수로 가지는 수
#에라토스테네스의 체
def solution(n):
    answer = 0
    temp=[]
    for i in range(0,n+1): temp.append(i)  
    for i in range(2,n+1):
        if temp[i]==0: continue
        for k in range(i+i,n+1,i):
            temp[k]=0
    for a in range(2,n+1):
        if temp[a]!=0: answer+=1    
    return answer

#solution2
#에라토스테네스의 체 응용 
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
