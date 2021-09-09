def solution(s):
    cnt1,cnt2=0,0
    while True:
        for i in s:
            if i =='0':
                cnt2+=1
        s=s.replace('0','')
        s=format(len(s),'b')
        cnt1+=1  
        if s=='1': break
    return [cnt1,cnt2]
