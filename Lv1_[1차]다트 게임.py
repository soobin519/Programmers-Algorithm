def solution(dartResult):
    n = ''
    box=[]
    for i in dartResult:
        if i.isnumeric():
            n+=i
        elif i == 'S':
            n=int(n)**1
            box.append(n)
            n=''
        elif i == 'D':
            n=int(n)**2
            box.append(n)
            n=''
        elif i == 'T':
            n=int(n)**3
            box.append(n)
            n=''
        elif i == '*':
            box[-1]=box[-1]*2
            if len(box)>1:
                box[-2]=box[-2]*2
        elif i == '#':
            box[-1]=box[-1]*-1
    return(sum(box))
