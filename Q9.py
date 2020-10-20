def filter_long_words(lwords,n):
    x = []
    for i in lwords:
        if len(i) > n:
            x.append(i)
        else:
            pass
    return x

if __name__ == '__main__':
    words = list(input("Write a list of words: ").split(","))
    search = int(input("Words longer than: "))
    print(filter_long_words(words, search))

