def solution(n):
    #삼각형 만들기 
    answer = [[1]*i for i in range(1,n+1)] 
    #x,y좌표 
    x ,y = -1,0
    num=1
    
    for a in range(0,n):
        for b in range(a,n):
            if a%3==0:#아래로
                x+=1               
            elif a%3==1:#오른쪽으로
                y+=1
            elif a%3==2: #위로
                x-=1
                y-=1
                
            answer[x][y]=num
            num+=1
    return sum(answer,[]) #이차원 리스트의 합
