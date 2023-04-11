class Solution:
    def countVowels(self, word: str) -> int:
        s = 0
        for i in range(len(word)):
            if word[i] in set(('a', 'e', 'i', 'o', 'u')):
                s += ((i + 1) * (len(word) - i))
        return s

class Solution:
    def countVowels(self, word: str) -> int:
        def combs(n): return n * (n + 1) // 2
        s = 0
        all_combs = combs(len(word))
        for i in range(len(word)):
            if word[i] in set(('a', 'e', 'i', 'o', 'u')):
                left_only_combs = combs(i)
                right_only_combs = combs(len(word) - i - 1)
                s += (all_combs - left_only_combs - right_only_combs)
        return s
    
class Solution:
    def countVowels(self, word: str) -> int:
        s = 0
        vowels = set('aeiou')
        for i in range(len(word)):
            if word[i] in vowels:
                s += ((i + 1) * (len(word) - i))
        return s