Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:44:01) 
[Clang 12.0.0 (clang-1200.0.32.27)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(n):
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            sum += i
    return sum

>>> #solution 2
>>> def solution2(num):
	return sum([i for i in range(1,n+1) if n%i==0])