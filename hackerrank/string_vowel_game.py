# Chick Fil A Intern application summer 2024
# this problem was very unclear, did not end up solving it
# two players, Alex, Chris
# list of strings
# Alex goes first, then Chris, then Alex, etc
# alex can remove substrings with an odd number of vowels
# chris can remove substrings with an even number of vowels
# whoever can't remove anything loses
# return the winner for each round in an array

def vowel_game(words):
    def remove_vowels(word, num_vowels):
        if num_vowels % 2 == 0:
            return word.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
        else:
            return word.replace("b", "").replace("c", "").replace("d", "").replace("f", "").replace("g", "").replace("h", "").replace("j", "").replace("k", "").replace("l", "").replace("m", "").replace("n", "").replace("p", "").replace("q", "").replace("r", "").replace("s", "").replace("t", "").replace("v", "").replace("w", "").replace("x", "").replace("y", "").replace("z", "")
    def num_vowels(word):
        return word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")
    def remove_vowels_from_words(words):
        return [remove_vowels(word, num_vowels(word)) for word in words]
    def winner(words):
        if len(words) == 0:
            return "Chris"
        elif len(remove_vowels_from_words(words)) == 0:
            return "Alex"
        elif len(remove_vowels_from_words(words)) == 1:
            return "Chris"
        else:
            return winner(remove_vowels_from_words(words))
    return [winner(words[i:]) for i in range(len(words))]