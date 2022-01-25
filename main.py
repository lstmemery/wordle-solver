# import nltk
# nltk.download('brown')

from nltk.corpus import wordnet




letter_score = {
    "e": 57,
    "a": 43,
    "r": 39,
    "i": 38,
    "o": 37,
    't': 35,
    'n': 34,
    's': 29,
    'l': 28,
    'c': 23,
    'u': 19,
    'd': 17,
    'p': 16,
    'm': 15,
    'h': 15,
    'g': 13,
    'b': 11,
    'f': 9,
    'y': 9,
    'w': 7,
    'k': 6,
    'v': 5,
    'x': 1,
    'z': 1,
    'j': 1,
    'q': 1,
}

# S – 29
# L – 28
# C – 23
# U – 19
# D – 17
# P – 16
# M – 15 +
# H – 15
# G – 13
# B – 11
# F – 9 +
# Y – 9
# W – 7
# K – 6
# V – 5
# X – 1 +
# Z – 1 +
# J – 1 +
# Q – 1



def score_word(word):
    score = 0
    for letter in word:
        score += letter_score[letter]
    return score



if __name__ == '__main__':
    query_word = "soare"
    print(query_word)
    response = input("Wordle Response? ")
    out_word = set()
    in_word = set()
    out_position = set()
    in_position = set()
    words = [word_.lower() for word_ in wordnet.words() if len(word_) == 5 and word_.isalpha()]
    while response != "22222":
        for index, letter in enumerate(response):
            if letter == "0":
                out_word.add(query_word[index])
            elif letter == "1":
                in_word.add(query_word[index])
                out_position.add((index, query_word[index]))
            elif letter == "2":
                in_word.add(query_word[index])
                in_position.add((index, query_word[index]))
            else:
                raise Exception
        print(in_position)
        possible_words = []
        for word in words:
            lower_word = list(word)
            if in_word & set(lower_word) == in_word:
                if len(out_word & set(lower_word)) == 0:
                    if all(lower_word[index] == letter for index, letter in in_position):
                        if not any(lower_word[index] == letter for index, letter in out_position):
                            possible_words.append((word, score_word(word)))
        if not possible_words:
            raise Exception

        skip_doubles = False
        for possible_word, word_score in sorted(possible_words, key=lambda x: x[1], reverse=True):
            print(possible_word, word_score)
            if len(set(possible_word)) == 5:
                print(possible_word)
                response = input("Wordle Response? ")
                if len(response) == 5:
                    query_word = possible_word
                    skip_doubles = True
                    break

        if not skip_doubles:
            print(possible_words[0][0])
            response = input("Wordle Response? ")