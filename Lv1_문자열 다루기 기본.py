def solution(s):
    answer = False
    n=len(s)
    if n==4 or n==6:
        #str.isdigit()와 str.isalpha()를 사용하여 주어진 문자열이 각각 양의 정수인지 알파벳인지 확인
        answer=s.isdigit()
    return answer

#solution2
def solution2(s):
    return s.isdigit() and len(s) in (4, 6)
