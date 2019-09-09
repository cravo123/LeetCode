import collections

# Solution 1, with sorting
class Solution:
    def change(self, word):
        d = collections.Counter()
        for c in word:
            if c.isalpha():
                d[c.lower()] += 1
        return d
    
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target = self.change(licensePlate)
        words.sort(key=lambda x:len(x))
        for word in words:
            d = self.change(word)
        
            if all(d[c] >= target[c] for c in target):
                return word

# Solution 2, without sorting
class Solution:
    def change(self, word):
        d = collections.Counter()
        for c in word:
            if c.isalpha():
                d[c.lower()] += 1
        return d
    
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target = self.change(licensePlate)
        
        res = None
        
        for word in words:
            if res is None or len(res) > len(word):
                d = self.change(word)
                if all(d[c] >= target[c] for c in target):
                    res = word
        return res