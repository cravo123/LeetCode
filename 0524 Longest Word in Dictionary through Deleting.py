class Solution:
    def is_eligible(self, curr, target):
        # delete some chars in target to arrive at curr
        i = j = 0
        m, n = len(curr), len(target)
        
        while i < m and j < n:
            if curr[i] == target[j]:
                i += 1
            j += 1
        return i == m
        
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (len(x), x))
        res = ''
        
        for i in range(len(d) - 1, -1, -1):
            if self.is_eligible(d[i], s):
                print(d[i])
                if len(d[i]) >= len(res):
                    res = d[i]
                else:
                    break
        return res