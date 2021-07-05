def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer+=(a[i]*b[i])
    return answer

#solution2 - zip()이용하기
def solution(a, b):

    return sum([x*y for x, y in zip(a,b)])
