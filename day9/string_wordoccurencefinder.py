sentence = "This is a test. This test is easy."
words = sentence.lower().replace(".", "").split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

repeated = [word for word, count in word_count.items() if count > 1]

print("Repeated words:", repeated)
