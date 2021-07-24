def valid_palindrome(word):
    reverse_words = []
    for i in range(len(word)-1,-1, -1):
        reverse_words.append(word[i])
    new_word = ''.join(reverse_words)
    print(new_word)
    if new_word == word:
        return True
    else:return False

print(valid_palindrome('level'))
