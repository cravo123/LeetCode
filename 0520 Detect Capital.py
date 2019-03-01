# Solution 1
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word in (word.upper(), word.lower(), word.capitalize()):
            return True
        return False

# Solution 2
class Solution:
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word.istitle()