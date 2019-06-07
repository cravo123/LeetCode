# Solution 1, standardize word
# map each char to its appearance order
class Solution:
    def change(self, word):
        res = []
        d = {}
        for c in word:
            d.setdefault(c, len(d))
            res.append(d[c])
        return ','.join(str(x) for x in res)
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        target = self.change(pattern)
        
        res = [word for word in words if self.change(word) == target]
        
        return res

# Solution 2, hash-map + hash-set
# bisection
class Solution:
    def is_match(self, word, pattern):
        d = {}
        seen = set()
        
        for c1, c2 in zip(word, pattern):
            if c1 in d and d[c1] != c2 or c1 not in d and c2 in seen:
                return False
            d[c1] = c2
            seen.add(c2)
        
        return True
        
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = [word for word in words if self.is_match(word, pattern)]
        
        return res