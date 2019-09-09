# Solution 1, two-pointer

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {c:i for i, c in enumerate(S)}
        
        curr = 0
        res = []
        prev = -1
        
        for i, c in enumerate(S):
            curr = max(curr, d[c])
            if curr == i:
                res.append(i - prev)
                prev = i
        
        return res