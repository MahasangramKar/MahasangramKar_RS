def acronym(words):
    return ''.join(word[0].upper() for word in words)
words = ["national", "aeronautics", "space", "administration"]
acro = acronym(words)
print("Words:", words)
print("Acronym:", acro)
