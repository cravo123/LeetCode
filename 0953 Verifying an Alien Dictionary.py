# Solution 1, map alien alphabet to English, and check if it is sorted
class Solution:
    def change(self, word, d):
        res = [d[c] for c in word]
        res = ''.join(res)
        
        return res
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c:chr(i + ord('a')) for i, c in enumerate(order)}
        
        tmp = [self.change(word, d) for word in words]
        res = tmp[::]
        res.sort()
        
        return res == tmp

# Solution 1.1, customized sorting
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c:i for i, c in enumerate(order)}
        
        words_tmp = words[::]
        words_tmp.sort(key=lambda x: [d[c] for c in x])
        
        return words_tmp == words

# Solution 2, there is no need to sort words actually.
# we can just check if words[i] <= words[i + 1] for all i
class Solution:
    def change(self, word, d):
        res = [d[c] for c in word]
        res = ''.join(res)
        
        return res
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c:chr(i + ord('a')) for i, c in enumerate(order)}
        
        tmp = [self.change(word, d) for word in words]
        
        return all(w1 <= w2 for w1, w2 in zip(tmp, tmp[1:]))
        