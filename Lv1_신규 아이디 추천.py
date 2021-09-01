def solution(new_id):
    answer = ''
    s =''
    temp=['.','-','_']
    #1단계
    s = new_id.lower()
    #2단계
    for i in range(len(s)):
        if s[i] in temp or s[i].isalpha() or s[i].isdigit():
            answer+=s[i] 
    #3단계
    while True:
        if ".." not in answer: break
        answer = answer.replace("..", ".")        
    #4단계
    if answer[0]==".": 
        if len(answer)>1: answer=answer[1:]
        else: answer = ' '            
    if answer[-1]==".": 
        if len(answer)>1: answer=answer[:-1]
        else: answer = ' '  
    #5단계
    if answer==' ': answer='a'
    #6단계
    if len(answer)>=16: 
        answer=answer[0:15]
        if answer[-1]=='.': answer=answer[0:14]
    #7단계
    if len(answer)<=2: 
        while True:
            answer+=answer[-1]
            if len(answer)==3: break

    return answer
