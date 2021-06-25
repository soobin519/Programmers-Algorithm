a, b = map(int, input().strip().split(' '))
for i in range(0,b): 
    for j in range(0,a):
        print('*', end='')
    print("")

#solution2
    
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)
