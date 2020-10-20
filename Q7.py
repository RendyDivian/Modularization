def words_to_integers(words):
    words_lengths = []

    for i in words:
        words_lengths.append(len(i))
    return words_lengths

if __name__ == "__main__":
    words = ['list', 'of', 'words']
    print(words_to_integers(words))
