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