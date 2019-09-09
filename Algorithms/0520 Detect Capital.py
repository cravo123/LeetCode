# Solution 1, built-in function
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in (word.upper(), word.lower(), word.capitalize())
         
# Solution 2
class Solution:
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word.istitle()