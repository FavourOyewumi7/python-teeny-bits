def capitalize(word):
    if word.istitle()or word.islower() or word.isupper():
        return True
    else: return False

print(capitalize('woRd'))
