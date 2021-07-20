def solution(s):
    answer = ''
    a = list(s)
    a.sort(reverse=True)
    for i in a:
        answer+=i
    return answer

#solution2
def solution(s):
    return ''.join(sorted(s, reverse=True))

#문자열을 이어붙일때, join을 사용하면 좋다.
#문자열 정렬은 sorted를 사용하면 된다.
#배열 정렬은 sort!!!!
