import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = collections.Counter(words)
        
        res = [(-value, key) for key, value in d.items()]
        res.sort()
        res = [x[1] for x in res][:k]
        
        return res