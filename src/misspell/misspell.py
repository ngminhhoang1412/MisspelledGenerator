import string
import random


def get_misspelled_word(phrase, misspelled_percentage=0.1):
    new_phrase = []
    words = phrase.split(' ')
    for word in words:
        outcome = random.random()
        if outcome <= misspelled_percentage:
            ix = random.choice(range(len(word)))
            new_word = ''.join([word[w] if w != ix else random.choice(string.ascii_letters) for w in range(len(word))])
            new_phrase.append(new_word)
        else:
            new_phrase.append(word)

    return ' '.join([w for w in new_phrase])


