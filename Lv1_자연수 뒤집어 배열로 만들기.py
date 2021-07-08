#내림차순 정렬이 아닌 자연수 뒤집기!!
def solution(n): 
    answer=[]
    l=list(str(n))
    for i in reversed(range(len(l))):
        answer.append(int(l[i]))    
    return(answer)

