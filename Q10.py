import string

def pangram(text):
    for i in string.ascii_lowercase:
        if i not in text.lower():
            return False
    return True

print(pangram("The quick brown fox jumps over the lazy dog."))
