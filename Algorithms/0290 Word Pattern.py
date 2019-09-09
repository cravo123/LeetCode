# Solution 1, dict + set, set is used to cache used words
class Solution:
    def wordPattern(self, pattern: str, S: str) -> bool:
        S = S.split()
        
        if len(S) != len(pattern):
            return False
        
        d = {}
        seen = set()
        
        for c, word in zip(pattern, S):
            if c in d and d[c] != word:
                return False
            elif c not in d and word in seen:
                return False
            elif c not in d:
                d[c] = word
                seen.add(word)
        return True

# Solution 2, transform to standard representation
class Solution:
    def transform(self, words):
        d = {}
        
        res = []
        
        for word in words:
            res.append(d.setdefault(word, len(d)))
        
        return res
        
    def wordPattern(self, pattern: str, S: str) -> bool:
        
        return self.transform(pattern) == self.transform(S.split())