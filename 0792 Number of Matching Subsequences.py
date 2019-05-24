import collections

# Solution 1,

# Solution 2.1,
# Use collections.Counter() to avoid duplicate check
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
        d = collections.Counter(words)
        res = sum(cnt if self.is_subsequence(S, word) else 0 for word, cnt in d.items())
        
        return res

# Solution 2.2, brute-force simulation (TLE)
class Solution:
    def is_subsequence(self, S, word):
        j = 0
        for i in range(len(S)):
            if S[i] == word[j]:
                j += 1
            if j == len(word):
                return True
           
        return False
        
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        res = sum(1 if self.is_subsequence(S, word) else 0 for word in words)
        
        return res