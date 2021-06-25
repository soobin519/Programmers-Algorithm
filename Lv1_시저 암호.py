
#odr(문자): 해당 문자의 아스키 코드 반환
#chr(숫자): 해당 아스키 코드의 문자 반환 
#소문자: 97~122
#대문자: 65~90
#공백(space): 32
def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if ord(s[i])>=97 and ord(s[i])<=122: #소문자일때
            if (ord(s[i])+n)>=123:
                answer+=chr(ord(s[i])+n-26)
            else:
                answer+=chr(ord(s[i])+n)
        elif ord(s[i])>=65 and ord(s[i])<=90: #대문자일때
            if (ord(s[i])+n)>=91:
                answer+=chr(ord(s[i])+n-26)
            else:
                answer+=chr(ord(s[i])+n)
        elif ord(s[i])==32: #공백일때
            answer+=s[i]      
    return answer

#solution2
#isupper(), islower()함수를 사용하면 대문자, 소문자의 아스키코드 몰라도됨.
def caesar(s, n): 
    s = list(s) #문자열을 리스트로 변환하면 문자 변경 가능-> 공백은 고려 안해도됨.
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
