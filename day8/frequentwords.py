text = input("Enter a sentence: ")
words = text.lower().split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

for word in sorted(freq, key=freq.get, reverse=True):
    print(f"{word}: {freq[word]}")
