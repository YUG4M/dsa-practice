sentence = "Madam Arora teaches malayalam and noon class"
words = sentence.split()

palindromes = []

for word in words:
    if word.lower() == word[::-1].lower():
        palindromes.append(word)

print("Palindromes:", palindromes)
