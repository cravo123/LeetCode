import collections

class Solution:
    def calc(self, word):
        return collections.Counter(word)
    
    def is_universal(self, word, d):
        t = collections.Counter(word)
        
        for c in d: # need to iterate through d not t!!!
            if t[c] < d[c]:
                return False
        return True
    
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d = collections.Counter()
        for word in B:
            t = self.calc(word)
            for c in t:
                d[c] = max(d[c], t[c])
        
        res = []
        
        for word in A:            
            if self.is_universal(word, d):
                res.append(word)
        
        return res