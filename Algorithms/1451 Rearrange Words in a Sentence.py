# Solution 1, simulation
class Solution:
    def arrangeWords(self, text: str) -> str:
        q = [(len(s), idx, s) for idx, s in enumerate(text.split())]
        q.sort(key=lambda x: (x[0], x[1]))
        
        res = ' '.join([x[2] for x in q])
        
        return res.capitalize()