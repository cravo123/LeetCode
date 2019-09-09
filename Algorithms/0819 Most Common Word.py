import collections

# Solution 1, simulation
class Solution:
    def parse(self, s):
        res = []
        n = len(s)
        i = 0
        while i < n:
            while i < n and not s[i].isalpha():
                i += 1
            j = i
            while j < n and s[j].isalpha():
                j += 1
            if i < n:
                res.append(s[i:j].lower())
            i = j
        return res
        
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = self.parse(paragraph)
        banned = set(banned)
        s = [word for word in s if word not in banned]
        d = collections.Counter(s)
        
        res = d.most_common(1)[0][0]
        
        return res