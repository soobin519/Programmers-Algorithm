def solution(arr):
    answer = 0
    for i in range(len(arr)):
        answer+=arr[i]
    answer=answer/len(arr)
    return answer

#solution2 - sum함수를 이용하여 배열의 원소의 합을 구할 수 있음.
def average(list):
    return (sum(list) / len(list))
