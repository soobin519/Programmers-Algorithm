def solution(n):
    answer = ''
    temp=['4','1','2']
    while n>0:
        remain = n%3
        n=n//3
        
        if remain==0:
            n = n-1
        answer = temp[remain]+answer
    return answer
