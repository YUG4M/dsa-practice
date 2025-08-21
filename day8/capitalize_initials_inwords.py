text = input("Enter a sentence: ")
capitalized = ' '.join(word.capitalize() for word in text.split())
print(capitalized)
