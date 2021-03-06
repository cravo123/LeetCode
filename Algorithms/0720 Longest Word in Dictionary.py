import string

# Solution 1, sort
class Solution:
    def longestWord(self, words: List[str]) -> str:
        res = []
        res_len = 0
        
        seen = set([''])
        
        # words.sort() also works...
        # note that, sort ['a', 'ab', 'b', 'ba']
        # will be ['a', 'ab', 'b', 'ba']
        words.sort(key=lambda x: (len(x), x))
        
        for word in words:
            if word[:-1] in seen:
                if len(word) > res_len:
                    res_len = len(word)
                    res = [word]
                elif len(word) == res_len:
                    res.append(word)
                seen.add(word)
        
        return res[0]

# Solution 2, elegant implementation, we can directly use plain sort...
# So it will sort like
# 'a', 'ab', 'abc', 'b'
class Solution:
    def longestWord(self, words: List[str]) -> str:
        res = ''
        seen = set([''])
        
        words.sort()
        
        for word in words:
            if word[:-1] in seen:
                res = word if len(word) > len(res) else res
                seen.add(word)
        
        return res

# Solution 2, BFS
class Solution:
    def longestWord(self, words: List[str]) -> str:
        d = set(words)
        
        curr = ['']
        
        while curr:
            tmp = []
            
            for word in curr:
                for c in string.ascii_lowercase:
                    new_word = word + c
                    if new_word in d:
                        tmp.append(new_word)
            
            if not tmp:
                return curr[0]
            curr = tmp