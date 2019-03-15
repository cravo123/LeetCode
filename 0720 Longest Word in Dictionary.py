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