import collections

# Solution 1, simulation
# Count char frequency and check if each word meet requirement
class Solution:
    def calc(self, word, d):
        d = d.copy()
        for c in word:
            d[c] -= 1
            if d[c] < 0:
                return 0
        return len(word)
    
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = collections.Counter(chars)
        
        res = sum(self.calc(word, d) for word in words)
        
        return res