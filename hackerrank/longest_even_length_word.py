# Chick Fil A Intern application summer 2024
# given an array of words, find the longest word of even length. If there is a tie return thre first one. If there are no even length words, reutrn 00

def longest_even_length_word(words):
    longest = ""
    for word in words:
        if len(word) % 2 == 0:
            if len(word) > len(longest):
                longest = word
    return longest if longest != "" else "00"