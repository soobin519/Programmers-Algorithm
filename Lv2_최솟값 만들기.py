def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    while 1:
        if len(A)==0: break
        answer+=A[0]*B[0]
        A.remove(A[0])
        B.remove(B[0])
    return answer

#solution2
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
