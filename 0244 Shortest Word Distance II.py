import collections
# Solution 1, Sliding Window
class WordDistance:

    def __init__(self, words: List[str]):
        d = collections.defaultdict(list)
        for i, word in enumerate(words):
            d[word].append(i)
        self.d = d

    def shortest(self, word1: str, word2: str) -> int:
        m, n = len(self.d[word1]), len(self.d[word2])
        res = float('inf')
        i = j = 0
        
        while i < m and j < n:
            v = self.d[word1][i] - self.d[word2][j]
            res = min(res, abs(v))
            
            if v < 0:
                i += 1
            else:
                j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)