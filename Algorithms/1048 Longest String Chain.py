import collections

# Solution 1, DP, hash table
class Solution:
    def calc_pre(self, word, d):
        for i, c in enumerate(word):
            tmp = word[:i] + word[(i + 1):]
            if tmp in d:
                yield tmp
            
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        
        d = collections.Counter()
        d[''] = 0
        
        for word in words:
            d[word] = 1
            for pre_word in self.calc_pre(word, d):
                d[word] = max(d[word], d[pre_word] + 1)
        
        return max(d.values())