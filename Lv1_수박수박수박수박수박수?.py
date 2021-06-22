Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:44:01) 
[Clang 12.0.0 (clang-1200.0.32.27)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(n):
    answer = ''
    for i in range(0,n):
        if i%2 ==0:
            answer+="수"
        else:
            answer+="박"
    return answer

>>> #solution 2
>>> def water_melon(n):
    s = "수박" * n
    return s[:n]
