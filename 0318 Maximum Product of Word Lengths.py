import collections

# Solution 1, brute-force
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        
        n = len(words)
        
        for i in range(n):
            for j in range(i):
                if len(set(words[i]) & set(words[j])) == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        
        return res

# Solution 2, mark char -> word, still O(n ^ 2)
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = collections.defaultdict(set)
        
        for i, word in enumerate(words):
            for c in word:
                d[c].add(i)
        
        res = 0
        
        for i in range(len(words)):
            for j in range(i):
                if any(i in d[c] and j in d[c] for c in string.ascii_lowercase):
                    continue
                res = max(res, len(words[i]) * len(words[j]))
        
        return res

# Solution 3, better solution, but still TLE
# We need bit-mask to improve further
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = collections.Counter()
        
        for word in words:
            w = collections.Counter(word)
            w = tuple([w[c] for c in string.ascii_lowercase])
            d[w] = max(d[w], len(word))
        
        res = 0
        
        for w1 in d:
            for w2 in d:
                if all(x * y == 0 for x, y in zip(w1, w2)):
                    res = max(res, d[w1] * d[w2])
        
        return res

# Solution 4, optimized on Solution 3
# bit-mask
class Solution:
    def calculate(self, word):
        res = 0
        
        for c in set(word):
            res += 1 << (ord(c) - ord('a'))
        
        return res
        
    def maxProduct(self, words: List[str]) -> int:
        d = collections.Counter()
        
        for word in words:
            v = self.calculate(word)
            d[v] = max(d[v], len(word))
        
        res = 0
        
        for v1 in d:
            for v2 in d:
                if v1 & v2 == 0:
                    res = max(res, d[v1] * d[v2])
        
        return res