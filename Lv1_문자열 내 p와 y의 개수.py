def solution(s):
    p=0
    y=0
    for i in s:
        if i=='p' or i=='P':
            p+=1
        if i=='y' or i=='Y':
            y+=1
    if p==y:
        return True
    else:
        return False

#solution2 - 함수를 잘 이용하자..
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
