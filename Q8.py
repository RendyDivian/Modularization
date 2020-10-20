def find_longest_word(lwords):
    word = []
    
    for i in lwords:
        word.append(len(i))
    return max(word)

if __name__ == "__main__":
    words = ['find', 'longest', 'words']
    print(find_longest_word(words))
