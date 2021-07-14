def solution(x):
    temp=0
    for i in str(x):
        temp+=int(i)
    if x%temp==0:
        return True
    else:
        return False

#solution2
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

