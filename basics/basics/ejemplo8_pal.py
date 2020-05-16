
def other_way(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    return False


def palindrom(word):
    reversed_letters = []
    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    if word != reversed_word:
        print('Not a palindrom')
    else:
        print('Yeah, It is a Palindrom')


if __name__ == '__main__':
    word = raw_input('Type a word: ')
    palindrom(word)
