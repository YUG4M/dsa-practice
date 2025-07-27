vowels='aeiouAEIOU'
a=''
word=input("Enter a word: ")
for i in word:
    if i not in vowels:
        a+=i
    else:
        a+="*"
print(a)