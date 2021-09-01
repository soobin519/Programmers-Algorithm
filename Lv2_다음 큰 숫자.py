#2, 8, 16진수는 bin(), oct(), hex() 함수 사용
def solution(n):  
    c= str(bin(n)[2:]).count('1') #1의개수
    while 1:
        n+=1
        if str(bin(n)[2:]).count('1') == c: break       
    return n
