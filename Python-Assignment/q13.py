S = 'Python-is-a-programming-language'
ch = '-'
k = 0
while(k < len(S)):
    for i in S:
        if(i == ch):
            print(S[:k])
