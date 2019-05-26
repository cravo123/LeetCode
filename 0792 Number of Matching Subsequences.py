import collections

# Solution 1, idea is caching matching index for eac word in words
# so that we only need to traverse each word once. 
# better is_subsequence function by using char index

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        d = collections.defaultdict(list)
        
        for word in words:
            d[word[0]].append(word[1:])
        
        res = 0
        for c in S:
            t = d[c]
            d[c] = []
            for v in t:
                if v == '':
                    res += 1
                else:
                    d[v[0]].append(v[1:])
        return res

# Solution 1.1, creating list is expensive, 
# so we use same idea as Solution 1, but with iterator
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        d = collections.defaultdict(list)
        
        for word in words:
            it = iter(word)
            d[next(it)].append(it)
        
        res = 0
        for c in S:
            tmp = d[c]
            d[c] = []
            
            for it in tmp:
                x = next(it, None)
                if x is None:
                    res += 1
                else:
                    d[x].append(it)
        return res

# Solution 2.1,
# Use collections.Counter() to avoid duplicate check
class Solution:
    def is_subsequence(self, S, word):
        j, n = 0, len(word)
        
        for c in S:
            if word[j] == c:
                j += 1
            if j == n:
                return True
        return False
    
    # better is_subsequence method using iterator
    # iterator can only be consumed once
    def is_subsequence_better(self, S, word):
        it = iter(S)
        
        return all(c in it for c in word)
        
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        d = collections.Counter(words)
        res = sum(cnt if self.is_subsequence(S, word) else 0 for word, cnt in d.items())
        
        return res

# Solution 2.2, brute-force simulation (TLE)
class Solution:
    def is_subsequence(self, S, word):
        j = 0
        n = len(S)
        for c in word:
            while j < n and S[j] != c:
                j += 1
            if j == n:
                return False
            j += 1
        return True
        
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        res = sum(1 if self.is_subsequence(S, word) else 0 for word in words)
        
        return res