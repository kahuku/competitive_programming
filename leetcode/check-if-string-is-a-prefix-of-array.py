class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        built_string = ''
        for word in words:
            built_string += word
            if built_string == s:
                return True
        return False