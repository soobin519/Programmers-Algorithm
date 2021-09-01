def solution(N, stages):
    answer = []
    fail = [[i]*2 for i in range(0,N+1)]

    #실패율 구하기 
    for i in range(1,N+1):
        cnt=0
        for n in stages: 
            if n>=i: cnt+=1
        #분모가 0이되는 부분을 처리해줘야함!!!!!! 꼼꼼히 문제를 읽을 것.
        if cnt==0: 
            fail[i][1]=0
        else:
            fail[i][1] = stages.count(i)/cnt
    #정렬
    fail= sorted(fail, reverse=True,key=lambda x: x[1])

    for i in range(N+1):
        if fail[i][0]!=0:
            answer.append(fail[i][0])
    return answer


