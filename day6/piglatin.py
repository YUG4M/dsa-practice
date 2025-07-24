def to_pig_latin(word):
    if len(word) == 0:
        return ""
    pig_latin = word[1:] + word[0] + "ay"
    return pig_latin

print(to_pig_latin("python"))