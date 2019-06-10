# Solution 1, simulation
# Check if word can be spelled by one line in keyboard
class Solution:
    def findWords(self, words: 'List[str]') -> 'List[str]':
        line1, line2, line3 = (set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm'))
        res = []
        for word in words:
            words = word.lower()
            if any(all(c in line for c in words) for line in [line1, line2, line3]):
                res.append(word)
        return res
