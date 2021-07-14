#행렬의 크기를 정해주는 것이 중요하다. 
def solution(arr1, arr2):
    answer = [[] for x in range(len(arr2))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j]+arr2[i][j])
    return answer

#solution2
#이중 for문도 한줄로 작성이 가능하다. 
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
