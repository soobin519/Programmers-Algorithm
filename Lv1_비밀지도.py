def solution(n, arr1, arr2):
    answer = [0]*n
    m1,m2 = [2]*n, [2]*n
    for i in range(n):
        #이진수 변환
        m1[i]=format(arr1[i],'b')
        m2[i]=format(arr2[i],'b')
        #1->#로 변환
        m1[i]=m1[i].replace('1','#')        
        m2[i]=m2[i].replace('1','#')       
        #자릿수 맞추기
        m1[i]=m1[i].zfill(n)
        m2[i]=m2[i].zfill(n)

    #지도 완성
    for i in range(n):
        s=''
        for j in range(n):
            if m1[i][j] =='#' or m2[i][j] =='#':
                s+='#'
            else:
                s+=' '
        answer[i]=s

    return answer
