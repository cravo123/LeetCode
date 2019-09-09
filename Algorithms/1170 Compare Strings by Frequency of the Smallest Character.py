# Solution 1, counting-sort idea
class Solution:
    def f(self, word):
        return word.count(min(word))
        
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        max_len = max(len(word) for word in words)
        cnts = [0 for _ in range(max_len + 2)]
        
        for word in words:
            cnts[self.f(word)] += 1
        
        # calc cum-sum, cnts[i] is the number of words such that f(word) >= i
        for i in range(max_len, 0, -1):
            cnts[i] += cnts[i + 1]
        
        res = [cnts[self.f(q) + 1] for q in queries]
        
        return res