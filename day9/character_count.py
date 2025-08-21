sentence = "Hello World"
charcount = {}

for char in sentence.lower():
    if char != " ":
        if char in charcount:
            charcount[char] += 1
        else:
            charcount[char] = 1

print(charcount)
