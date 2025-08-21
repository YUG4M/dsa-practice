a=["apple", "banana", "kiwi", "fig", "grapes"]
c={}
for i in a:
    wordlen= len(i)
    if wordlen not in c:
        c[wordlen]= [i]
    else:
        c[wordlen].append(i)