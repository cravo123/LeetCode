import collections

# Solution 1, hashmap
class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        
        n = len(words1)
        
        d = collections.defaultdict(set)
        
        for w1, w2 in pairs:
            d[w1].add(w2)
            d[w2].add(w1)
        
        
        for w1, w2 in zip(words1, words2):
            if w1 == w2 or w2 in d[w1] or w1 in d[w2]:
                continue
            return False
        
        return True

# Solution 2, hashmap is not necessary
class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        
        d = set(tuple(x) for x in pairs)
         
        for w1, w2 in zip(words1, words2):
            if w1 == w2 or (w1, w2) in d or (w2, w1) in d:
                continue
            return False
        
        return True