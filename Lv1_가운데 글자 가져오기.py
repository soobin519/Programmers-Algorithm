#주의: /는 나눗셈을 의미하며 결과가 float로 나타남, //는 나눗셈을 의미하며 결과가 int로 나타남.
def solution(s):
    answer = ''
    n=len(s)
    if n%2==0: #짝수이면
        answer=s[n//2-1]+s[n//2]       
    else: #홀수이면
        answer=s[(n+1)//2-1]
        
    return answer

#solution2 - 인덱스의 성질을 잘 파악할 것
def string_middle(str):  
    return str[(len(str)-1)//2:len(str)//2+1]
