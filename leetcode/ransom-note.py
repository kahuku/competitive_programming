from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dd = defaultdict(int)
        for letter in magazine:
            dd[letter] += 1
        
        for letter in ransomNote:
            dd[letter] -= 1
        
        return sorted(list(dd.values()))[0] >= 0