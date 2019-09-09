# Solution 1, Union Find
class Solution:
    def find(self, word, d):
        if word not in d:
            d[word] = word
        else:
            if d[word] != word:
                d[word] = self.find(d[word], d)
        return d[word]
        
    def build(self, pairs):
        # Union-Find
        d = {}
        
        for w1, w2 in pairs:
            p1, p2 = self.find(w1, d), self.find(w2, d)
            if p1 != p2:
                d[p1] = p2
        
        return d
        
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        
        d = self.build(pairs)
        
        for w1, w2 in zip(words1, words2):
            if w1 == w2 or self.find(w1, d) == self.find(w2, d):
                continue
            return False
        return True

# Solution 2, DFS
class Solution:
    def build(self, pairs):
        # build graph
        d = collections.defaultdict(set)
        
        for w1, w2 in pairs:
            d[w1].add(w2)
            d[w2].add(w1)
        
        return d
    
    def dfs(self, w1, w2, d, seen):
        if w1 == w2:
            return True
        
        if w1 not in d:
            return False
        
        seen.add(w1)
        
        for w3 in d[w1]:
            if w3 not in seen and self.dfs(w3, w2, d, seen):
                return True
        
        return False
        
    
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        
        d = self.build(pairs)
        
        for w1, w2 in zip(words1, words2):
            seen = set()
            if not self.dfs(w1, w2, d, seen):
                return False
        return True