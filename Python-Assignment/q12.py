S = 'Hello@World#How are(! you? *&'
spl_char = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for x in S:
    if x in spl_char:
        S = S.replace(x, " ")
print(S)
