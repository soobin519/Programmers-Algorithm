Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:44:01) 
[Clang 12.0.0 (clang-1200.0.32.27)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(s):   
    words_list = s.split(" ")
    list= []    
    for word in words_list: #단어의 길이만큼 반복
        new_words=''
        for j in range(0, len(word)):
            #new_words+=word[j].upper() if j%2==0 else word[j].lower()
            if j%2==0:
                new_words += word[j].upper()                
            elif j%2==1:
                new_words += word[j].lower()
        list.append(new_words)     
    return ' '.join(list)